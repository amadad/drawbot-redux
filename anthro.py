import sys
import drawBot as db
from PIL import Image
import os
from pathlib import Path
import time
import anthropic
import base64
from io import BytesIO
import black
import autopep8

class DesignSystem:
    def __init__(self):
        self.client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        self.model = "claude-3-5-sonnet-20241022"
        # Create output directory if it doesn't exist
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.output_dir = os.path.join(script_dir, "output")
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Load and cache DrawBot documentation
        doc_path = os.path.join(script_dir, "drawbotdoc.md")
        with open(doc_path, "r") as f:
            drawbot_doc = f.read()
            print("DrawBot doc length:", len(drawbot_doc))
            print("First 100 chars:", drawbot_doc[:100])
            
        # Cache the documentation in the system prompt
        self.system_prompt = [
            {
                "type": "text",
                "text": """You are an expert DrawBot programmer. Your code MUST follow these rules:
                1. ALWAYS prefix DrawBot functions with 'db.' (db.text(), db.fill(), etc)
                2. NEVER prefix Python variables with 'db.'
                3. Use 4-space indentation inside functions
                4. No spaces before function definitions
                5. All functions must be properly indented
                6. Return only valid, executable Python code"""
            },
            {
                "type": "text",
                "text": drawbot_doc,
                "cache_control": {"type": "ephemeral"}
            }
        ]

    def encode_image(self, image_path):
        """Convert image to base64 JPEG"""
        # Convert to JPEG if not already
        if not image_path.lower().endswith('.jpg'):
            img = Image.open(image_path)
            # Convert to RGB if needed (in case of RGBA PNG)
            if img.mode in ('RGBA', 'P'):
                img = img.convert('RGB')
            # Save as temporary JPEG
            jpeg_path = image_path.rsplit('.', 1)[0] + '_temp.jpg'
            img.save(jpeg_path, 'JPEG', quality=95)
            image_path = jpeg_path

        # Encode the JPEG
        with open(image_path, "rb") as image_file:
            base64_image = base64.b64encode(image_file.read()).decode('utf-8')
        
        # Clean up temp file if created
        if image_path.endswith('_temp.jpg'):
            os.remove(image_path)
            
        return base64_image

    def get_image_input(self):
        """Get image path from user"""
        script_dir = os.path.dirname(os.path.abspath(__file__))
        while True:
            path = input("\nPlease provide the path to your image file: ").strip()
            # Convert relative path to absolute if needed
            if not os.path.isabs(path):
                path = os.path.join(script_dir, path)
            if os.path.exists(path) and path.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.pdf')):
                return path
            print("Invalid path or unsupported file format. Please try again.")

    def analyze_image(self, image_path):
        """Use Claude to analyze the image"""
        print("\n=== IMAGE ANALYSIS ===")
        print("\nAnalyzing image content, layout, form and style...")
        
        image_base64 = self.encode_image(image_path)
        
        prompt = """Please analyze this image and provide a detailed description of:
        1. Content (what's in the image)
        2. Layout (composition, grid, hierarchy)
        3. Form (shapes, lines, typography)
        4. Style (aesthetic, mood, era)
        
        Be specific and technical in your analysis, as this will be used to reproduce the design."""
        
        message = self.client.messages.create(
            model=self.model,
            max_tokens=1024,
            messages=[{
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image", "source": {"type": "base64", "media_type": "image/jpeg", "data": image_base64}}
                ]
            }]
        )
        
        description = message.content[0].text
        print("\nAnalysis:", description)
        return description

    def generate_drawbot_code(self, description):
        """Use Claude to generate DrawBot code"""
        response = self.client.messages.create(
            model=self.model,
            max_tokens=2048,
            system=self.system_prompt,
            messages=[{
                "role": "user", 
                "content": f"""Based on the DrawBot documentation and this visual description, generate executable Python code:

                {description}

                Requirements:
                - Use db.newPage(1000, 1000)
                - Use db.rect(0, 0, db.width(), db.height()) to set a background color
                - All DrawBot functions must be prefixed with 'db.'
                - No preview() or saveImage()
                - Clean, minimal code only"""
            }]
        )
        
        code = response.content[0].text.strip()
        
        # Extract code from markdown if present
        if "```" in code:
            code = code.split("```")[1]
            code = code.replace("python", "", 1).strip()
        
        # Apply black formatting
        try:
            code = black.format_str(code, mode=black.FileMode())
        except:
            pass  # Fallback if black fails
        
        # Apply PEP8 formatting
        code = autopep8.fix_code(code, options={'aggressive': 1})
        
        return code

    def execute_code(self, code, output_name):
        """Execute DrawBot code and save output"""
        print("\n=== EXECUTING CODE ===")
        print("\nGenerated code:")
        print("----------------")
        print(code)
        print("----------------\n")
        
        # Get absolute paths
        script_dir = os.path.dirname(os.path.abspath(__file__))
        drawbot_path = os.path.join(script_dir, "drawBot")
        
        # Ensure output name ends in .png
        output_name = output_name.replace('.pdf', '.png')
        output_path = os.path.abspath(os.path.join(self.output_dir, output_name))
        temp_file = os.path.join(self.output_dir, "temp_drawbot.py")
        
        print(f"Output will be saved to: {output_path}")
        print(f"Temp file at: {temp_file}")
        
        # Create a temporary Python file with path setup
        with open(temp_file, "w") as f:
            f.write("import os, sys\n")
            f.write(f'sys.path.insert(0, r"{script_dir}")\n')
            f.write(f'sys.path.insert(0, r"{drawbot_path}")\n')
            f.write("import drawBot as db\n")
            f.write(f'os.chdir(r"{script_dir}")\n')
            f.write(code)
            if "saveImage" not in code:
                f.write(f'\ndb.saveImage(r"{output_path}")')
        
        try:
            # Use current Python interpreter
            python_path = sys.executable
            print(f"Using Python: {python_path}")
            print(f"Script directory: {script_dir}")
            print(f"DrawBot path: {drawbot_path}")
            result = os.system(f'"{python_path}" {temp_file}')
            
            if result != 0:
                print(f"Error: Command failed with return code {result}")
                return False
                
            if not os.path.exists(output_path):
                print(f"Error: Output file not created at {output_path}")
                return False
                
            print(f"\nOutput saved to: {output_path}")
            os.remove(temp_file)
            return True
        except Exception as e:
            print(f"\nError executing code: {e}")
            if os.path.exists(temp_file):
                os.remove(temp_file)
            return False

    def get_critique(self, original_path, output_path):
        """Use Claude to critique the reproduction"""
        print("\n=== DESIGN CRITIQUE ===")
        
        original_base64 = self.encode_image(original_path)
        output_base64 = self.encode_image(output_path)
        
        prompt = """Please provide a detailed critique comparing the original design to the reproduction:
        1. What works well?
        2. What needs improvement?
        3. Specific suggestions for changes?
        
        Focus on accuracy, fidelity, and technical aspects of the reproduction."""
        
        message = self.client.messages.create(
            model=self.model,
            max_tokens=1024,
            messages=[{
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image", "source": {"type": "base64", "media_type": "image/jpeg", "data": original_base64}},
                    {"type": "image", "source": {"type": "base64", "media_type": "image/jpeg", "data": output_base64}}
                ]
            }]
        )
        
        critique = message.content[0].text
        print("\nCritique:", critique)
        return critique

    def revise_code(self, code, critique):
        """Use Claude to revise code based on critique"""
        print("\n=== CODE REVISION ===")
        
        prompt = f"""Please revise this DrawBot code based on the critique:

        Original Code:
        {code}

        Critique:
        {critique}

        Important: Provide ONLY the revised Python code. No explanations or comments outside the code block.
        The code must:
        1. Use 'db.' prefix for all DrawBot functions
        2. NOT include any saveImage() command
        3. Use proper color values (e.g., db.fill(1, 0, 0) not db.fill((1, 0, 0)))"""
        
        message = self.client.messages.create(
            model=self.model,
            max_tokens=2048,
            messages=[{
                "role": "user",
                "content": prompt
            }]
        )
        
        revised_code = message.content[0].text
        
        # Extract only the code block if wrapped in markdown
        if "```" in revised_code:
            revised_code = revised_code.split("```")[1]
            if revised_code.startswith("python"):
                revised_code = revised_code[6:]
        
        # Remove any saveImage lines
        revised_code = '\n'.join([line for line in revised_code.split('\n') 
                                 if 'saveImage' not in line and 
                                 not line.startswith('Here') and
                                 not line.startswith('#')])
        
        print("\nRevised code:", revised_code)
        return revised_code

    def main(self):
        print("\n=== DESIGN REPRODUCTION SYSTEM ===")
        
        # Step 1: Get and analyze image
        image_path = self.get_image_input()
        description = self.analyze_image(image_path)
        
        # Step 2: Generate and execute initial code
        proceed = input("\nProceed with reproduction? (y/n): ").lower()
        if proceed != 'y':
            return
            
        code = self.generate_drawbot_code(description)
        success = self.execute_code(code, "output_v1.png")
        
        if not success:
            return
            
        # Step 3: Critique and revision
        critique = self.get_critique(image_path, os.path.join(self.output_dir, "output_v1.png"))
        
        proceed = input("\nProceed with revision? (y/n): ").lower()
        if proceed != 'y':
            return
            
        revised_code = self.revise_code(code, critique)
        self.execute_code(revised_code, "output_v2.png")
        
        print("\nDesign reproduction process completed!")

if __name__ == "__main__":
    system = DesignSystem()
    system.main()

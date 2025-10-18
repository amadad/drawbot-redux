import sys
import os
from pathlib import Path
import time
import base64
from io import BytesIO
import black
import autopep8

# Attempt to import drawBot, PIL, and google.generativeai
# These are not strictly needed for the LLM interaction part to be written,
# but are essential for the full script to run.
try:
    import drawBot as db
except ImportError:
    print("Warning: drawBot module not found. Code execution will fail.")
    db = None # Placeholder

try:
    from PIL import Image
except ImportError:
    print("Warning: Pillow (PIL) module not found. Image processing will fail.")
    Image = None # Placeholder

try:
    import google.generativeai as genai
    from google.generativeai.types import Part # CORRECTED IMPORT
    from google.generativeai.types import HarmCategory, HarmBlockThreshold
    from google.generativeai import caching
except ImportError:
    print("Warning: google-generativeai module not found. LLM interaction will fail.")
    genai = None
    Part = None
    HarmCategory = None
    HarmBlockThreshold = None
    caching = None


class DesignSystem:
    def __init__(self):
        if not genai:
            raise ImportError("google-generativeai library is required. Please install it.")

        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        self.model_name = "gemini-1.5-flash-latest" # Or "gemini-1.5-pro-latest"
        
        # Generation config for safety (can be customized)
        self.generation_config = {
            "temperature": 0.7,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 8192, # Increased for code + doc
        }
        self.safety_settings = {
            HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
        }

        # Create output directory if it doesn't exist
        script_dir = Path(__file__).parent.resolve()
        self.output_dir = script_dir / "output"
        self.output_dir.mkdir(exist_ok=True)
        
        # System instruction (rules for DrawBot)
        self.drawbot_system_instruction = Part.from_text(
            """You are an expert DrawBot programmer. Your code MUST follow these rules:
            1. ALWAYS prefix DrawBot functions with 'db.' (db.text(), db.fill(), etc)
            2. NEVER prefix Python variables with 'db.'
            3. Use 4-space indentation inside functions
            4. No spaces before function definitions
            5. All functions must be properly indented
            6. Return only valid, executable Python code. Do NOT include any explanatory text before or after the code block.
            7. Do NOT include `db.newPage()` or `db.saveImage()` unless explicitly asked. Assume the setup and saving is handled externally.
            8. When colors are needed, use `db.fill(r, g, b)` or `db.stroke(r, g, b)` where r,g,b are floats between 0 and 1.
            9. If a background is needed, use `db.rect(0, 0, db.width(), db.height())` after setting the fill color.
            """
        )

        # Load and cache DrawBot documentation
        doc_path = script_dir / "drawbotdoc.md"
        self.cached_drawbot_doc = None
        if doc_path.exists():
            with open(doc_path, "r", encoding="utf-8") as f:
                drawbot_doc_content = f.read()
                print("DrawBot doc length:", len(drawbot_doc_content))
                print("First 100 chars:", drawbot_doc_content[:100])
            
            # Try to find existing cache or create a new one
            # For simplicity in this example, we'll create a new one each time or use a fixed name
            # In a production system, you might list caches and reuse if appropriate.
            cache_name = "drawbot-doc-cache-v1" # Give your cache a meaningful name
            try:
                self.cached_drawbot_doc = caching.CachedContent.get(f"cachedContents/{cache_name}")
                print(f"Reusing existing cache: {self.cached_drawbot_doc.name}")
            except Exception: # google.api_core.exceptions.NotFound or similar
                print(f"Creating new cache: {cache_name}")
                # Cache the documentation. This is an API call.
                # The model used for creating the cache should ideally match the one using it.
                cache_model_name = self.model_name # or "gemini-1.5-pro-latest" if doc is very large/complex
                self.cached_drawbot_doc = caching.CachedContent.create(
                    model=f"models/{cache_model_name}",
                    display_name="DrawBot Documentation Cache",
                    system_instruction=self.drawbot_system_instruction, # Rules can be part of cache context
                    contents=[Part.from_text(drawbot_doc_content)],
                    ttl_seconds=3600 # Cache for 1 hour, adjust as needed
                )
                print(f"Created and using cache: {self.cached_drawbot_doc.name}")
        else:
            print(f"Warning: DrawBot documentation not found at {doc_path}. Code generation quality may be affected.")

        # Initialize the generative model with the system instruction for general tasks
        # For tasks using the cache, the cache's system instruction might take precedence or combine.
        self.model = genai.GenerativeModel(
            model_name=self.model_name,
            generation_config=self.generation_config,
            safety_settings=self.safety_settings,
            system_instruction=self.drawbot_system_instruction # General rules for all interactions
        )
        print(f"Gemini model {self.model_name} initialized.")

    def encode_image(self, image_path_str):
        """Convert image to base64 JPEG"""
        if not Image:
            print("Pillow (PIL) is not available. Cannot encode image.")
            return None
            
        image_path = Path(image_path_str)
        temp_jpeg_path = None
        try:
            img = Image.open(image_path)
            # Convert to RGB if needed (in case of RGBA PNG or other modes)
            if img.mode in ('RGBA', 'P', 'LA'):
                img = img.convert('RGB')
            
            buffer = BytesIO()
            img.save(buffer, 'JPEG', quality=95)
            buffer.seek(0)
            # Gemini's Part.from_data expects raw bytes, not base64 string.
            # We return base64 for consistency with original, but will decode before use.
            return base64.b64encode(buffer.getvalue()).decode('utf-8')

        except Exception as e:
            print(f"Error encoding image {image_path}: {e}")
            return None


    def get_image_input(self):
        """Get image path from user"""
        script_dir = Path(__file__).parent.resolve()
        while True:
            path_str = input("\nPlease provide the path to your image file: ").strip()
            path = Path(path_str)
            if not path.is_absolute():
                path = script_dir / path_str
            
            if path.exists() and path.suffix.lower() in ('.png', '.jpg', '.jpeg', '.tiff', '.webp'):
                return str(path)
            print("Invalid path or unsupported file format (PNG, JPG, JPEG, TIFF, WEBP). Please try again.")

    def analyze_image(self, image_path):
        """Use Gemini to analyze the image"""
        print("\n=== IMAGE ANALYSIS ===")
        print("\nAnalyzing image content, layout, form and style...")
        
        image_base64 = self.encode_image(image_path)
        if not image_base64:
            return "Error: Could not encode image."

        image_bytes = base64.b64decode(image_base64)
        image_part = Part.from_data(data=image_bytes, mime_type="image/jpeg")
        
        prompt = """Please analyze this image and provide a detailed description of:
        1. Content (what's in the image)
        2. Layout (composition, grid, hierarchy)
        3. Form (shapes, lines, typography)
        4. Style (aesthetic, mood, era)
        
        Be specific and technical in your analysis, as this will be used to reproduce the design."""
        
        contents = [prompt, image_part]
        
        try:
            response = self.model.generate_content(
                contents,
                # No specific cache used here, rely on model's general knowledge + system instruction
            )
            description = response.text
            print("\nAnalysis:", description)
            return description
        except Exception as e:
            print(f"Error during image analysis with Gemini: {e}")
            if hasattr(e, 'response') and e.response.prompt_feedback:
                print(f"Prompt Feedback: {e.response.prompt_feedback}")
            return f"Error analyzing image: {e}"


    def generate_drawbot_code(self, description, size):
        """Use Gemini to generate DrawBot code tailored to the original canvas size"""
        width, height = size

        user_prompt = f"""Based on the DrawBot documentation (implicitly provided via cache) and this visual description, generate executable Python code:

        {description}

        Canvas size for reference: {width} × {height} points.

        Your generated code should:
        - Define functions to draw elements if the design is complex.
        - Use db.newPage({width}, {height}) as the first DrawBot command IF it's the main drawing script. 
          However, if you are generating a function to be called by other code, DO NOT include newPage. 
          For this specific task, assume you are generating the main script, so DO include `db.newPage({width}, {height})`.
        - Use db.rect(0, 0, db.width(), db.height()) to set a background color if one is described.
        - Adhere to all DrawBot programming rules provided in the system instructions.
        - Output ONLY the Python code. No explanations, no markdown backticks.
        """
        
        contents_for_generation = [user_prompt]
        request_options = None

        if self.cached_drawbot_doc:
            # If we have cached content, use it.
            # The user_prompt will be combined with the cached document by the model.
            # The system_instruction for the cache creation might override the model's default.
            # Let's make a model instance that will use the cache
            cached_model = genai.GenerativeModel.from_cached_content(self.cached_drawbot_doc)
            print(f"Using cached content ({self.cached_drawbot_doc.name}) for code generation.")
            response = cached_model.generate_content(
                contents_for_generation, # Just the user prompt, cache is implicitly used
                generation_config=self.generation_config,
                safety_settings=self.safety_settings
            )
        else:
            # Fallback if no cache (e.g., doc file not found)
            # The model will rely on its general training and the explicit system_instruction.
            print("No cached documentation available. Generating code without it.")
            # The drawbot_doc_content could be added directly to contents if small enough,
            # but it's better to rely on the cache mechanism.
            # For now, we'll rely on the system instruction and hope for the best.
            response = self.model.generate_content(
                contents_for_generation,
                # system_instruction is already set on self.model
            )


        try:
            code = response.text.strip()

            # Clean up potential markdown
            if code.startswith("```python"):
                code = code[len("```python"):].strip()
            if code.startswith("```"):
                code = code[len("```"):].strip()
            if code.endswith("```"):
                code = code[:-len("```")].strip()

            # Apply black formatting
            try:
                code = black.format_str(code, mode=black.FileMode())
            except black.NothingChanged:
                pass
            except Exception as e_black:
                print(f"Black formatting failed: {e_black}. Using original code.")


            # Apply PEP8 formatting (autopep8 can be aggressive, use with care)
            # code = autopep8.fix_code(code, options={"aggressive": 1}) # Keep aggressive if needed

            return code
        except Exception as e:
            print(f"Error during code generation with Gemini: {e}")
            if hasattr(response, 'prompt_feedback') and response.prompt_feedback:
                 print(f"Prompt Feedback: {response.prompt_feedback}")
            if hasattr(response, 'candidates') and response.candidates:
                for candidate in response.candidates:
                    if candidate.finish_reason != 1 : # 1 = OK
                        print(f"Candidate Finish Reason: {candidate.finish_reason}")
                        print(f"Safety Ratings: {candidate.safety_ratings}")

            return f"# Error generating code: {e}\n# Response was: {getattr(response, 'text', 'N/A')}"


    def execute_code(self, code, output_name_suffix):
        """Execute DrawBot code and save output"""
        if not db or not Image:
            print("DrawBot or Pillow not available. Skipping code execution.")
            return False
            
        print("\n=== EXECUTING CODE ===")
        print("\nGenerated code:")
        print("----------------")
        print(code)
        print("----------------\n")
        
        script_dir = Path(__file__).parent.resolve()
        # Ensure output name ends in .png
        base_name = Path(image_path).stem if 'image_path' in globals() else "design" # Fallback name
        output_file_name = f"{base_name}_{output_name_suffix}.png"
        output_path = self.output_dir / output_file_name
        
        temp_file_path = self.output_dir / "temp_drawbot.py"
        
        print(f"Output will be saved to: {output_path}")
        print(f"Temp file at: {temp_file_path}")
        
        # Create a temporary Python file
        full_code = f"""
import os, sys
script_dir_path = r"{script_dir}"
sys.path.insert(0, script_dir_path) 
# If drawBot is in a subfolder like 'drawBot', adjust path:
# drawbot_lib_path = os.path.join(script_dir_path, "drawBot")
# sys.path.insert(0, drawbot_lib_path)

import drawBot as db
os.chdir(script_dir_path) # For relative asset loading if any

# --- User Generated Code Start ---
{code}
# --- User Generated Code End ---

if 'saveImage' not in '''{code}''': # Check if user code already saves
    if db.pageCount() > 0: # Ensure there's something to save
        db.saveImage(r"{output_path}")
    else:
        print("DrawBot: No pages were drawn, nothing to save.")
else:
    print("DrawBot: saveImage command detected in user code. Assuming manual save.")

if db.pageCount() > 0:
    db.endDrawing() # Clean up
"""
        with open(temp_file_path, "w", encoding="utf-8") as f:
            f.write(full_code)
        
        try:
            python_exe = sys.executable
            print(f"Using Python: {python_exe}")
            # Use subprocess for better control and error capturing in future
            result = os.system(f'"{python_exe}" "{temp_file_path}"') 
            
            if result != 0:
                print(f"Error: DrawBot script execution failed with return code {result}")
                # Consider printing stderr from temp_file_path execution if using subprocess
                return False
                
            if not output_path.exists():
                print(f"Error: Output file not created at {output_path}. Check DrawBot script for errors (e.g., newPage, drawing commands).")
                return False
                
            print(f"\nOutput saved to: {output_path}")
            return str(output_path) # Return path of successfully created image
        except Exception as e:
            print(f"\nError executing DrawBot code: {e}")
            return False
        finally:
            if temp_file_path.exists():
                # os.remove(temp_file_path) # Keep for debugging for now
                print(f"Temporary script kept at {temp_file_path} for debugging.")


    def get_critique(self, original_path, generated_image_path):
        """Use Gemini to critique the reproduction"""
        print("\n=== DESIGN CRITIQUE ===")
        
        original_base64 = self.encode_image(original_path)
        generated_base64 = self.encode_image(generated_image_path)

        if not original_base64 or not generated_base64:
            return "Error: Could not encode one or both images for critique."

        original_img_bytes = base64.b64decode(original_base64)
        generated_img_bytes = base64.b64decode(generated_base64)

        original_part = Part.from_data(data=original_img_bytes, mime_type="image/jpeg")
        generated_part = Part.from_data(data=generated_img_bytes, mime_type="image/jpeg")
        
        prompt = """Please provide a detailed critique comparing the original design (first image) to the reproduction (second image):
        1. What works well in the reproduction compared to the original?
        2. What specific elements or aspects need improvement in the reproduction to better match the original?
        3. Provide concrete suggestions for changes to the DrawBot code (conceptual, not actual code snippets yet) that could achieve these improvements.
        
        Focus on accuracy, fidelity, and technical aspects like color matching, element placement, typography, and overall style replication."""
        
        # The system instruction on self.model (DrawBot rules) isn't strictly necessary here,
        # but it doesn't hurt.
        contents = [prompt, "ORIGINAL:", original_part, "REPRODUCTION:", generated_part]
        
        try:
            response = self.model.generate_content(contents)
            critique = response.text
            print("\nCritique:", critique)
            return critique
        except Exception as e:
            print(f"Error during critique with Gemini: {e}")
            if hasattr(e, 'response') and e.response.prompt_feedback:
                print(f"Prompt Feedback: {e.response.prompt_feedback}")
            return f"Error getting critique: {e}"

    def revise_code(self, original_code, critique, size):
        """Use Gemini to revise code based on critique, using cached docs"""
        print("\n=== CODE REVISION ===")
        width, height = size
        
        user_prompt = f"""Please revise the following DrawBot code based on the provided critique.
        The goal is to make the output of the revised code more closely match the original design that the critique refers to.
        Canvas size for reference: {width} x {height} points.

        Original DrawBot Code:
        ```python
        {original_code}
        ```

        Critique of the code's output compared to the target design:
        {critique}

        Important Instructions for Revision:
        1. Adhere strictly to all DrawBot programming rules (implicitly provided via system instruction and cache).
        2. Focus on addressing the points raised in the critique.
        3. If the original code was missing `db.newPage({width}, {height})`, add it.
        4. Do NOT include any `db.saveImage()` command.
        5. Output ONLY the revised Python code. No explanations, no markdown backticks.
        """
        
        contents_for_revision = [user_prompt]
        response = None

        if self.cached_drawbot_doc:
            cached_model = genai.GenerativeModel.from_cached_content(self.cached_drawbot_doc)
            print(f"Using cached content ({self.cached_drawbot_doc.name}) for code revision.")
            response = cached_model.generate_content(
                contents_for_revision,
                generation_config=self.generation_config,
                safety_settings=self.safety_settings
            )
        else:
            print("No cached documentation available. Revising code without it.")
            response = self.model.generate_content(
                contents_for_revision
                # system_instruction is already set on self.model
            )

        try:
            revised_code = response.text.strip()
            
            if revised_code.startswith("```python"):
                revised_code = revised_code[len("```python"):].strip()
            if revised_code.startswith("```"):
                revised_code = revised_code[len("```"):].strip()
            if revised_code.endswith("```"):
                revised_code = revised_code[:-len("```")].strip()
            
            # Remove any saveImage lines (double check, model should follow instructions)
            lines = revised_code.split('\n')
            cleaned_lines = [line for line in lines if 'saveImage' not in line and not line.strip().startswith("Here's") and not line.strip().startswith("#")]
            revised_code = '\n'.join(cleaned_lines).strip()

            # Apply black formatting
            try:
                revised_code = black.format_str(revised_code, mode=black.FileMode())
            except black.NothingChanged:
                pass
            except Exception as e_black:
                print(f"Black formatting failed for revised code: {e_black}. Using original.")

            print("\nRevised code (raw from model):")
            print(response.text) # Log raw output for debugging
            print("\nRevised code (after cleaning and formatting):")
            print(revised_code)
            return revised_code
        except Exception as e:
            print(f"Error during code revision with Gemini: {e}")
            if hasattr(response, 'prompt_feedback') and response.prompt_feedback:
                 print(f"Prompt Feedback: {response.prompt_feedback}")
            return f"# Error revising code: {e}\n{original_code}" # Return original on error

    def main(self):
        print("\n=== GEMINI DESIGN REPRODUCTION SYSTEM ===")

        # Step 1: Get and analyze image
        global image_path # Make it accessible in execute_code for naming
        image_path = self.get_image_input()
        if not image_path or not Image:
            print("Image path not provided or Pillow not available. Exiting.")
            return

        try:
            with Image.open(image_path) as img:
                width, height = img.size
        except Exception as e:
            print(f"Could not open image to get dimensions: {e}")
            return

        description = self.analyze_image(image_path)
        if description.startswith("Error:"):
            print(description)
            return

        # Step 2: Generate and execute initial code
        proceed = input(f"\nProceed with generating DrawBot code for a {width}x{height} canvas? (y/n): ").lower()
        if proceed != 'y':
            return

        code_v1 = self.generate_drawbot_code(description, (width, height))
        if code_v1.startswith("# Error"):
            print(code_v1)
            return
            
        generated_image_v1_path = self.execute_code(code_v1, "v1_gemini")
        if not generated_image_v1_path:
            print("Initial code execution failed.")
            # Optionally, allow user to manually fix code_v1 and retry here
            return

        # Step 3: Critique and revision
        critique = self.get_critique(image_path, generated_image_v1_path)
        if critique.startswith("Error:"):
            print(critique)
            return

        proceed = input("\nProceed with code revision based on critique? (y/n): ").lower()
        if proceed != 'y':
            return

        code_v2 = self.revise_code(code_v1, critique, (width, height))
        if code_v2.startswith("# Error"):
            print(code_v2)
            # Optionally allow user to try revising again or manually edit
            return
            
        self.execute_code(code_v2, "v2_gemini_revised")

        print("\nDesign reproduction process completed!")

if __name__ == "__main__":
    # Ensure GOOGLE_API_KEY is set in your environment
    if not os.getenv("GOOGLE_API_KEY"):
        print("Error: GOOGLE_API_KEY environment variable not set.")
        sys.exit(1)
    
    # Create a dummy drawbotdoc.md if it doesn't exist for testing
    script_dir = Path(__file__).parent.resolve()
    dummy_doc_path = script_dir / "drawbotdoc.md"
    if not dummy_doc_path.exists():
        print(f"Creating dummy drawbotdoc.md at {dummy_doc_path}")
        with open(dummy_doc_path, "w") as f:
            f.write("# DrawBot Basic Documentation\n\n")
            f.write("## Shapes\n\n`db.rect(x, y, w, h)`: Draws a rectangle.\n`db.oval(x, y, w, h)`: Draws an oval.\n\n")
            f.write("## Color\n\n`db.fill(r, g, b, a=1)`: Sets the fill color.\n`db.stroke(r, g, b, a=1)`: Sets the stroke color.\n\n")
            f.write("## Text\n\n`db.text(txt, (x, y))`: Draws text.\n`db.font(fontName, fontSize)`: Sets font and size.\n\n")
            f.write("## Page\n\n`db.newPage(w, h)`: Creates a new page.\n`db.saveImage(path)`: Saves the canvas.\n`db.width()`: Returns page width.\n`db.height()`: Returns page height.\n")

    system = DesignSystem()
    system.main()
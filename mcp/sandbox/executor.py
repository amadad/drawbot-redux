import asyncio
import dagger
import os
import tempfile
from pathlib import Path
from typing import Dict, Any, Optional
import base64
from datetime import datetime


async def execute_sandboxed(
    code: str,
    output_name: str = "output.png",
    sandbox_type: str = "dagger",
    timeout: int = 30
) -> Dict[str, Any]:
    """Execute DrawBot code in a sandboxed environment."""
    
    if sandbox_type == "dagger":
        return await execute_with_dagger(code, output_name, timeout)
    else:
        return await execute_local_sandbox(code, output_name, timeout)


async def execute_with_dagger(
    code: str,
    output_name: str,
    timeout: int
) -> Dict[str, Any]:
    """Execute DrawBot code using Dagger for containerization."""
    
    timestamp = datetime.now().isoformat()
    
    try:
        async with dagger.Connection() as client:
            # Create a container with Python and DrawBot
            container = (
                client.container()
                .from_("python:3.11-slim")
                # Install system dependencies needed for drawbot-skia
                .with_exec(["apt-get", "update"])
                .with_exec(["apt-get", "install", "-y", 
                           "gcc", "g++", "python3-dev", "build-essential",
                           "libfreetype6-dev", "libjpeg-dev", "libpng-dev"])
                # Install DrawBot-skia (headless version)
                .with_exec(["pip", "install", "--upgrade", "pip"])
                .with_exec(["pip", "install", "drawbot-skia", "pillow"])
                .with_workdir("/app")
            )
            
            # Create the DrawBot script with proper imports
            full_code = f"""
import drawBot as db
from pathlib import Path

# User code
{code}

# Save the output
output_path = Path("/app/{output_name}")
db.saveImage(str(output_path))
print(f"Saved to: {{output_path}}")
"""
            
            # Create and execute the script
            result_container = (
                container
                .with_new_file("/app/script.py", contents=full_code)
                .with_exec(["python", "script.py"])
            )
            
            # Get the output file
            output_file = await result_container.file(f"/app/{output_name}")
            output_contents = await output_file.contents()
            
            # Get execution logs
            stdout = await result_container.stdout()
            stderr = await result_container.stderr()
            
            # Save output locally
            output_dir = Path(__file__).parent.parent.parent / "output"
            output_dir.mkdir(exist_ok=True)
            
            local_output_path = output_dir / f"{timestamp}_{output_name}"
            with open(local_output_path, "wb") as f:
                f.write(output_contents.encode() if isinstance(output_contents, str) else output_contents)
            
            # Convert to base64 for response
            with open(local_output_path, "rb") as f:
                output_base64 = base64.b64encode(f.read()).decode()
            
            return {
                "success": True,
                "output_path": str(local_output_path),
                "output_base64": output_base64,
                "stdout": stdout,
                "stderr": stderr,
                "timestamp": timestamp,
                "sandbox": "dagger"
            }
            
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "timestamp": timestamp,
            "sandbox": "dagger"
        }


async def execute_local_sandbox(
    code: str,
    output_name: str,
    timeout: int
) -> Dict[str, Any]:
    """Execute DrawBot code in a local sandbox (less secure, for development)."""
    
    timestamp = datetime.now().isoformat()
    
    try:
        # Create temporary directory
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            script_path = temp_path / "script.py"
            output_path = temp_path / output_name
            
            # Get the absolute path to drawBot
            project_root = Path(__file__).parent.parent.parent
            drawbot_path = project_root / "drawBot"
            
            # Prepare the script
            full_code = f"""
import sys
import os

# Add DrawBot to path
sys.path.insert(0, r"{str(project_root)}")
sys.path.insert(0, r"{str(drawbot_path)}")

import drawBot as db

# User code
{code}

# Save the output
db.saveImage(r"{str(output_path)}")
print(f"Saved to: {output_path}")
"""
            
            # Write script
            script_path.write_text(full_code)
            
            # Execute with timeout
            proc = await asyncio.create_subprocess_exec(
                "python", str(script_path),
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
                cwd=str(Path(__file__).parent.parent.parent)
            )
            
            try:
                stdout, stderr = await asyncio.wait_for(
                    proc.communicate(),
                    timeout=timeout
                )
            except asyncio.TimeoutError:
                proc.kill()
                return {
                    "success": False,
                    "error": f"Execution timed out after {timeout} seconds",
                    "timestamp": timestamp,
                    "sandbox": "local"
                }
            
            # Check if output was created
            if output_path.exists():
                # Copy to permanent location
                output_dir = Path(__file__).parent.parent.parent / "output"
                output_dir.mkdir(exist_ok=True)
                
                permanent_path = output_dir / f"{timestamp}_{output_name}"
                
                with open(output_path, "rb") as src:
                    output_contents = src.read()
                    
                with open(permanent_path, "wb") as dst:
                    dst.write(output_contents)
                
                # Convert to base64
                output_base64 = base64.b64encode(output_contents).decode()
                
                return {
                    "success": True,
                    "output_path": str(permanent_path),
                    "output_base64": output_base64,
                    "stdout": stdout.decode() if stdout else "",
                    "stderr": stderr.decode() if stderr else "",
                    "timestamp": timestamp,
                    "sandbox": "local"
                }
            else:
                return {
                    "success": False,
                    "error": "No output file generated",
                    "stdout": stdout.decode() if stdout else "",
                    "stderr": stderr.decode() if stderr else "",
                    "timestamp": timestamp,
                    "sandbox": "local"
                }
                
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "timestamp": timestamp,
            "sandbox": "local"
        }


def validate_code(code: str) -> Dict[str, Any]:
    """Basic validation of DrawBot code for security."""
    
    # Forbidden imports/operations
    forbidden = [
        "import os",
        "import subprocess",
        "import socket",
        "__import__",
        "eval",
        "exec",
        "compile",
        "open(",
        "file(",
        "input(",
        "raw_input"
    ]
    
    for forbidden_item in forbidden:
        if forbidden_item in code:
            return {
                "valid": False,
                "reason": f"Forbidden operation: {forbidden_item}"
            }
    
    return {"valid": True}
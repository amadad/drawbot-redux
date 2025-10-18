import asyncio
import dagger


async def test_simple_dagger():
    """Test simple Dagger execution without heavy dependencies."""
    print("Testing Dagger with simple Python script...")
    
    try:
        async with dagger.Connection() as client:
            print("✓ Connected to Dagger")
            
            # Simple Python container
            container = client.container().from_("python:3.11-slim")
            
            # Test script
            test_script = """
print("Hello from Dagger container!")
import sys
print(f"Python version: {sys.version}")
print("Dagger is working!")
"""
            
            # Execute
            result = await (
                container
                .with_new_file("/app/test.py", contents=test_script)
                .with_exec(["python", "/app/test.py"])
                .stdout()
            )
            
            print(f"\nContainer output:\n{result}")
            print("\n✓ Dagger is working correctly!")
            
    except Exception as e:
        print(f"✗ Error: {type(e).__name__}: {e}")


if __name__ == "__main__":
    asyncio.run(test_simple_dagger())
import asyncio
import dagger


async def test_dagger():
    """Test basic Dagger functionality."""
    print("Testing Dagger connection...")
    
    try:
        async with dagger.Connection() as client:
            print("✓ Connected to Dagger")
            
            # Test pulling a container
            container = client.container().from_("python:3.11-slim")
            print("✓ Pulled Python container")
            
            # Test running a command
            result = await container.with_exec(["python", "--version"]).stdout()
            print(f"✓ Executed command: {result.strip()}")
            
            # Test installing packages
            container = container.with_exec(["pip", "install", "--no-cache-dir", "drawbot-skia"])
            print("✓ Installed drawbot-skia")
            
            # Test creating and running a simple DrawBot script
            test_script = """
import drawbot_skia as db
db.newPage(100, 100)
db.fill(1, 0, 0)
db.rect(10, 10, 80, 80)
db.saveImage("/app/test.png")
print("Success!")
"""
            
            result = await (
                container
                .with_new_file("/app/test.py", contents=test_script)
                .with_exec(["python", "/app/test.py"])
                .stdout()
            )
            print(f"✓ DrawBot test: {result.strip()}")
            
            print("\nDagger is working correctly!")
            
    except Exception as e:
        print(f"✗ Error: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(test_dagger())
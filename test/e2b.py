from e2b import Sandbox

# Create a new sandbox
sandbox = Sandbox(template="base")

# Clone your repository or copy your DrawBot script into the sandbox
sandbox.run('git clone https://github.com/typemytype/drawbot.git')

# Navigate to the DrawBot directory and install dependencies if necessary
sandbox.run('cd https://github.com/typemytype/drawbot && pip install -r requirements.txt')

# Run your DrawBot script
drawbot_process = sandbox.process.start('python your-drawbot-repo/generate_drawbot_code.py')

# Wait for the process to complete
drawbot_process.wait()

# Capture and print the output (stdout)
print(drawbot_process.stdout)

# Optionally, capture stderr to handle any errors
print(drawbot_process.stderr)

# Close the sandbox when done
sandbox.close()
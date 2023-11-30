import subprocess
import sys

# Ensure a repository name is provided as a command-line argument
if len(sys.argv) < 2:
    print("Usage: python script.py <day2>")
    sys.exit(1)

day2 = sys.argv[1]

# Run Terraform apply with the desired repository name as a variable
subprocess.run(["terraform", "apply", "-auto-approve", f"-var='day2={day2}'"])


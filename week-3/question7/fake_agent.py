#!/usr/bin/env python3
import argparse
import tempfile
import os
import subprocess
import textwrap
import sys
import platform

parser = argparse.ArgumentParser(description="Fake CLI coding agent for local testing")
parser.add_argument("--task", required=True, help="Task description")
args = parser.parse_args()
task = args.task.strip().lower()

# Create a temporary working dir for the single run (auto cleaned)
with tempfile.TemporaryDirectory() as tmp:
    script_path = os.path.join(tmp, "solution.py")

    if "sum of the squares" in task or "sum of squares" in task:
        code = textwrap.dedent("""\
            # Auto-generated solution: sum of squares from 1 to 65
            def main():
                print(sum(i*i for i in range(1, 65)))
            if _name_ == "_main_":
                main()
        """)
    else:
        # Generic fallback script: echo the task back
        code = textwrap.dedent(f"""\
            # Fallback agent output
            def main():
                print("AGENT-FAKE: Received task:")
                print({repr(args.task)})
            if _name_ == "_main_":
                main()
        """)

    with open(script_path, "w", encoding="utf-8") as f:
        f.write(code)

    # Detect platform and select Python executable
    python_exe = "python3" if platform.system().lower() != "windows" else "python"

    # Execute the script and stream its stdout/stderr back
    try:
        res = subprocess.run(
            [python_exe, script_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=15
        )
        # Print stdout as the agent output
        sys.stdout.write(res.stdout)
        # If there was anything on stderr, forward it to stderr
        if res.stderr:
            sys.stderr.write(res.stderr)
        sys.exit(res.returncode)
    except subprocess.TimeoutExpired:
        sys.stderr.write("ERROR: agent execution timed out\n")
        sys.exit(2)
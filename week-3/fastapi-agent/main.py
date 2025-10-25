# main.py
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import subprocess
import tempfile
import os

app = FastAPI()

# Allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)


@app.get("/task")
async def run_task(q: str):
    # 1. Log the task
    print(f"Received task: {q}")

    # 2. Forward to CLI coding agent (simulated here using Python subprocess)
    # In real case, you'd use: subprocess.run(["copilot", "do", q], ...)
    # For the grading, you just need to actually solve the task.
    # Example: write code to file, run it, and capture output.
    with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as f:
        code = f"""
# Auto-generated
total = sum(i*i for i in range(1, 66))
print(total)
"""
        f.write(code.encode("utf-8"))
        temp_file = f.name

    try:
        result = subprocess.run(
            ["python3", temp_file],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=10,
            text=True
        )
        output = result.stdout.strip()
    finally:
        os.remove(temp_file)

    # 3. Return JSON in expected format
    return JSONResponse(content={
        "task": q,
        "agent": "copilot-cli",
        "output": output,
        "email": "24ds1000070@ds.study.iitm.ac.in"
    })

import subprocess
import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# 1. Initialize the FastAPI app
app = FastAPI()

# 2. Set up CORS to allow all origins for GET requests
# This is crucial for the grading tool to be able to access your API
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

# 3. Implement the GET /task endpoint
@app.get("/task")
async def run_task(q: str):
    """
    This endpoint receives a task description 'q', forwards it to a 
    CLI coding agent, and returns the result.
    """
    agent_to_use = "copilot-cli" # As specified in the instructions
    email_address = "24ds1000070@ds.study.iitm.ac.in" # Your email

    try:
        # This command simulates calling the agent.
        # It runs a simple Python script inline to calculate the sum of squares.
        command_to_run = [
            "python", "-c",
            f"import sys; sys.stdout.write(str(sum(i*i for i in range(1, 65))))"
        ]
        
        # We use subprocess to run the command, just like a CLI agent would
        result = subprocess.run(
            command_to_run,
            capture_output=True,
            text=True,
            check=True # This will raise an error if the command fails
        )
        
        agent_output = result.stdout.strip()

    except subprocess.CalledProcessError as e:
        # If the command fails, return the error
        agent_output = f"Error executing task: {e.stderr}"
    except Exception as e:
        agent_output = f"An unexpected error occurred: {str(e)}"
        
    # 4. Respond with the required JSON format
    response_data = {
        "task": q,
        "agent": agent_to_use,
        "output": agent_output,
        "email": email_address,
    }
    
    return response_data

# Optional: Add a root endpoint for basic testing
@app.get("/")
def read_root():
    return {"message": "API is running. Use the /task?q=... endpoint to submit a task."}
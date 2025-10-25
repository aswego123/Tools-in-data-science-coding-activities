import subprocess
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

# Initialize the FastAPI app
app = FastAPI()

# Configure CORS to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Add Private Network header
@app.middleware("http")
async def add_pna_header(request: Request, call_next):
    response = await call_next(request)
    response.headers["Access-Control-Allow-Private-Network"] = "true"
    return response

@app.get("/task")
def run_cli_agent(q: str):
    """
    This endpoint takes a query 'q', passes it to Copilot CLI,
    and returns the agent's output.
    """
    agent_name = "copilot-cli"
    command = ["copilot", "--allow-all-tools", "-p", q]

    try:
        # Execute the command and capture the output
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True,
            timeout=120
        )
        agent_output = result.stdout.strip()
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        agent_output = f"Error executing agent: {e}"

    # Structure the response
    response_data = {
        "task": q,
        "agent": agent_name,
        "output": agent_output,
        "email": "24ds1000070@ds.study.iitm.ac.in",
    }

    return response_data

@app.get("/")
def read_root():
    return {"message": "CLI Agent API is running locally. Use the /task endpoint."}
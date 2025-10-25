# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "fastapi",
#     "uvicorn",
# ]
# ///

from fastapi import FastAPI, HTTPException
from typing import Dict, List

app = FastAPI()

@app.get("/items")
async def get_items():
    return {"message": "Hello, Items!"}

@app.get("/books")
async def get_books():
    return {"message": "Hello, Books!"}

@app.post
 
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

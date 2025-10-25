import os
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse, JSONResponse
from starlette.middleware.sessions import SessionMiddleware
from authlib.integrations.starlette_client import OAuth

load_dotenv()
app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="super-secret-key")

oauth = OAuth()
oauth.register(
    name="google",
    client_id=os.getenv("GOOGLE_CLIENT_ID"),
    client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={"scope": "openid email profile"},
)

@app.get("/")
async def login(request: Request):
    user = request.session.get("user")
    if user:
        return RedirectResponse("/id_token")
    if "code" in request.query_params:
        token = await oauth.google.authorize_access_token(request)
        request.session["user"] = token
        return RedirectResponse("/")
    return await oauth.google.authorize_redirect(request, request.url)

@app.get("/id_token")
async def get_id_token(request: Request):
    user = request.session.get("user")
    if not user:
        return RedirectResponse("/")
    return JSONResponse({
        "id_token": user["id_token"],
        "client_id": os.getenv("GOOGLE_CLIENT_ID")
    })

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)

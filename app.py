from fastapi import FastAPI
from src.users.router import user_router

app = FastAPI(title="JhakasKart Backend", version="1.0.0")

app.include_router(user_router, prefix="/api", tags=["users"])

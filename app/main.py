from fastapi import FastAPI
from app.routers import authors

app = FastAPI()

app.include_router(authors.router)

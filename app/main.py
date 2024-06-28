from fastapi import FastAPI
from routers import authors

app = FastAPI()

app.include_router(authors.router)

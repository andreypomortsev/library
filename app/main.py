from fastapi import FastAPI
from routers import authors, books

app = FastAPI()

app.include_router(authors.router)
app.include_router(books.router)

from fastapi import FastAPI
from routers import books, customers

app = FastAPI()

app.include_router(customers.router)
app.include_router(books.router)

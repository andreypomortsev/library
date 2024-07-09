from fastapi import FastAPI

from routers import books, customers, loans

app = FastAPI()

app.include_router(customers.router)
app.include_router(books.router)
app.include_router(loans.router)

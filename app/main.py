from fastapi import FastAPI
from app.api.index import api_router

app = FastAPI(
    title="Employee CRUD API",
    description="Structured Employee CRUD application backed by MongoDB"
)

# Include main API router
app.include_router(api_router)


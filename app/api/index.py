from fastapi import APIRouter
from app.api.routes.employee.employee_routes import router as employee_router

api_router = APIRouter()

# Register employee routes once
api_router.include_router(employee_router)

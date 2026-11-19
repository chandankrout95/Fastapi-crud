from fastapi import APIRouter
from app.models.employee import Employee, UpdateEmployee
import app.api.v1.controller.employee.employee_controller as controller

router = APIRouter(prefix="/employees", tags=["Employees"])


@router.get("")
async def get_all_employee():
    return controller.get_all_employees()


@router.post("")
async def create_employee(new_employee: Employee):
    return controller.create_employee(new_employee)


@router.put("/{id}")
async def update_employee(id: str, updated_employee: UpdateEmployee):
    return controller.update_employee(id, updated_employee)


@router.delete("/{id}")
async def delete_employee(id: str):
    return controller.delete_employee(id)

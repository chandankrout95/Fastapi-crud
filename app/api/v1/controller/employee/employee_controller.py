from fastapi import HTTPException
from app.models.employee import Employee, UpdateEmployee
import app.services.employee.employee_service as service


def get_all_employees():
    """Controller function to get all employees."""
    return service.get_all_employees()


def create_employee(new_employee: Employee):
    """Controller function to create a new employee."""
    try:
        inserted_id = service.create_employee(new_employee)
        return {
            "status_code": 201,
            "id": inserted_id,
            "detail": "Employee created successfully"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error {e}")


def update_employee(employee_id: str, updated_employee: UpdateEmployee):
    """Controller function to update an employee."""
    status = service.update_employee(employee_id, updated_employee)
    if status == "invalid_id":
        raise HTTPException(status_code=400, detail="Invalid employee ID format")
    if status == "not_found":
        raise HTTPException(status_code=404, detail="Employee not found")
    return {
        "status_code": 200,
        "detail": "Employee updated successfully"
    }


def delete_employee(employee_id: str):
    """Controller function to delete an employee."""
    status = service.delete_employee(employee_id)
    if status == "invalid_id":
        raise HTTPException(status_code=400, detail="Invalid employee ID format")
    if status == "not_found":
        raise HTTPException(status_code=404, detail="Employee not found")
    return {
        "status_code": 200,
        "detail": "Employee deleted successfully"
    }

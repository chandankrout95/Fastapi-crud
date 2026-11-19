from datetime import datetime
from bson import ObjectId
from app.db.mongodb import collection
from app.schemas.employee import list_data, individual_data
from app.models.employee import Employee, UpdateEmployee


def get_all_employees():
    """Retrieve all employee records from MongoDB."""
    data = collection.find()
    return list_data(data)


def get_employee_by_id(employee_id: str):
    """Retrieve a single employee by their ObjectId."""
    if not ObjectId.is_valid(employee_id):
        return None
    emp = collection.find_one({"_id": ObjectId(employee_id)})
    return individual_data(emp) if emp else None


def create_employee(employee: Employee):
    """Insert a new employee record into MongoDB."""
    doc = dict(employee)
    response = collection.insert_one(doc)
    return str(response.inserted_id)


def update_employee(employee_id: str, updated_employee: UpdateEmployee):
    """Update fields of an existing employee by ObjectId."""
    if not ObjectId.is_valid(employee_id):
        return "invalid_id"

    id_obj = ObjectId(employee_id)
    existing = collection.find_one({"_id": id_obj})
    if not existing:
        return "not_found"

    update_data = {k: v for k, v in dict(updated_employee).items() if v is not None}
    update_data["updated_at"] = int(datetime.timestamp(datetime.now()))

    collection.update_one({"_id": id_obj}, {"$set": update_data})
    return "success"


def delete_employee(employee_id: str):
    """Delete an employee record from MongoDB by ObjectId."""
    if not ObjectId.is_valid(employee_id):
        return "invalid_id"

    id_obj = ObjectId(employee_id)
    response = collection.delete_one({"_id": id_obj})
    if response.deleted_count == 0:
        return "not_found"
    return "success"

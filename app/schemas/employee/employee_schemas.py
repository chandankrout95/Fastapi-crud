def individual_data(employee: dict) -> dict:
    return {
        "_id": str(employee["_id"]),
        "name": employee.get("name", ""),
        "email": employee.get("email", ""),
        "password": employee.get("password", ""),
        "department": employee.get("department", ""),
        "created_at": employee.get("created_at"),
        "updated_at": employee.get("updated_at")
    }


def list_data(employees) -> list:
    return [individual_data(employee) for employee in employees]

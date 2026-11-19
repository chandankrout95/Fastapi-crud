import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
if not MONGO_URI:
    raise ValueError(
        "MONGO_URI environment variable is not set. "
        "Please provide it in your .env file."
    )

DB_NAME = os.getenv("DB_NAME", "employee_db")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "employee_data")

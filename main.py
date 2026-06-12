from fastapi import FastAPI
from pydantic import BaseModel
import mysql.connector

app = FastAPI()

class Employee(BaseModel):
    emp_id: int
    emp_name: str
    salary: float

@app.post("/employee")
def create_employee(employee: Employee):

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root@123",
        database="sandb"
    )

    cursor = conn.cursor()

    sql = """
    INSERT INTO employee
    (emp_id, emp_name, salary)
    VALUES (%s, %s, %s)
    """

    cursor.execute(
        sql,
        (
            employee.emp_id,
            employee.emp_name,
            employee.salary
        )
    )

    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "Employee inserted successfully"}
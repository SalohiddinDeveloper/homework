from database import execute_query


def create_tables():
    employees = """
    CREATE TABLE IF NOT EXISTS employees (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(128),
    phone_number VARCHAR(13),
    password VARCHAR(128),
    start_time VARCHAR(5),
    end_time VARCHAR(5),
    is_login SMALLINT NOT NULL DEFAULT 0
    )"""

    penalties = """
    CREATE TABLE IF NOT EXISTS penalties (
    id SERIAL PRIMARY KEY,
    employee_id INTEGER,
    amount BIGINT,
    created_at VARCHAR(100),
    minutes INTEGER
    )"""

    try:
        execute_query(query=employees)
        execute_query(query=penalties)
    except Exception as e:
        print(e)


def add_employee_query(values: tuple) -> bool:
    try:
        query = """
        INSERT INTO employees
        (full_name, phone_number, password, start_time, end_time)
        VALUES (%s, %s, %s, %s, %s)"""
        execute_query(query=query, params=values)
        return True
    except Exception as e:
        print(e)
        return False


def get_employee_by_phone(phone: str) -> tuple | bool:
    try:
        query = """
        SELECT * FROM employees WHERE phone_number=%s"""
        return execute_query(query=query, params=(phone,), fetch="one")
    except Exception as e:
        print(e)
        return False


def update_is_login(status: int, employee_id: int):
    try:
        query = """
        UPDATE employees SET is_login=%s WHERE id=%s"""
        execute_query(query=query, params=(status, employee_id,))
        return True
    except Exception as e:
        print(e)
        return False


def logout_query():
    try:
        query = """
        UPDATE employees SET is_login=%s WHERE is_login=%s"""
        execute_query(query=query, params=(0, 1,))
        return True
    except Exception as e:
        print(e)
        return False


def get_active_user():
    try:
        query = """
            SELECT * FROM employees WHERE is_login=%s"""
        return execute_query(query=query, params=(1,), fetch="one")
    except Exception as e:
        print(e)
        return False


def add_penalty_query(values: tuple) -> bool:
    try:
        query = """
        INSERT INTO penalties
        (employee_id, amount, created_at, minutes)
        VALUES (%s, %s, %s, %s)"""
        execute_query(query=query, params=values)
        return True
    except Exception as e:
        print(e)
        return False


def get_employee_last_penalty(employee_id):
    try:
        query = """
            SELECT * FROM penalties WHERE employee_id=%s ORDER BY id DESC LIMIT 1"""
        return execute_query(query=query, params=(employee_id,), fetch="one")
    except Exception as e:
        print(e)
        return False

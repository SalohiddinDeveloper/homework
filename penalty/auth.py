from config import admin_phone, admin_password
from queries import get_employee_by_phone, update_is_login


def login() -> str | None:
    phone_number = input("Enter your phone number: ")
    password = input("Enter your password: ")

    employee = get_employee_by_phone(phone=phone_number)
    if employee:
        if employee[3] == password:
            update_is_login(status=1, employee_id=employee[0])
            return "employee"
        else:
            return None

    elif phone_number == admin_phone and password == admin_password:
        return "admin"

    return None






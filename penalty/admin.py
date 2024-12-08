from queries import add_employee_query


def add_employee() -> bool:
    full_name = input('Enter employee full name: ')
    phone = input('Enter employee phone number: ')
    password = input('Enter employee password: ')
    start_time = input("Enter employee's working hours start time: EX: 9:00")
    end_time = input("Enter employee's working hours end time: EX: 18:00")

    if add_employee_query(
            values=(full_name, phone, password, start_time, end_time)
    ):
        return True
    return False


def show_all_employees():
    if not employees:
        print("No employees found.")
        return
    for employee in employees:
        print(f"Full Name: {employee['full_name']}, Phone: {employee['phone_number']}, Start: {employee['start_time']}, End: {employee['end_time']}, Total Penalty: {employee['total_penalty']}")

def delete_employee():
    phone_number = input("Enter the phone number of the employee to delete: ")
    global employees
    employees = [emp for emp in employees if emp['phone_number'] != phone_number]
    print(f"Employee with phone number {phone_number} deleted successfully.")

def search_employee():
    search_term = input("Enter the full name or phone number to search: ")
    found = False
    for employee in employees:
        if search_term in employee['full_name'] or search_term in employee['phone_number']:
            print(f"Full Name: {employee['full_name']}, Phone: {employee['phone_number']}, Start: {employee['start_time']}, End: {employee['end_time']}, Total Penalty: {employee['total_penalty']}")
            found = True
    if not found:
        print("No employee found with that name or phone number.")

def calculate_total_penalties():
    total = 0
    for employee in employees:
        total += employee['total_penalty']
    return total

def total_penalties():
    total = calculate_total_penalties()
    print(f"Total penalties for all employees: {total}")

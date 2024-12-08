from admin import add_employee, show_all_employees, delete_employee,  search_employee, total_penalties
from auth import login
from employee import start_work, end_work, view_penalties
from menu import auth_menu, admin_menu, employee_menu
from queries import create_tables, logout_query


def show_auth_menu():
    print(auth_menu)
    choice = input("Select from menu: ")
    if choice == "1":
        result = login()
        if result == "admin":
            return show_admin_menu()
        elif result == "employee":
            return show_employee_menu()
        print("Invalid username or password")
        return show_auth_menu()
    elif choice == "2":
        print("Good bye !")
        return
    else:
        print("Invalid choice !")
        return show_auth_menu()


def show_admin_menu():
    print(admin_menu)
    choice = input("Select from menu: ")
    if choice == "1":
        if add_employee():
            print("Added employee is added")
        else:
            print("Something wrong")
    elif choice == "2":
        show_all_employees()
    elif choice == "3":
        delete_employee()
    elif choice == "4":
        search_employee()
    elif choice == "5":
        total_penalties()
    elif choice == "6":
        logout_query()
        return show_auth_menu()
    else:
        print("Invalid choice !")
        return show_auth_menu()
    return show_admin_menu()


def show_employee_menu():
    print(employee_menu)
    choice = input("Select from menu: ")
    if choice == "1":
        result = start_work()
        if result == "started":
            print("You have already started the work")
        elif result is True:
            print(f"You start your work on time.")
        elif isinstance(result, int):
            print(f"Sorry, you late {result} minutes, your penalty: {result * 1000} sum")
        else:
            print("Sorry, something went wrong")
    elif choice == "2":
        result = end_work()
        if result == "end":
            print("You have already started the work")
        elif result is True:
            print(f"You start your work on time.")
        elif isinstance(result, int):
            print(f"Sorry, you late {result} minutes, your penalty: {result * 1000} sum")
        else:
            print("Sorry, something went wrong")
    elif choice == "3":
        result=view_penalties()
    elif choice == "4":
        logout_query()
        return show_auth_menu()
    else:
        print("Invalid choice !")
        return show_auth_menu()
    return show_employee_menu()


if __name__ == "__main__":
    create_tables()
    logout_query()
    show_auth_menu()

from datetime import datetime
from utils import calculate_penalty, check_employee_started, fetch_all_penalties
from queries import get_active_user, add_penalty_query


def start_work() -> bool | None | int | str:
    try:
        user = get_active_user()
        if check_employee_started(employee_id=user[0]):
            return "started"
        penalty = calculate_penalty(user_start_time=user[4])
        if penalty < 0:
            return True
        calculated_penalty = penalty * 1000
        current_date = str(datetime.now())
        values = (user[0], calculated_penalty, current_date, penalty)
        add_penalty_query(values=values)
        return penalty
    except Exception as e:
        print(e)
        return None


def end_work() -> bool | None | int | str:
    try:
        user = get_active_user()
        if not check_employee_started(employee_id=user[0]):
            return "not_started"
        penalty = calculate_penalty(user_end_time=user[5])
        if penalty > 0:
            return True
        calculated_penalty = penalty * 1000
        current_date = str(datetime.now())
        values = (user[0], calculated_penalty, current_date, penalty)
        add_penalty_query(values=values)
        return penalty
    except Exception as e:
        print(e)
        return None


def view_penalties() -> str:
    try:
        user = get_active_user()
        penalties = fetch_all_penalties(employee_id=user[0])
        if not penalties:
            return "You have no penalties."
        result = "\nYour Penalties:\n" + "-" * 30 + "\n"
        for penalty in penalties:
            result += f"Date: {penalty[2]}, Amount: {penalty[1]} UZS, Offset: {penalty[3]} mins\n"
        result += "-" * 30
        return result
    except Exception as e:
        return f"Error fetching penalties: {e}"





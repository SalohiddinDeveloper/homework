import math
from datetime import datetime

from queries import get_employee_last_penalty


def calculate_penalty(user_start_time: str):
    start_time_str = datetime.strptime(user_start_time, "%H:%M").time()
    start_time_date = datetime.combine(datetime.now(), start_time_str)

    time_diff = datetime.now() - start_time_date
    penalty = math.floor(time_diff.total_seconds() / 60)
    return penalty


def check_employee_started(employee_id: int):
    last_penalty = get_employee_last_penalty(employee_id=employee_id)
    if last_penalty:
        current_date = str(datetime.now().date())
        if current_date in last_penalty[3]:
            return True
    return False

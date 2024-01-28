# Task 4: Get Upcoming Birthdays

from datetime import datetime, timedelta

test_user_list = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.28"},
    {"name": "Josdf Doe", "birthday": "1989.01.26"},
    {"name": "Jsdfn Doe", "birthday": "1992.01.27"},
    {"name": "sdfn Doe", "birthday": "2000.02.01"},
    {"name": "Jsdfn Doe", "birthday": "1976.02.10"}
  
]

def get_upcoming_birthdays(users=None)-> list:
    """
    Identifies upcoming birthdays from a list of users within the next 7 days.

    Parameters:
    users (list of dicts): A list of dictionaries, each containing 'name' and 'birthday'.

    Returns:
    list of dicts: List of dictionaries with 'name' and adjusted 'birthday' for upcoming greetings.
    """
    if users is None:
        users = []
    today = datetime.today().date()
    birthdays_list = []
    for user in users:
        birthday_this_year = datetime.strptime(str(today.year) + user['birthday'][4:], "%Y.%m.%d").date()
        if 0 <= (birthday_this_year - today).days <= 7:
            if birthday_this_year.weekday() > 4: # Adjusting for weekends
                birthday_this_year += timedelta(days=(7 - birthday_this_year.weekday()))
            birthdays_list.append({'name': user['name'], 'birthday': birthday_this_year.strftime("%Y.%m.%d")})
    return birthdays_list

upcoming_birthdays = get_upcoming_birthdays(test_user_list)
print("Список привітань на цьому тижні:", upcoming_birthdays)
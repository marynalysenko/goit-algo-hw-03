from datetime import datetime 
from datetime import timedelta 
import random
import re

# Task 1: Get Days From Today

test_date1= '2020-10-09'
test_date2 = '2024-10-09'

def get_days_from_today(date_object: str) -> str:
    """
    Calculates the number of days between a given date and today.

    Parameters:
    date_object (str): Date in the format 'YYYY-MM-DD'.

    Returns:
    str: String message with the number of days or an error message.
    """
    try:
        date_parsing = datetime.strptime(date_object, "%Y-%m-%d")
        now_date = datetime.now() 
        days_since = (now_date - date_parsing).days
        return (f'Кількість днів між заданою  та поточною датами: {days_since} дні')
    except Exception:
            return('Ви ввели помилкові дані')
        
print(get_days_from_today(test_date1))
print(get_days_from_today(test_date2))



# Task 2: Lottery Number Generator

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    """
    Generates a set of unique random numbers within a specified range.

    Parameters:
    min (int): Minimum possible number in the set.
    max (int): Maximum possible number in the set.
    quantity (int): The number of numbers to select.

    Returns:
    list: Sorted list of unique random numbers or an empty list if parameters are invalid.
    """
    if min >= max or quantity > (max - min + 1):
        return([]) 
    else:
        unique_numbers = random.sample(range(min, max + 1), quantity)
        return(sorted(unique_numbers))

print(get_numbers_ticket(1, 49, 5))



# Task 3: Normalize Phone Number

test_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def normalize_phone(phone_number) -> str:
    """
    Normalizes a given phone number to a standard format.

    Parameters:
    phone_number (str): The phone number in various formats.

    Returns:
    str: Normalized phone number with country code.
    """
    cleaned_number = ''.join(re.findall(r'\d+', phone_number))
    if not cleaned_number.startswith('38'):
        cleaned_number = '38' + cleaned_number
    return '+' + cleaned_number

for phone in test_numbers:
     print(normalize_phone(phone))   



# Task 4: Get Upcoming Birthdays

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
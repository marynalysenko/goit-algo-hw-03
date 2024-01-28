# Task 1: Get Days From Today

from datetime import datetime 

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

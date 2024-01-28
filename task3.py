# Task 3: Normalize Phone Number

import re

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
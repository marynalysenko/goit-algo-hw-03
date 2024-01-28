# Task 2: Lottery Number Generator

import random

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



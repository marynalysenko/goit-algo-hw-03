# goit-algo-hw-03

## Description

Welcome to the `goit-algo-hw-03` repository for the Data Science course. This repository hosts the third homework assignment, designed to challenge and enhance your skills in algorithmic problem-solving and data analysis in the field of Data Science.

## Homework Assignment 3

### Task 1: Date Difference Function

**Objective:**  
Create a function `get_days_from_today(date)` that calculates the number of days between a given date and the current date.

**Requirements:**
- The function accepts one parameter: `date` — a string representing a date in the format 'YYYY-MM-DD' (e.g., '2020-10-09').
- The function returns an integer indicating the number of days from the given date to the current date. The result should be negative if the given date is later than the current date.
- Only consider the days, ignoring hours, minutes, and seconds.
- Use Python's `datetime` module for date calculations.

**Evaluation Criteria:**
- Correctness of the function: it should accurately calculate the number of days between dates.
- Exception handling: the function should handle incorrect input formats.
- Code readability: the code should be clean and well-documented.

### Task 2: Lottery Number Generator

**Objective:**  
Develop a function `get_numbers_ticket(min, max, quantity)` to generate a set of unique random numbers for lottery tickets.

**Requirements:**
- Function parameters:
  - `min`: the minimum possible number in the set (at least 1).
  - `max`: the maximum possible number in the set (no more than 1000).
  - `quantity`: the number of numbers to select (between `min` and `max`).
- The function generates the specified quantity of unique numbers within the given range.
- The function returns a list of randomly selected, sorted numbers. Numbers in the set should not repeat. If the parameters do not meet the specified limits, the function returns an empty list.

**Evaluation Criteria:**
- Validity of input data: the function should check the correctness of parameters.
- Uniqueness of the result: all numbers in the output should be unique.
- Compliance with requirements: the result should be in the form of a sorted list of unique numbers.
- Code readability: the code should be clean and well-documented.

### Task 3: Phone Number Normalization

**Objective:**  
Implement the function `normalize_phone(phone_number)` to normalize phone numbers into a standard format, removing all unnecessary characters and adding the country code if needed.

**Requirements:**
- The function parameter `phone_number` is a string with the phone number in various formats.
- The function removes all characters except digits and the '+' symbol.
- If the international code is missing, the function adds the code '+38'. This accounts for cases where the number starts with '380' (only '+' is added) and when the number starts without the code ('+38' is added).
- The function returns the normalized phone number as a string.

**Evaluation Criteria:**
- Correctness of the function: it should properly handle different formats of numbers, considering the presence or absence of an international code.
- Code readability: the code should be clean, well-organized, and well-documented.
- Proper use of regular expressions for removing extraneous characters and formatting the number.

### Task 4: Upcoming Birthdays

**Objective:**  
Create the function `get_upcoming_birthdays(users)` to help determine which colleagues to greet for their birthdays.

**Requirements:**
- The function parameter `users` is a list of dictionaries, each containing `name` (user's name, string) and `birthday` (birthday, string in the format 'year.month.date').
- The function should identify whose birthdays are coming up within the next 7 days, including today. If the birthday falls on a weekend, the greeting date is moved to the next Monday.
- The function returns a list of dictionaries, each containing information about the user (key `name`) and the congratulation date (key `congratulation_date`, data in the string format 'year.month.date').

**Evaluation Criteria:**
- Accuracy and correctness in determining birthdays for the next 7 days.
- Proper handling of cases when birthdays fall on weekends.
- Code readability and structure.
from datetime import date

def get_valid_string(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty.")

def get_valid_date(prompt: str) -> date:
    while True:
        try:
            value = input(prompt + " (YYYY-MM-DD): ")
            return date.fromisoformat(value)
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.")

def get_valid_int(prompt: str, min_val: int, max_val: int) -> int:
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            print(f"Value must be between {min_val} and {max_val}.")
        except ValueError:
            print("Please enter a valid integer.")
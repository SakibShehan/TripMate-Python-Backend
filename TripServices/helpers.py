def ask_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")


def ask_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def ask_day_range(trip_days):
    """Ask for a (start_day, end_day) pair and return it as a tuple."""
    while True:
        start_day = ask_int("Main plan start day: ")
        end_day = ask_int("Main plan end day: ")
        if 1 <= start_day <= end_day <= trip_days:
            return (start_day, end_day)
        print(f"Days must be between 1 and {trip_days}, and start can't be after end.")
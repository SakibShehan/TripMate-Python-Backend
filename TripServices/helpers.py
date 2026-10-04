def ask_int(prompt, minimum=1):
    """Keep asking until the user types a whole number >= minimum."""
    while True:
        try:
            value = int(input(prompt))
        except ValueError:                      # typed text like "abc"
            print("Invalid input. Please enter a whole number.")
            continue

        if value < minimum:
            print(f"Number must be at least {minimum}.")
            continue
        return value


def ask_float(prompt, minimum=0):
    """Keep asking until the user types a number >= minimum."""
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if value < minimum:
            print(f"Number cannot be less than {minimum}.")
            continue
        return value


def ask_day_range(trip_days):
    """Ask for (start_day, end_day) and return it as a tuple."""
    while True:
        start_day = ask_int("Main plan start day: ")
        end_day = ask_int("Main plan end day: ")
        if start_day <= end_day <= trip_days:
            return (start_day, end_day)
        print(f"Days must be between 1 and {trip_days}, and start can't be after end.")
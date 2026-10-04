
from TripServices.budget import calculate_per_day_budget, get_budget_status



def ask_day_range(trip_days):
    """Ask for a (start_day, end_day) pair and return it as a tuple."""
    while True:
        start_day = int(input("Main plan start day: "))
        end_day = int(input("Main plan end day: "))
        if 1 <= start_day <= end_day <= trip_days:
            return (start_day, end_day)
        print(f"Days must be between 1 and {trip_days}, and start can't be after end.")



def get_trip_details():
    trip_name = input("Enter the name of your trip: ")
    destination = input("Enter your destination: ")
    country = input("Enter the country (or a tag like 'beach'): ").strip().title()
    trip_days = int(input("Enter the number of days for your trip: "))
    day_range = ask_day_range(trip_days)
    total_budget = float(input("Enter your total budget for the trip: "))

    note = ""
    if input("\nAdd a note? (yes/no): ").lower() == "yes":
        note = input("Enter your note: ")
    else:
        note = ""

    return {
        "trip_name": trip_name,
        "destination": destination,
        "country": country,
        "trip_days": trip_days,
        "day_range": day_range,
        "total_budget": total_budget,
        "note": note,
        "status": get_budget_status(total_budget),
        "per_day_budget": calculate_per_day_budget(total_budget, trip_days),
        "activities": {}
    }
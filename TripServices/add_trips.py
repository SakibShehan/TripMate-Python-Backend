
from TripServices.budget import calculate_per_day_budget, get_budget_status
from TripServices.helpers import ask_int, ask_float, ask_day_range



def get_trip_details():
    trip_name = input("Enter the name of your trip: ")
    destination = input("Enter your destination: ")
    country = input("Enter the country (or a tag like 'beach'): ").strip().title()
    trip_days = ask_int("Enter the number of days for your trip: ")
    day_range = ask_day_range(trip_days)
    total_budget = ask_float("Enter your total budget for the trip: ")

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
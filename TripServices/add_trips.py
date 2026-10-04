
from TripServices.budget import calculate_per_day_budget, get_budget_status


def get_trip_details():
    trip_name = input("Enter the name of your trip: ")
    destination = input("Enter your destination: ")
    trip_days = int(input("Enter the number of days for your trip: "))
    total_budget = float(input("Enter your total budget for the trip: "))

    note = ""
    if input("\nAdd a note? (yes/no): ").lower() == "yes":
        note = input("Enter your note: ")
    else:
        note = ""

    return {
        "trip_name": trip_name,
        "destination": destination,
        "trip_days": trip_days,
        "total_budget": total_budget,
        "note": note,
        "status": get_budget_status(total_budget),
        "per_day_budget": calculate_per_day_budget(total_budget, trip_days),
    }
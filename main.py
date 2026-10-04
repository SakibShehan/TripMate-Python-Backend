#The main file from where the program is run


import json
import os 
print("==========================================")
print("        TripMate - Travel Planner         ")
print("==========================================")




DATA_FILE = "trips_database.json"

#READ DATA: Load previous trips if the file exists, otherwise start fresh
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as file:
        trips = json.load(file)
    print(f"Loaded {len(trips)} previous trip(s) from memory.")
else:
    trips = []
    print("No previous memory found. Starting with an empty trip list.")

  # List to store trip details


def get_trip_details():
    trip_details = {}

    trip_name = input("Enter the name of your trip: ")
    trip_details["trip_name"] = trip_name

    destination = input("Enter your destination: ")
    trip_details["destination"] = destination

    trip_days = int(input("Enter the number of days for your trip: "))
    trip_details["trip_days"] = trip_days

    total_budget = float(input("Enter your total budget for the trip: "))
    trip_details["total_budget"] = total_budget

    Note=None
    Note = input("\nWould you like to add any notes for your trip? (yes/no): ")
    if Note.lower() == "yes":
        note_content = input("Enter your note: ")
    else:
        note_content = ""
    trip_details["note"] = note_content

    if total_budget <  10000:
        status = "Budget is low. Consider increasing your budget for a better experience."
    elif total_budget < 20000:
        status = "Budget is moderate. You can have a decent trip with careful planning."
    else:
        status = "Budget is high. You can enjoy a luxurious trip with this budget."

    trip_details["status"] = status

    per_day_budget = calculate_per_day_budget(total_budget, trip_days)
    trip_details["per_day_budget"] = per_day_budget
    trips.append(trip_details)

    #STORE DATA: Save the updated list back to the file before the script exits
    with open(DATA_FILE, "w") as file:
        json.dump(trips, file, indent=4) 

    return trip_details


def calculate_per_day_budget(total_budget, trip_days):
    if trip_days > 0:
        return total_budget / trip_days
    else:
        return 0.0



def display_trip_details():
    for trip in trips:
        print("\nTrip Name:", trip["trip_name"])
        print("Destination:", trip["destination"])
        print("Number of Days:", trip["trip_days"])
        print("Total Budget:", trip["total_budget"])
        print("Per Day Budget:", trip["per_day_budget"])
        if trip["note"]:
            print("Note:", trip["note"])
        print("Status:", trip["status"])

  



while True:
    print("1.Add Trip 2.View Trips 0.Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        get_trip_details()
        pass
    elif choice == "2":
        display_trip_details()
        pass
    elif choice == "0" or choice == "":
        print("Thank you for using TripMate!")
        break
    else:
        print("Invalid choice. Please try again.")

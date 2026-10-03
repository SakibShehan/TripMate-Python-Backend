#The main file from where the program is run

print("==========================================")
print("        TripMate - Travel Planner")
print("==========================================")


def get_trip_details():
    trip_name = input("Enter the name of your trip: ")
    destination = input("Enter your destination: ")
    trip_days = int(input("Enter the number of days for your trip: "))
    total_budget = float(input("Enter your total budget for the trip: "))
    Note=None
    Note = input("\nWould you like to add any notes for your trip? (yes/no): ")

    if Note.lower() == "yes":
       note_content = input("Enter your notes: ")

    return trip_name, destination, trip_days, total_budget, Note

def calculate_per_day_budget(total_budget, trip_days):
    if trip_days > 0:
        return total_budget / trip_days
    else:
        return 0.0





def display_trip_details(trip_name, destination, trip_days, total_budget, per_day_budget):
    print("\nTrip Details:")
    print(f"Trip Name: {trip_name}")
    print(f"Destination: {destination}")
    print(f"Number of Days: {trip_days}")
    print(f"Total Budget: {total_budget:.2f} TK")
    print(f"Per Day Budget: {per_day_budget:.2f} TK")

    if total_budget <  10000:
        status = "Budget is low. Consider increasing your budget for a better experience."
    elif total_budget < 20000:
        status = "Budget is moderate. You can have a decent trip with careful planning."
    else:
        status = "Budget is high. You can enjoy a luxurious trip with this budget."

    print(f"Budget Status: {status}")


while True:
    print("1.Add Trip 2.View Trips 0.Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        trip_name, destination, trip_days, total_budget, Note = get_trip_details()
        per_day_budget = calculate_per_day_budget(total_budget, trip_days)
        pass
    elif choice == "2":
        display_trip_details(trip_name, destination, trip_days, total_budget, per_day_budget)
        pass
    elif choice == "0" or choice == "":
        print("Thank you for using TripMate!")
        break
    else:
        print("Invalid choice. Please try again.")

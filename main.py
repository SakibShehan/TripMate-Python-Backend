#The main file from where the program is run

print("==========================================")
print("        TripMate - Travel Planner")
print("==========================================")

trip_name = input("Enter the name of your trip: ")
destination = input("Enter your destination: ")
trip_days = int(input("Enter the number of days for your trip: "))
total_budget = float(input("Enter your total budget for the trip: "))
Note=None


per_day_budget = total_budget / trip_days

print("\nTrip Details:")
print(f"Trip Name: {trip_name}")
print(f"Destination: {destination}")
print(f"Number of Days: {trip_days}")
print(f"Total Budget: {total_budget:.2f} TK")
print(f"Per Day Budget: {per_day_budget:.2f} TK")
Note = input("\nWould you like to add any notes for your trip? (yes/no): ")
if Note.lower() == "yes":
    note_content = input("Enter your notes: ")
    print("\nYour Notes:")
    print(note_content)



# The main file from where the program is run
from TripServices.add_trips import get_trip_details
from TripServices.view_trips import display_trip_details
from TripServices.storage import load_trips, save_trips


def main():
    print("==========================================")
    print("        TripMate - Travel Planner         ")
    print("==========================================")

    trips = load_trips()
    print(f"Loaded {len(trips)} previous trip(s).")

    while True:
        print("\n1.Add Trip 2.View Trips 0.Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            trip = get_trip_details()
            trips.append(trip)
            save_trips(trips)
            print("Trip saved!")
        elif choice == "2":
            display_trip_details(trips)
        elif choice == "0":
            print("Thank you for using TripMate!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
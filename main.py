# The main file from where the program is run
from TripServices.add_trips import get_trip_details
from TripServices.view_trips import display_trip_details, show_visited
from TripServices.storage import load_trips, save_trips
from TripServices.activities import add_activity, view_itinerary


def main():
    print("==========================================")
    print("        TripMate - Travel Planner         ")
    print("==========================================")

    trips = load_trips()
    print(f"Loaded {len(trips)} previous trip(s).")

    while True:
        print("\n1.Add Trip \n" \
        " 2.View Trips \n" \
        " 3. Add Activity to a Day  \n" \
        "4. View Itinerary \n" \
        "5. Show Visited Countries/Tags \n" \
        " 0.Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            trip = get_trip_details()
            trips.append(trip)
            save_trips(trips)
            print("Trip saved!")
        elif choice == "2":
            display_trip_details(trips)
        elif choice == "3":
            if add_activity(trips):
                save_trips(trips)
        elif choice == "4":
            view_itinerary(trips)
        elif choice == "5":
            show_visited(trips)
        elif choice == "0":
            print("Thank you for using TripMate!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
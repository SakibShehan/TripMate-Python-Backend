def display_trip_details(trips):
    if not trips:
        print("\nNo trips saved yet.")
        return

    for trip in trips:
        print("\nTrip Name:", trip["trip_name"])
        print("Destination:", trip["destination"])
        print("Number of Days:", trip["trip_days"])
        print("Total Budget:", trip["total_budget"])
        print("Per Day Budget:", trip["per_day_budget"])
        if trip["note"]:
            print("Note:", trip["note"])
        print("Status:", trip["status"])
def display_trip_details(trips):
    if not trips:
        print("\nNo trips saved yet.")
        return

    for trip in trips:
        print("\nTrip Name:", trip["trip_name"])
        print("Destination:", trip["destination"])
        print("Country/Tag:", trip.get("country", "Not set"))
        print("Number of Days:", trip["trip_days"])
        print("Total Budget:", trip["total_budget"])
        print("Per Day Budget:", trip["per_day_budget"])
        if "day_range" in trip:
            start, end = tuple(trip["day_range"])   # list from JSON -> tuple
            print(f"Main plan: day {start} to day {end}")
        if trip["note"]:
            print("Note:", trip["note"])
        print("Status:", trip["status"])

        for day in range(1, trip["trip_days"] + 1):
            activities = trip.get("activities", {}).get(str(day), [])
            if activities:
                print(f"  Day {day} activities: {', '.join(activities)}")
            else:
                print(f"  Day {day} activities: None")


def show_visited(trips):
    """Build a set of unique countries/tags and show it."""
    visited = set()
    for trip in trips:
        country = trip.get("country")
        if country:
            visited.add(country)

    if not visited:
        print("\nNo countries or tags saved yet.")
    else:
        print("\nUnique countries/tags:", ", ".join(sorted(visited)))
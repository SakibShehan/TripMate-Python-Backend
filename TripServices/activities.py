

def choose_trip(trips):
    """Show numbered trips, return the chosen trip dict, or None."""
    if not trips:
        print("\nNo trips saved yet.")
        return None

    print("\nYour trips:")
    for number, trip in enumerate(trips, start=1):
        print(f"{number}. {trip['trip_name']} ({trip['destination']})")

    choice = int(input("Choose a trip number: "))
    if 1 <= choice <= len(trips):
        return trips[choice - 1]

    print("Invalid trip number.")
    return None


def add_activity(trips):
    """Add an activity to a day. Returns True if something was added."""
    trip = choose_trip(trips)
    if trip is None:
        return False

    day_number = int(input(f"Which day (1-{trip['trip_days']})? ")) 
    if day_number > trip["trip_days"]:
        print(f"This trip has only {trip['trip_days']} days.")
        return False

    activity = input("Activity name: ").strip()
    if not activity:
        print("Activity name can't be empty.")
        return False

    day = str(day_number)                      # JSON keys must be text
    activities = trip.setdefault("activities", {})
    activities.setdefault(day, []).append(activity)

    print(f"Added '{activity}' to day {day_number}.")
    return True


def view_itinerary(trips):
    """Print the chosen trip's plan day by day."""
    trip = choose_trip(trips)
    if trip is None:
        return

    print(f"\nItinerary: {trip['trip_name']} ({trip['destination']})")
    activities = trip.get("activities", {})

    for day in range(1, trip["trip_days"] + 1):
        print(f"\nDay {day}")
        day_activities = activities.get(str(day), [])
        if not day_activities:
            print("  No activities planned")
        else:
            for activity in day_activities:
                print(f"  - {activity}")
def calculate_per_day_budget(total_budget, trip_days):
    if trip_days > 0:
        return total_budget / trip_days
    return 0.0


def get_budget_status(total_budget):
    if total_budget < 10000:
        return "Budget is low. Consider increasing your budget for a better experience."
    elif total_budget < 20000:
        return "Budget is moderate. You can have a decent trip with careful planning."
    else:
        return "Budget is high. You can enjoy a luxurious trip with this budget."
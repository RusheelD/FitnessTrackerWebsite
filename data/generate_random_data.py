import random
import json
import sys
import datetime

STRENGTH_ACTIVITY_TYPES = ["push-ups", "sit-ups", "pull-ups"]
CARDIO_ACTIVITY_TYPES = ["running", "cycling"]
NUTRITION_TYPES = ["breakfast", "lunch", "dinner", "snack"]

def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python generate_random_data.py <number_of_days>")
        sys.exit(1)

    output_file = "daily_stats.json"

    try:
        number_of_days = int(sys.argv[1])
    except ValueError:
        print("Please provide a valid integer for the number of days.")
        sys.exit(1)
    
    date_today = datetime.date.today()

    daily_data = {}

    for i in range(number_of_days):
        date = (date_today - datetime.timedelta(days=i)).strftime("%Y-%m-%d")
        data = {"activities": [], "nutrition": []}

        # Generate random activities
        # Generate random unique strength activities
        strength_activities = random.sample(STRENGTH_ACTIVITY_TYPES, k=random.randint(1, len(STRENGTH_ACTIVITY_TYPES)))
        for activity in strength_activities:
            data["activities"].append({
                "activityType": "strength",
                "activityName": activity,
                "count": random.randint(15, 50),
                "minutes": 0
            })

        # Generate random unique cardio activities
        cardio_activities = random.sample(CARDIO_ACTIVITY_TYPES, k=random.randint(1, len(CARDIO_ACTIVITY_TYPES)))
        for activity in cardio_activities:
            data["activities"].append({
                "activityType": "cardio",
                "activityName": activity,
                "count": 0,
                "minutes": random.randint(15, 60)
            })
        
        # Generate random nutrition data
        for meal in NUTRITION_TYPES:
            data["nutrition"].append({
                "mealType": meal,
                "mealName": f"Random {meal.capitalize()} Meal",
                "calories": random.randint(150, 1200)
            })

        daily_data.update({date: data})
    
    with open(output_file, 'w') as file:
        json.dump(daily_data, file, indent=4)

    print(f"Random data generated and saved to {output_file}")

if __name__ == "__main__":
    main()
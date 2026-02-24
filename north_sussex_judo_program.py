# Solihull College and University Centre
# North Sussex Judo Program
# Name - Muhammad Subhan Arif
# ID Number- ARI222004436
# Unit 1 programming (HND Cybersecurity)


#variables section
TRAINING_PLANS = {
    "Beginner": 25.00,
    "Intermediate": 30.00,
    "Elite": 35.00
}# this can be a dictionary to keep track of the expenses
#other fixed prices
PRIVATE_TUITION = 9.50
COMPETITION_FEE = 22.00
WEEKS_PER_MONTH = 4

athletes = {}
application_running = True

#functions
def add_athlete():
    print("Adding new athlete to the program")
    name = input("Input Athlete Name: ")
    age = input("Input Athlete Age: ")
    weight = int(input("Input Athlete Weight: "))
    coaching_hours = int(input("Enter the amount of Coaching Hours 0-20: "))
    competitions = int(input("How many competitions would you like enter this month? 0-4: "))

#check which weight category is the athlete
# 66kg is flyweight - 73kg is lightweight - 81kg is light middleweight, anything above is heavywight
    weight_category = "none"
    if weight <= 66:
        weight_category = "Flyweight"
    elif weight > 66 and weight <= 73:
        weight_category = "Lightweight"
    elif weight > 73 and weight <= 81:
        weight_category = "Light Middleweight"
    elif weight > 81 and weight <= 90:
        weight_category = "Middleweight"
    elif weight > 90 and weight <= 100:
        weight_category = "Light-Heavyweight"
    else:
        weight_category = "Heavyweight"

    print("Select Training Plan:")
    print("1. Beginner")
    print("2. Intermediate")
    print("3. Elite")
    plan_choice = input("Enter choice (1-3): ")

    training_plan = "Beginner"
    weekly_fee = 0
    if plan_choice == "1":
        training_plan = "Beginner"
        weekly_fee = TRAINING_PLANS["Beginner"]
    elif plan_choice == "2":
        training_plan = "Intermediate"
        weekly_fee = TRAINING_PLANS["Intermediate"]
    elif plan_choice == "3":
        training_plan = "Elite"
        weekly_fee = TRAINING_PLANS["Elite"]

    if training_plan == "Beginner" and competitions > 0:
        print("Error: Beginner athletes cannot enter competitions!")
        competitions = 0

    if coaching_hours > 20:
        print("Error: Maximum 20 hours private coaching per month!")
        coaching_hours = 20

    training_cost = weekly_fee * WEEKS_PER_MONTH
    coaching_hours_cost = coaching_hours * PRIVATE_TUITION
    competitions_cost = competitions * COMPETITION_FEE
    total_cost = training_cost + coaching_hours_cost + competitions_cost

    athlete = {
        'name': name,
        'age': age,
        'weight': weight,
        'weight category': weight_category,
        'training plan': training_plan,
        'coaching hours': coaching_hours,
        'competitions': competitions,
        'weekly fee': weekly_fee,
        'training cost': training_cost,
        'coaching cost': coaching_hours_cost,
        'competition cost': competitions_cost,
        'total cost': total_cost
    }

    athletes[name] = athlete
    print("Successfully added - ", athlete["name"])


def show_athlete():
    print("Search for an Athlete in the main system")
    name = input("What is the name of this Athlete: ")

    if name not in athletes:
        print("Athlete not found, try again")
        return

    found_athlete = athletes[name]

    print("Athlete Information")
    print("Name: ", found_athlete['name'])
    print("Age: ", found_athlete['age'])
    print("Weight: ", found_athlete['weight'], "kg")
    print("Weight Category: ", found_athlete['weight category'])
    print("Training Plan: ", found_athlete['training plan'])
    print("Coaching Hours: ", found_athlete['coaching hours'])
    print("Competitions Entered This Month: ", found_athlete['competitions'])

    weight_limit = 0
    if found_athlete['weight category'] == "Flyweight":
        weight_limit = 66
    elif found_athlete['weight category'] == "Lightweight":
        weight_limit = 73
    elif found_athlete['weight category'] == "Light Middleweight":
        weight_limit = 81
    elif found_athlete['weight category'] == "Middleweight":
        weight_limit = 90
    elif found_athlete['weight category'] == "Light-Heavyweight":
        weight_limit = 100
    else:
        weight_limit = 999

    if found_athlete['weight'] <= weight_limit or found_athlete['weight category'] == "Heavyweight":
        print("Weight Status: Within competition weight category")
    else:
        print("Weight Status: OVER competition weight category limit!")

    print("Monthly Costs:")
    print("Training Cost: £", (found_athlete['training cost']))
    print("Coaching Cost: £", (found_athlete['coaching cost']))
    print("Competition Cost: £", (found_athlete['competition cost']))
    print("Total Monthly Cost: £", (found_athlete['total cost']))
    print("====== END =======")


def show_all_athletes():
    print("North Sussex Judo Program Current Members: ", str(len(athletes)))

    if len(athletes) == 0:
        print("Please Add the Athletes first!")
    else:
        for name in athletes:
            print(name)


def home_menu():
    global application_running
    while application_running:
        print("1. Add Athlete")
        print("2. Show Athlete Details")
        print("3. Show all Athletes")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_athlete()
        elif choice == "2":
            show_athlete()
        elif choice == "3":
            show_all_athletes()
        elif choice == "4":
            print("Exiting program...")
            application_running = False
        else:
            print("Invalid choice")

#user interface
print(""""North Sussex Judo Program"""")
print(""""North Sussex Judo Program"""")
print(""""North Sussex Judo Program"""")
print(""""Logged in as Admin!"""")
print(""""Pick an option from below:"""")
home_menu() # call the main menu function



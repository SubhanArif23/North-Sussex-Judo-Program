# Solihull College and University Centre
# North Sussex Judo Program
# Name - Muhammad Subhan Arif
# ID Number- ARI222004436
# Unit 1 programming (HND Cybersecurity)

TRAINING_PLANS = {
    "Beginner": 25.00,
    "Intermediate": 30.00,
    "Elite": 35.00
}

PRIVATE_TUITION = 9.50
COMPETITION_FEE = 22.00
WEEKS_PER_MONTH = 4

WEIGHT_CATEGORIES = {
    "Flyweight": 66,
    "Lightweight": 73,
    "Light Middleweight": 81,
    "Middleweight": 90,
    "Light-Heavyweight": 100,
    "Heavyweight": 999
}

athletes = {}
application_running = True

def save_to_file():
    try:
        filename = "judo_data.txt"
        file = open(filename, "w")
        for name in athletes:
            a = athletes[name]
            file.write("---NEW ATHLETE---\n")
            file.write("name:" + a['name'] + "\n")
            file.write("age:" + a['age'] + "\n")
            file.write("weight:" + str(a['weight']) + "\n")
            file.write("weight category:" + a['weight category'] + "\n")
            file.write("training plan:" + a['training plan'] + "\n")
            file.write("coaching hours:" + str(a['coaching hours']) + "\n")
            file.write("competitions:" + str(a['competitions']) + "\n")
            file.write("weekly fee:" + str(a['weekly fee']) + "\n")
            file.write("training cost:" + str(a['training cost']) + "\n")
            file.write("coaching cost:" + str(a['coaching cost']) + "\n")
            file.write("competition cost:" + str(a['competition cost']) + "\n")
            file.write("total cost:" + str(a['total cost']) + "\n")
        file.close()
        print("Data saved successfully to judo_data.txt")
    except:
        print("Error: Could not save to file.")

def load_from_file():
    try:
        filename = "judo_data.txt"
        file = open(filename, "r")
        lines = file.readlines()
        file.close()
        temp_athlete = {}
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if line == "---NEW ATHLETE---":
                if len(temp_athlete) > 0:
                    name = temp_athlete['name']
                    athletes[name] = temp_athlete
                    temp_athlete = {}
            elif ":" in line:
                parts = line.split(":")
                key = parts[0]
                value = parts[1]
                if key == "name":
                    temp_athlete['name'] = value
                elif key == "age":
                    temp_athlete['age'] = value
                elif key == "weight":
                    temp_athlete['weight'] = int(value)
                elif key == "weight category":
                    temp_athlete['weight category'] = value
                elif key == "training plan":
                    temp_athlete['training plan'] = value
                elif key == "coaching hours":
                    temp_athlete['coaching hours'] = int(value)
                elif key == "competitions":
                    temp_athlete['competitions'] = int(value)
                elif key == "weekly fee":
                    temp_athlete['weekly fee'] = float(value)
                elif key == "training cost":
                    temp_athlete['training cost'] = float(value)
                elif key == "coaching cost":
                    temp_athlete['coaching cost'] = float(value)
                elif key == "competition cost":
                    temp_athlete['competition cost'] = float(value)
                elif key == "total cost":
                    temp_athlete['total cost'] = float(value)
            i = i + 1
        if len(temp_athlete) > 0:
            name = temp_athlete['name']
            athletes[name] = temp_athlete
        print("Data loaded successfully from judo_data.txt")
        print("Loaded " + str(len(athletes)) + " athletes.")
    except FileNotFoundError:
        print("No existing data file found. Starting with empty system.")
    except:
        print("Error: Could not load from file. File may be corrupted.")

def show_help():
    print("")
    print("HELP SYSTEM - NORTH SUSSEX JUDO PROGRAM")
    print("")
    print("MAIN MENU OPTIONS:")
    print("1. Add New Athlete")
    print("   Enter all details for a new judo athlete.")
    print("   You will be prompted for name, age, weight,")
    print("   training plan, coaching hours, and competitions.")
    print("")
    print("2. View Athlete Details")
    print("   Search for and display complete information")
    print("   for a specific athlete including all costs")
    print("   and weight category status.")
    print("")
    print("3. View All Athletes")
    print("   Display a list of all registered athletes.")
    print("   Also shows summary statistics and total revenue.")
    print("")
    print("4. Update Athlete")
    print("   Modify coaching hours and/or competition count")
    print("   for an existing athlete. Costs recalculated automatically.")
    print("")
    print("5. Delete Athlete")
    print("   Remove an athlete from the system.")
    print("   You will be asked to confirm before deletion.")
    print("")
    print("6. Advanced Search")
    print("   Search athletes using multiple filters:")
    print("   Training plan type")
    print("   Weight category")
    print("   Minimum/maximum monthly cost")
    print("")
    print("7. Bulk Update")
    print("   Update multiple athletes at once:")
    print("   Increase all training fees by percentage")
    print("   Reset coaching hours for all athletes")
    print("")
    print("8. Save Data")
    print("   Save all athlete data to a file (judo_data.txt)")
    print("")
    print("9. Load Data")
    print("   Load athlete data from a previously saved file")
    print("")
    print("10. Help")
    print("    Display this help screen")
    print("")
    print("11. Exit Program")
    print("    Save data and exit the application")
    print("")
    print("TRAINING PLANS:")
    print("Beginner    : £25.00/week (2 sessions)")
    print("Intermediate: £30.00/week (3 sessions)")
    print("Elite       : £35.00/week (5 sessions)")
    print("")
    print("ADDITIONAL FEES:")
    print("Private Coaching: £9.50 per hour")
    print("Competition Entry: £22.00 each")
    print("")
    print("WEIGHT CATEGORIES:")
    print("Flyweight        : up to 66kg")
    print("Lightweight      : up to 73kg")
    print("Light Middleweight: up to 81kg")
    print("Middleweight     : up to 90kg")
    print("Light-Heavyweight: up to 100kg")
    print("Heavyweight      : unlimited")
    print("")
    print("RULES:")
    print("Only Intermediate and Elite can enter competitions")
    print("Maximum 5 coaching hours per week (20 per month)")
    print("Month is calculated as 4 weeks")

def advanced_search():
    print("")
    print("ADVANCED SEARCH")
    print("")
    if len(athletes) == 0:
        print("No athletes in the system to search.")
        return
    print("Search Filters:")
    print("1. Search by training plan")
    print("2. Search by weight category")
    print("3. Search by monthly cost range")
    print("4. Search by multiple criteria")
    print("5. Cancel")
    choice = get_valid_number("Choose search type (1-5): ", 1, 5)
    if choice == 5:
        return
    results = []
    if choice == 1:
        print("")
        print("Select training plan:")
        print("1. Beginner")
        print("2. Intermediate")
        print("3. Elite")
        plan_choice = get_valid_number("Choose plan (1-3): ", 1, 3)
        plans = ["Beginner", "Intermediate", "Elite"]
        selected_plan = plans[plan_choice - 1]
        for name in athletes:
            if athletes[name]['training plan'] == selected_plan:
                results.append(name)
        print("")
        print("Found " + str(len(results)) + " " + selected_plan + " athletes:")
    elif choice == 2:
        print("")
        print("Select weight category:")
        cat_list = list(WEIGHT_CATEGORIES.keys())
        i = 0
        while i < len(cat_list):
            print(str(i+1) + ". " + cat_list[i])
            i = i + 1
        cat_choice = get_valid_number("Choose category (1-6): ", 1, 6)
        selected_cat = cat_list[cat_choice - 1]
        for name in athletes:
            if athletes[name]['weight category'] == selected_cat:
                results.append(name)
        print("")
        print("Found " + str(len(results)) + " " + selected_cat + " athletes:")
    elif choice == 3:
        min_cost = get_valid_number("Enter minimum monthly cost (£): ", 0, 1000)
        max_cost = get_valid_number("Enter maximum monthly cost (£): ", min_cost, 1000)
        for name in athletes:
            cost = athletes[name]['total cost']
            if cost >= min_cost and cost <= max_cost:
                results.append(name)
        print("")
        print("Found " + str(len(results)) + " athletes with cost between £" + str(min_cost) + " and £" + str(max_cost) + ":")
    elif choice == 4:
        print("")
        print("Multiple Criteria Search")
        print("Leave filter blank (press enter) to skip any criterion.")
        plan_filter = input("Training plan (Beginner/Intermediate/Elite or blank): ")
        cat_filter = input("Weight category (or blank): ")
        min_filter = input("Minimum monthly cost (or blank): ")
        max_filter = input("Maximum monthly cost (or blank): ")
        for name in athletes:
            a = athletes[name]
            match = True
            if plan_filter != "" and a['training plan'].lower() != plan_filter.lower():
                match = False
            if cat_filter != "" and a['weight category'].lower() != cat_filter.lower():
                match = False
            if min_filter != "":
                try:
                    min_val = int(min_filter)
                    if a['total cost'] < min_val:
                        match = False
                except:
                    pass
            if max_filter != "":
                try:
                    max_val = int(max_filter)
                    if a['total cost'] > max_val:
                        match = False
                except:
                    pass
            if match:
                results.append(name)
    if len(results) == 0:
        print("No athletes match your search criteria.")
        return
    i = 0
    while i < len(results):
        name = results[i]
        a = athletes[name]
        print("")
        print(str(i+1) + ". " + name)
        print("   Plan: " + a['training plan'] + " | Category: " + a['weight category'])
        print("   Monthly Cost: £" + str(a['total cost']))
        i = i + 1
    print("")
    print("Total results: " + str(len(results)))

def bulk_update():
    print("")
    print("BULK UPDATE OPERATIONS")
    print("")
    if len(athletes) == 0:
        print("No athletes to update.")
        return
    print("Select bulk operation:")
    print("1. Increase all training fees by percentage")
    print("2. Reset coaching hours to zero for all athletes")
    print("3. Apply competition limit to all athletes")
    print("4. Cancel")
    choice = get_valid_number("Choose operation (1-4): ", 1, 4)
    if choice == 4:
        return
    if choice == 1:
        print("")
        print("WARNING: This will increase training fees for ALL athletes.")
        percent = get_valid_number("Enter percentage increase (e.g., 10 for 10%): ", 1, 100)
        multiplier = 1 + (percent / 100)
        confirm = input("Type 'CONFIRM' to proceed: ")
        if confirm != "CONFIRM":
            print("Bulk update cancelled.")
            return
        count = 0
        for name in athletes:
            a = athletes[name]
            old_fee = a['weekly fee']
            new_fee = old_fee * multiplier
            a['weekly fee'] = new_fee
            a['training cost'] = new_fee * WEEKS_PER_MONTH
            a['total cost'] = a['training cost'] + a['coaching cost'] + a['competition cost']
            count = count + 1
        print("Updated " + str(count) + " athletes with " + str(percent) + "% fee increase.")
    elif choice == 2:
        print("")
        print("WARNING: This will set coaching hours to ZERO for ALL athletes.")
        confirm = input("Type 'CONFIRM' to proceed: ")
        if confirm != "CONFIRM":
            print("Bulk update cancelled.")
            return
        count = 0
        for name in athletes:
            a = athletes[name]
            a['coaching hours'] = 0
            a['coaching cost'] = 0
            a['total cost'] = a['training cost'] + a['competition cost']
            count = count + 1
        print("Reset coaching hours for " + str(count) + " athletes.")
    elif choice == 3:
        print("")
        print("This will ensure all athletes follow competition rules:")
        print("- Beginners will have competitions set to 0")
        print("- Intermediate/Elite competitions will be capped at 4")
        confirm = input("Type 'CONFIRM' to proceed: ")
        if confirm != "CONFIRM":
            print("Bulk update cancelled.")
            return
        count = 0
        for name in athletes:
            a = athletes[name]
            changed = False
            if a['training plan'] == "Beginner" and a['competitions'] > 0:
                a['competitions'] = 0
                a['competition cost'] = 0
                changed = True
            if a['competitions'] > 4:
                a['competitions'] = 4
                a['competition cost'] = 4 * COMPETITION_FEE
                changed = True
            if changed:
                a['total cost'] = a['training cost'] + a['coaching cost'] + a['competition cost']
                count = count + 1
        print("Corrected competition entries for " + str(count) + " athletes.")

def get_valid_number(prompt, min_val, max_val):
    while True:
        try:
            value = int(input(prompt))
            if value < min_val or value > max_val:
                print("Error: Please enter a number between " + str(min_val) + " and " + str(max_val))
                continue
            return value
        except ValueError:
            print("Error: Please enter a valid number!")

def add_athlete():
    print("")
    print("ADD NEW ATHLETE")
    print("")
    name = input("Input Athlete Name: ")
    if name in athletes:
        print("Error: An athlete with this name already exists!")
        print("Please use a different name or select option 2 to view existing athlete.")
        return
    age = input("Input Athlete Age: ")
    weight = get_valid_number("Input Athlete Weight (kg): ", 20, 200)
    print("")
    print("Available Weight Categories:")
    category_list = list(WEIGHT_CATEGORIES.keys())
    i = 0
    while i < len(category_list):
        cat = category_list[i]
        limit = WEIGHT_CATEGORIES[cat]
        if limit == 999:
            print(str(i+1) + ". " + cat + " (Unlimited)")
        else:
            print(str(i+1) + ". " + cat + " (up to " + str(limit) + "kg)")
        i = i + 1
    cat_choice = get_valid_number("Select weight category (1-6): ", 1, 6)
    weight_category = category_list[cat_choice - 1]
    suggested_category = "Heavyweight"
    for cat, limit in WEIGHT_CATEGORIES.items():
        if weight <= limit:
            suggested_category = cat
            break
    if weight_category != suggested_category and weight_category != "Heavyweight":
        print("Note: Based on weight " + str(weight) + "kg, suggested category is " + suggested_category)
        confirm = input("Continue with selected category? (yes/no): ").lower()
        if confirm != "yes":
            print("Please re-enter athlete with correct category.")
            return
    print("")
    print("Select Training Plan:")
    plan_list = ["Beginner", "Intermediate", "Elite"]
    i = 0
    while i < len(plan_list):
        plan = plan_list[i]
        print(str(i+1) + ". " + plan + " (£" + str(TRAINING_PLANS[plan]) + "/week)")
        i = i + 1
    plan_choice = get_valid_number("Enter choice (1-3): ", 1, 3)
    training_plan = plan_list[plan_choice - 1]
    weekly_fee = TRAINING_PLANS[training_plan]
    coaching_hours = get_valid_number("Enter coaching hours this month (0-20): ", 0, 20)
    competitions = 0
    if training_plan in ["Intermediate", "Elite"]:
        competitions = get_valid_number("Enter competitions this month (0-4): ", 0, 4)
    else:
        print("Note: Beginner athletes cannot enter competitions. Competitions set to 0.")
    training_cost = weekly_fee * WEEKS_PER_MONTH
    coaching_cost = coaching_hours * PRIVATE_TUITION
    competition_cost = competitions * COMPETITION_FEE
    total_cost = training_cost + coaching_cost + competition_cost
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
        'coaching cost': coaching_cost,
        'competition cost': competition_cost,
        'total cost': total_cost,
        'registration date': 'Current Session'
    }
    athletes[name] = athlete
    print("")
    print("Successfully added " + name + " to the system!")
    print("Total monthly cost: £" + str(total_cost))

def show_athlete():
    print("")
    print("SEARCH ATHLETE")
    print("")
    if len(athletes) == 0:
        print("No athletes in the system yet. Please add athletes first.")
        return
    print("")
    print("Registered athletes:")
    name_list = list(athletes.keys())
    i = 0
    while i < len(name_list):
        print(str(i+1) + ". " + name_list[i])
        i = i + 1
    print(str(len(name_list)+1) + ". Search by name")
    choice = get_valid_number("Select athlete or search option: ", 1, len(name_list)+1)
    if choice == len(name_list) + 1:
        search_name = input("Enter athlete name to search: ")
        found = []
        i = 0
        while i < len(name_list):
            name = name_list[i]
            if search_name.lower() in name.lower():
                found.append(name)
            i = i + 1
        if len(found) == 0:
            print("No athletes found with that name.")
            return
        elif len(found) == 1:
            name = found[0]
        else:
            print("Multiple athletes found:")
            i = 0
            while i < len(found):
                print(str(i+1) + ". " + found[i])
                i = i + 1
            sub_choice = get_valid_number("Select athlete: ", 1, len(found))
            name = found[sub_choice - 1]
    else:
        name = name_list[choice - 1]
    a = athletes[name]
    print("")
    print("ATHLETE INFORMATION")
    print("")
    print("Name: " + a['name'])
    print("Age: " + a['age'])
    print("Weight: " + str(a['weight']) + " kg")
    print("Weight Category: " + a['weight category'])
    print("Training Plan: " + a['training plan'] + " (£" + str(a['weekly fee']) + "/week)")
    print("Coaching Hours: " + str(a['coaching hours']))
    print("Competitions: " + str(a['competitions']))
    limit = WEIGHT_CATEGORIES[a['weight category']]
    if a['weight'] <= limit or a['weight category'] == "Heavyweight":
        print("Weight Status: Within category limit")
        if a['weight category'] != "Heavyweight":
            diff = limit - a['weight']
            print("  (" + str(diff) + "kg under limit)")
    else:
        diff = a['weight'] - limit
        print("Weight Status: OVER category limit!")
        print("  (" + str(diff) + "kg over limit)")
    print("")
    print("MONTHLY COSTS")
    print("")
    print("Training (" + a['training plan'] + "): £" + str(a['training cost']))
    print("Private Coaching: £" + str(a['coaching cost']))
    print("Competitions: £" + str(a['competition cost']))
    print("")
    print("TOTAL: £" + str(a['total cost']))

def show_all_athletes():
    print("")
    print("ALL REGISTERED ATHLETES")
    print("")
    if len(athletes) == 0:
        print("No athletes registered yet.")
        return
    print("Total members: " + str(len(athletes)))
    print("")
    total_revenue = 0
    beginner_count = 0
    intermediate_count = 0
    elite_count = 0
    name_list = list(athletes.keys())
    i = 0
    while i < len(name_list):
        name = name_list[i]
        a = athletes[name]
        print(str(i+1) + ". " + name)
        print("   Plan: " + a['training plan'] + " | Weight: " + str(a['weight']) + "kg (" + a['weight category'] + ")")
        print("   Monthly Cost: £" + str(a['total cost']))
        total_revenue = total_revenue + a['total cost']
        if a['training plan'] == "Beginner":
            beginner_count = beginner_count + 1
        elif a['training plan'] == "Intermediate":
            intermediate_count = intermediate_count + 1
        else:
            elite_count = elite_count + 1
        i = i + 1
    print("")
    print("SUMMARY STATISTICS")
    print("Total monthly revenue: £" + str(total_revenue))
    print("Plan breakdown: Beginner:" + str(beginner_count) + " Intermediate:" + str(intermediate_count) + " Elite:" + str(elite_count))

def update_athlete():
    print("")
    print("UPDATE ATHLETE")
    print("")
    if len(athletes) == 0:
        print("No athletes to update.")
        return
    name_list = list(athletes.keys())
    i = 0
    while i < len(name_list):
        print(str(i+1) + ". " + name_list[i])
        i = i + 1
    choice = get_valid_number("Select athlete to update: ", 1, len(name_list))
    name = name_list[choice - 1]
    a = athletes[name]
    print("")
    print("Updating: " + name)
    print("1. Update coaching hours")
    print("2. Update competitions entered")
    print("3. Update both")
    print("4. Cancel")
    choice = get_valid_number("Choose option: ", 1, 4)
    if choice == 4:
        print("Update cancelled.")
        return
    if choice == 1 or choice == 3:
        new_hours = get_valid_number("Enter new coaching hours (0-20): ", 0, 20)
        a['coaching hours'] = new_hours
        a['coaching cost'] = new_hours * PRIVATE_TUITION
    if choice == 2 or choice == 3:
        if a['training plan'] in ["Intermediate", "Elite"]:
            new_comps = get_valid_number("Enter new competitions (0-4): ", 0, 4)
            a['competitions'] = new_comps
            a['competition cost'] = new_comps * COMPETITION_FEE
        else:
            print("Beginner athletes cannot enter competitions. Competitions remain 0.")
            a['competitions'] = 0
            a['competition cost'] = 0
    a['total cost'] = a['training cost'] + a['coaching cost'] + a['competition cost']
    print("Athlete " + name + " updated successfully!")
    print("New monthly total: £" + str(a['total cost']))

def delete_athlete():
    print("")
    print("DELETE ATHLETE")
    print("")
    if len(athletes) == 0:
        print("No athletes to delete.")
        return
    name_list = list(athletes.keys())
    i = 0
    while i < len(name_list):
        print(str(i+1) + ". " + name_list[i])
        i = i + 1
    choice = get_valid_number("Select athlete to delete: ", 1, len(name_list))
    name = name_list[choice - 1]
    print("")
    print("Are you sure you want to delete " + name + "?")
    print("This action cannot be undone.")
    confirm = input("Type 'yes' to confirm: ").lower()
    if confirm == 'yes':
        del athletes[name]
        print(name + " has been removed from the system.")
    else:
        print("Deletion cancelled.")

def home_menu():
    global application_running
    while application_running:
        print("")
        print("NORTH SUSSEX JUDO PROGRAM")
        print("")
        print("1. Add New Athlete")
        print("2. View Athlete Details")
        print("3. View All Athletes")
        print("4. Update Athlete")
        print("5. Delete Athlete")
        print("6. Advanced Search")
        print("7. Bulk Update Operations")
        print("8. Save Data to File")
        print("9. Load Data from File")
        print("10. Help")
        print("11. Exit Program")
        print("")

        choice = input("Choose option (1-11): ")

        if choice == "1":
            add_athlete()
        elif choice == "2":
            show_athlete()
        elif choice == "3":
            show_all_athletes()
        elif choice == "4":
            update_athlete()
        elif choice == "5":
            delete_athlete()
        elif choice == "6":
            advanced_search()
        elif choice == "7":
            bulk_update()
        elif choice == "8":
            save_to_file()
        elif choice == "9":
            load_from_file()
        elif choice == "10":
            show_help()
        elif choice == "11":
            print("")
            save_confirm = input("Save data before exiting? (yes/no): ").lower()
            if save_confirm == "yes":
                save_to_file()
            print("")
            print("Thank you for using North Sussex Judo Program!")
            print("Exiting...")
            application_running = False
        else:
            print("Invalid choice. Please enter a number between 1 and 11.")

print("")
print("WELCOME TO NORTH SUSSEX JUDO")
print("Training Fee Management System")
print("")
print("Logged in as: Admin")
print("Type '10' at any time for help")
print("")

load_from_file()

home_menu()

print("")
print("Program terminated. Goodbye!")
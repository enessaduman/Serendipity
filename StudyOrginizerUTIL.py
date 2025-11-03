def user_cleaner():
    with open("current_user.txt","w") as f:
        f.write("noUser")
def pull_user():
    with open("current_user.txt","r") as f:
        username=f.read().strip()
    return username
def user_checker():
    username=""
    with open("current_user.txt","r") as f:
        username=f.read().strip()
    if username == "noUser":
        print("You are not logged in! Please either log in or sign up")
        raise SystemExit
def plan_file_reader(temp_study_plan, temp_user, users_and_plans):
    try:
        with open("plans.txt", "r") as file:
            for line in file:
                # Split user_id and their plan string
                parts = line.strip().split("-", 1)
                if len(parts) != 2:
                    user_id, plan_str = parts[0], ""
                else:
                    user_id, plan_str = parts
                users_and_plans[user_id] = plan_str
                # If this is the current user, parse their plan into dictionary
                if user_id == temp_user and plan_str:
                    for element in plan_str.split(","):
                        if ":" in element:
                            course, time = element.split(":", 1)
                            temp_study_plan[course.strip()] = time.strip()
                        else:
                            temp_study_plan[element.strip()] = ""
    except FileNotFoundError:
        # If plans.txt does not exist, create empty dictionaries
        users_and_plans.clear()
        temp_study_plan.clear()

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
def plan_file_reader(temp_study_plan,temp_user,users_and_plans):
    with open("plans.txt", "r") as file:
        for line in file:
            lst1 = line.strip().split("-")
            users_and_plans[lst1[0]]=lst1[1]
            if str(lst1[0]) == str(temp_user):
                lst2 = lst1[1].split(",")
                for element in lst2:
                    if ":" in element:
                        lst3 = element.split(":")
                        temp_study_plan[lst3[0]] = lst3[1]
                    else:
                        temp_study_plan[lst3[0]]=" "
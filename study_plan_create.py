import argparse
from StudyOrginizerUTIL import pull_user,user_checker,plan_file_reader
parser = argparse.ArgumentParser(description="You can add study goals from here, each run adds 1 course!\n      Use UNDERSCORE instead of WHITESPACES!")
parser.add_argument("--course_name",required=True,help="Name of the lecture")
parser.add_argument("--time",required=True,help="Time goal for the course in hh/mm")
args = parser.parse_args()
user_checker()
temp_user=pull_user()
user_plan={}
users_and_plans={}
plan_str=""
course_name=str(args.course_name).replace("_"," ").lower()
time_list=str(args.time).split("/")
try:
    if len(time_list) != 2:
        print("You've entered either too many or a few time indicators! \nPlease check out the help menu to figure out the proper format for time!")
        raise SystemExit
    elif int(time_list[0])<0 or int(time_list[0])>24:
        print("You cannot study over 24 hours or under '0' hour! Please check your inputs!")
        raise SystemExit
    elif int(time_list[1])<0 or int(time_list[1])>59:
        print("Minutes should be represented between 0 and 59! Please check your inputs!")
        raise SystemExit
except ValueError:
    print("You didn't enter a valid time! Please check out the help menu to figure out the proper format for time!")
    raise SystemExit
plan_file_reader(user_plan,temp_user,users_and_plans)
user_plan[course_name] = f"{time_list[0]}/{time_list[1]}"
plan_str = ",".join([f"{key}:{v}" for key, v in user_plan.items()])
users_and_plans[temp_user] = plan_str
with open("plans.txt", "w") as file:
    for key, value in users_and_plans.items():
        file.write(f"{key}-{value}\n")
    print(f"You're plan has been updated with the addition of {course_name} with a time of {time_list[0]}/{time_list[1]}.")
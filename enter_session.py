import argparse
from StudyOrginizerUTIL import pull_user,user_checker,plan_file_reader
user_checker()
temp_user=pull_user()
temp_study_plan={}
plan_str=""
users_and_plans={}
plan_file_reader(temp_study_plan,temp_user,users_and_plans)
parser = argparse.ArgumentParser(description="You can enter study sessions so that your gols will be completed! Each run adds 1 course!\n      Use UNDERSCORE instead of WHITESPACES!")
parser.add_argument("--course_name",required=True,help="Name of the lecture",choices=[keys.replace(" ","_") for keys in temp_study_plan.keys()],type=str)
parser.add_argument("--time",required=True,help="Studied time for the course in hh/mm")
args=parser.parse_args()
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
if course_name in temp_study_plan.keys():
    completed_time=int(time_list[0])*60+int(time_list[1])
    goal_time_list=temp_study_plan[course_name].split("/")
    goal_time=int(goal_time_list[0])*60+int(goal_time_list[1])
    minutes=0
    hours=0
    if completed_time>goal_time:
        remaining=completed_time-goal_time
        minutes = remaining%60
        hours = remaining//60
        if hours==0:
            print(f"You've surpassed your goal! Congratulations! You've studied {minutes} minutes more than your goal!")
        elif hours==1:
            print(f"You've surpassed your goal! Congratulations! You've studied {hours} hour and {minutes} minutes more than your goal!")
        else:
            print(f"You've surpassed your goal! Congratulations! You've studied {hours} hours and {minutes} minutes more than your goal!")
        temp_study_plan[course_name]="0/0"
    elif completed_time==goal_time:
        print("You've totally completed your goal! Congratulations!")
        temp_study_plan[course_name]="0/0"
    else:
        remaining_time=goal_time-completed_time
        hours=remaining_time//60
        minutes=remaining_time%60
        if hours==0:
            print(f"Your study is saved! Now you have {minutes} minutes remaining to study in {course_name}!")
        elif hours==1:
            print(f"Your study is saved! Now you have {hours} hour and {minutes} minutes remaining to study in {course_name}!")
        else:
            print(f"Your study is saved! Now you have {hours} hours and {minutes} minutes remaining to study in {course_name}!")
        temp_study_plan[course_name]=f"{hours}/{minutes}"
    plan_str=",".join([f"{k}:{v}" for k, v in temp_study_plan.items()])
    with open("plans.txt","w") as file:
        for keys,values in users_and_plans.items():
            if str(temp_user)==str(keys):
                file.write(f"{keys}-{plan_str}\n")
            else:
                file.write(f"{keys}-{values}\n")

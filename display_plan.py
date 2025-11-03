import argparse
from StudyOrginizerUTIL import pull_user,user_checker,plan_file_reader
#user validation
user_checker()
temp_user=pull_user()
#data retrieve
users_and_plans={}
temp_study_plan={}
plan_file_reader(temp_study_plan,temp_user,users_and_plans)
parser=argparse.ArgumentParser(description="You can display your current plan here")
#list display
print(f"    ~~ Study PLan ~~")
if not temp_study_plan:
    print("You currently have any study plan!")
else:
    for i, (key, value) in enumerate(temp_study_plan.items(), start=1):
        if str(value) != "0/0":
            time_list = str(value).split("/")
            print(f"{i} -> COURSE: {str(key).title()}  -  TIME: {time_list[0]}h and {time_list[1]}m")
        else:
            print(f" {i} -> COURSE: {str(key).title()}  -  COMPLETED!")
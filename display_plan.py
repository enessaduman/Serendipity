import argparse
from StudyOrginizerUTIL import pull_user,user_checker,plan_file_reader
user_checker()
temp_user=pull_user()
users_and_plans={}
temp_study_plan={}
plan_file_reader(temp_study_plan,temp_user,users_and_plans)
parser=argparse.ArgumentParser(description="You can display your current plan here")
print(f"    ~~ Study PLan ~~")
for i,(key,value) in enumerate(temp_study_plan.items(),start=1):
    if str(value)!="0/0":
        time_list = str(value).split("/")
        print(f"{i} -> COURSE: {key}  -  TIME: {time_list[0]}h and {time_list[1]}m")
    else:
        print(f" {i} -> COURSE: {key}  -  COMPLETED!")
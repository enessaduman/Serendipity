import argparse
usernames_passwords={}
usernames_info={}
def data_loader():
    with open("student_login_info.txt","r") as file:
        for line in file:
            lst=line.strip("\n").split(":")
            usernames_passwords[lst[0]]=lst[1]
    with open("student_full_info.txt","r") as file:
        for line in file:
            lst=line.strip("\n").split("/")
            usernames_info[lst[0]]=lst[1]
parser = argparse.ArgumentParser()
parser.add_argument("--student_id",required=True,help="Student ID")
parser.add_argument("--password",required=True,help="Password")
args = parser.parse_args()
data_loader()
try:
    student_id=(int(args.student_id))
except ValueError:
    print("Student Id must be comprised of numbers")
    raise SystemExit
if str(student_id) not in usernames_passwords.keys():
    print(f"There is no student id such {student_id}")
    raise SystemExit
else:
    if usernames_passwords[str(student_id)] == args.password:
        with open("current_user.txt","w") as file:
            file.write(str(student_id))
        info_lst=usernames_info[str(student_id)].split(":")
        print(f"Login Successful! Welcome {info_lst[0]}")
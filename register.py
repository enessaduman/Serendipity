import argparse
#data retrieve
existed_students=[]
with open("student_login_info.txt","r") as f:
    for line in f:
        line_lst=line.split(":")
        existed_students.append(line_lst[0])
parser = argparse.ArgumentParser(description='User Registration\n!!! Please use UNDERSCORE (_) instead of SPACE between words !!!\nOtherwise you will not be able to enter multiple words for a field')
parser.add_argument("--student_id",required=True, help="Student ID")
parser.add_argument("--name_surname",required=True, help="Name and surname")
parser.add_argument("--collage",required=True, help="Collage Name")
parser.add_argument("--major",required=True, help="Major Name")
parser.add_argument("--password",required=True, help="Password")
args = parser.parse_args()
#arg parsing
student_id = args.student_id
name_lst=str(args.name_surname).split("_")
name_surname=" ".join(name_lst)
collage_lst=str(args.collage).split("_")
collage =" ".join(collage_lst)
major_name_lst=str(args.major).split("_")
major =" ".join(major_name_lst)
password = args.password
#checking inputs, enforce user to enter properly
try:
    student_id = int(student_id)
except ValueError:
    print("Student ID must be comprised of integers only!")
    raise SystemExit
if str(student_id) in existed_students:
    print("This student ID already exists! If you ensured that ID, please try to login!")
    raise SystemExit
with open("student_full_info.txt", "a") as student_file:
    student_file.write(f"{student_id}/{name_surname}:{collage}:{major}:{password}\n")
with open("current_user.txt","w") as file:
    file.write(f"{student_id}")
with open("student_login_info.txt","a") as file:
    file.write(f"{student_id}:{password}\n")
print(f"You're successfully registered {name_surname}!")
#Enes
#LOG FORMAT: student_no_password= studentNo-password
#LOG FORMAT: student_full_info: StudentNo/name-surname-collageName-Major-Grade-password / ile numarayı arama yapmak için ayırıyoruz


#Variables:
student_name=""
student_surname=""
collage_name=""
major_name=""
grade=0
student_no_password={}
temp_student_no=0
def login_menu():
    login_menu_list=["Press 1 to log in","Press 2 to sign up","Press 3 to exit"]
    for i,list_thing in enumerate(login_menu_list,start=1):
        print(f"{i} -> {list_thing}")
def data_updater():
   with open("student_login_info.txt","w") as file:
       for student_No in student_no_password.keys():
           file.write(f"{student_No}-{student_no_password[student_No]}\n")
def data_loader():
    with open ("student_login_info.txt", "r") as file:
        for line in file:
            line_lst=line.strip("\n").split("-")
            student_no_password[line_lst[0]]=line_lst[1]
data_loader()
while True:
    login_menu()
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Enter a valid choice")
        continue
    if choice == 1:
        while True:
            student_no = input("Enter your student number: ")
            if student_no in student_no_password.keys():
                while True:
                    password = input("Enter your password: ")
                    if password == student_no_password[student_no]:
                        temp_student = student_no
                        print(f"You've successfully logged in as {temp_student}.")
                        #ismi parcing ile çekip merhaba falan yazdırılabilir
                        break
                    else:
                        print("Wrong password")
                break
            else:
                print(f"There is no student number as {student_no}")
    elif choice == 2:
        print("     Welcome again to the Study Organizer    \n")
        print("Please fill up the blanks that are given below one-by-one: \n")
        student_name=str(input("Enter your name: "))
        student_surname=str(input("Enter your surname: "))
        collage_name=str(input("Enter your collage name: "))
        major_name=str(input("Enter your major: "))
        while True:
            grade = int(input("Enter your grade: "))
            if 6<grade<0:
                print("Your grade is out of range. Try again.")
            else:
                break
        while True:
            temp_student_no = int(input("Enter your student number: "))
            if temp_student_no in student_no_password:
                print("This student number is already taken. Please check your student no and try again.")
            else:
                break
        student_no_password[temp_student_no]=input("Enter your password: ")
        with open("student_full_info.txt","a",encoding="UTF-8") as file:
            file.write(f"{temp_student_no}/{student_name}-{student_surname}-{collage_name}-{major_name}-{grade}\n")
        data_updater()
        print("You've successfully signed up.")
    elif choice == 3:
        print("Thank you for using this program. Exiting...")
        break
    else:
        print("Input value is out of the menu range! Please enter a valid choice")

#Zeynep

#Aleyna


#Zehra

#Büşra

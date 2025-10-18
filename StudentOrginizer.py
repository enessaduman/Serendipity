#Enes
#LOG FORMAT: studentNo-password
#{11111111111:1111111,222222222:2222222}
student_no_password={}
temp_student=0
def data_loader():
    with open ("student_login_info.txt", "r") as file:
        for line in file:
            line_lst=line.strip("\n").split("-")
            student_no_password[line_lst[0]]=line_lst[1]
data_loader()
while True:
    student_no = input("Enter your student number: ")
    if student_no in student_no_password:
        while True:
            password = input("Enter your password: ")
            if password == student_no_password[student_no]:
                temp_student = student_no
                break
            else:
                print("Wrong password")
        break
    else:
        print(f"There is no student number as {student_no}")

#Zeynep

#Aleyna


#Zehra

#Büşra

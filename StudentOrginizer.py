#Enes
#LOG FORMAT: studentNo-password
#{11111111111:1111111,222222222:2222222}
student_no_password={}
temp_student=0
def data_loader():
    with open ("student_login_info.txt", "r") as file:
        for line in file:
            line_lst=line.strip("\n").split(",")
            student_no_password[line_lst[0]]=line_lst[1]
choice=0
while True:
    if choice==1:
        while True:
            student_no = int(input("Enter your student number: "))
            for student_nos, student_password in student_no_password:
                if student_nos == student_no:
                    while True:
                        password = input("Enter your password: ")
                        if password == student_password:
                            temp_student = student_nos
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

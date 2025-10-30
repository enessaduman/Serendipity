## 📚​ Study Orginizer <br>

📘 Overview<br>

Study Organizer is a command-line tool that helps users manage their study goals efficiently.
It allows users to define study plans, log their daily study sessions, and track their overall progress through simple terminal commands.

<h2>🧭How to Run</h2>

### 1️⃣ Register & Login

Before adding study goals or sessions, you need to register a user and log in.  
The following commands should be run in your terminal.

#### 🔹 Register a new user
```bash
$ py register.py --student_id STUDENT_ID --name_surname NAME_SURNAME --collage COLLAGE --major MAJOR --password PASSWORD  
```
#### 🔹 Login as an user
```bash
$ py login.py --student_id STUDENT_ID --password PASSWORD
```
### 2️⃣ Adding a Study Plan

After registering and logging in, you can create a new study plan for a specific course.  
Each plan requires a course name and a time goal (in hours and minutes).

#### 🔹 Create a new study plan
```bash
$ py study_plan_create.py --course_name COURSE_NAME --time TIME


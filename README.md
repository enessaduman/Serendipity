# 📚​ Study Organizer <br>

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
#### 🔹 Login as a user
```bash
$ py login.py --student_id STUDENT_ID --password PASSWORD
```
### 2️⃣ Adding a Study Plan

After registering and logging in, you can create a new study plan for a specific course.  
Each plan requires a course name and a time goal (in hours and minutes).

#### 🔹 Create a new study plan
```bash
$ py study_plan_create.py --course_name COURSE_NAME --time TIME
```
### 3️⃣ Displaying the Current Plan

Next up is monitoring the plan! You can your whole courses and their times in a single plan. 
It displays the courses one bye one in a list that matched with their goal times.

#### 🔹 Display the Plan
```bash
$ py display.py
```
### 4️⃣ Adding a Completed Study Session

After creating a study plan, you can log a completed study session for any course.  
Each session entry requires the course name and the time you studied.

#### 🔹 Add a completed study session
```bash
$ py enter_session.py --course_name COURSE_NAME --time TIME
```
### 5️⃣ Exiting...

Finally, when you're done with your operations, you have to exit.

#### 🔹 Finalize the program
```bash
$ py exit.py
```
## 📁 File Structure
```
StudyOrganizer/
├── register.py           # Register a new user
├── login.py              # Log in as an existing user
├── study_plan_create.py  # Create a new study plan
├── enter_session.py      # Add completed study sessions
├── StudyOrganizerUTIL.py # Utility functions
└── .txt files            # Stores user data and plans
```



def user_cleaner():
    with open("current_user.txt","w") as f:
        f.write("noUser")
def pull_user():
    with open("current_user.txt","r") as f:
        username=f.read().strip()
    return username
def user_checker():
    username=""
    with open("current_user.txt","r") as f:
        username=f.read().strip()
    if username == "noUser":
        print("You are not logged in! Please either log in or sign up")
        raise SystemExit
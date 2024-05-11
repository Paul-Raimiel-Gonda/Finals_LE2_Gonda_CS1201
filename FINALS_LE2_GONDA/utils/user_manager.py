from utils.user import User

class UserManager:
    def __init__(self):
        self.users = {}

#VALIDATE THE USERNAME AND PASSWORD THE USER HAS INPUT
    def register(self, user):
        if len(user.username) < 4:
            print("Username cannot be less than 4 characters")
            return
        if len(user.password) < 8:
            print("Password cannot be less than 8 characters")
            return
        user_list = user.load_users()
        if (user.username, user.password) in user_list:  #CHECK IF USER ALREADY EXISTS
            print("Username already exists")
            return
        print("User successfully registered")
        user.save_user()    #PROCEED TO SAVE USER at user.py
        self.users[user.username] = user

#CHECK EXISTING USER DATA 
    def login(self, user):
        user_list = user.load_users()   #PROCEED TO LOAD USER at user.py
        for username, password, _ in user_list:
            if username == user.username and password == user.password:
                print("Login successful")
                return user   #RETURN TO MAIN MENU TO PROCEED TO THE GAME MENU
        print("Invalid username or password")
        return None
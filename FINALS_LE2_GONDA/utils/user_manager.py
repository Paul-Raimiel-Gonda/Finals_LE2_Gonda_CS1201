from utils.user import User

class UserManager:
    def __init__(self):
        self.users = {}

    def register(self, user):
        if len(user.username) < 4:
            print("Username cannot be less than 4 characters")
            return
        if len(user.password) < 8:
            print("Password cannot be less than 8 characters")
            return
        user_list = user.load_users()
        if (user.username, user.password) in user_list:
            print("Username already exists")
            return
        user.save_user()
        self.users[user.username] = user

    def login(self, user):
        user_list = user.load_users()
        for username, password, _ in user_list:
            if username == user.username and password == user.password:
                print("Login successful")
                return user
        print("Invalid username or password")
        return None
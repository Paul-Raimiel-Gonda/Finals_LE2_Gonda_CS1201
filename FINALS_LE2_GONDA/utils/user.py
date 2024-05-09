import os

class User:
    def __init__(self, username, password, score):
        self.username = username
        self.password = password
        self.score = score

    def load_users(self):
        user_file_path = os.path.join('data', 'user_database.txt')
        users = []
        if os.path.exists(user_file_path):
            with open(user_file_path, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    parts = line.strip().split(',')
                    username = parts[0]
                    password = parts[1]
                    score = int(parts[2])
                    users.append((username, password, score))
        return users

    def save_user(self):
        user_folder = 'data'
        user_file_path = os.path.join(user_folder, 'user_database.txt')

        if not os.path.exists(user_folder):
            os.makedirs(user_folder)

        with open(user_file_path, 'a+') as file:
            file.write(f"{self.username},{self.password},{self.score}\n")
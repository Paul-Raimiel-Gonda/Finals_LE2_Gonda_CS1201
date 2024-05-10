import os

class User:
    def __init__(self, username, password, score):
        self.username = username
        self.password = password
        self.score = score

#READ EXISTING USER DATA
    def load_users(self):
        user_file_path = os.path.join('data', 'user_database.txt')  #CHECK IF FILES EXIST
        users = []
        if os.path.exists(user_file_path):
            with open(user_file_path, 'r') as file: #READS THE FILE
                lines = file.readlines()
                for line in lines:
                    parts = line.strip().split(',')  #TO SEPARATE AND ARRANGE THE DATA
                    username = parts[0]
                    password = parts[1]
                    score = int(parts[2])
                    users.append((username, password, score))
        return users #returns the list of users containing tuples of (username, password, score).

#SAVE AND CREATE USER DATA
    def save_user(self):
        user_folder = 'data'    
        user_file_path = os.path.join(user_folder, 'user_database.txt')  #DEFINE THE FILE PATH 

        if not os.path.exists(user_folder):
            os.makedirs(user_folder)  #CREATE DATA FOLDER AND USER DATABASE TXT FILE IF IT DOESN'T ALREADY EXIST

        with open(user_file_path, 'a+') as file:
            file.write(f"{self.username},{self.password},{self.score}\n") #SAVE THE USERNAME, PASSWORD AND INITIAL SCORE (0) OF THE USER
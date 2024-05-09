from utils.user_manager import UserManager
from utils.user import User
from utils.dice_game import DiceGame

class Main:
    def __init__(self):
        self.user_manager = UserManager()
        self.dice_game = DiceGame()

    def main(self):
        while True:
            print("""
                Welcome to DICE GAME
                1. User Sign up
                2. User Log in
                3. Exit
            """)
            choice = input("Enter choice: ")
            if choice == '1':
                username = input("Enter Username: ")
                password = input("Enter your password: ")
                user = User(username, password, 0)
                self.user_manager.register(user)
                
            elif choice == '2':
                username = input("Input your username: ")
                password = input("Input your password: ")
                user = User(username, password, 0)
                logged_user = self.user_manager.login(user)
                if logged_user:
                    self.dice_game.game_menu(logged_user)
            elif choice == '3':
                exit()
            else:
                print("Invalid choice, try again")

if __name__ == "__main__":
    game = Main()
    game.main()
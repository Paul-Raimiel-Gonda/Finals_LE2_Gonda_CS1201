
from utils.user import User
from utils.score import Score
import random
import os
from datetime import datetime

class DiceGame:
    def __init__(self):
        self.current_user = None
        self.total_rounds = 3
        self.total_stages = 3
        self.scores = []

    def play_game(self, user):
        total_score = 0
        total_rounds_won = 0
        total_stages_won = 0

        for stage in range(self.total_stages):
            stage_score = 0
            stage_rounds_won = 0

            print(f"\nStage {stage + 1}\n")

            for _ in range(self.total_rounds):
                user_number = random.randint(1, 6)
                cpu_number = random.randint(1, 6)

                print(f"{user.username} rolled: {user_number}\nCPU rolled: {cpu_number}\n")

                while user_number == cpu_number:
                    print("It's a draw! Rolling again...\n")
                    user_number = random.randint(1, 6)
                    cpu_number = random.randint(1, 6)
                    print(f"{user.username} rolled: {user_number}\nCPU rolled: {cpu_number}\n")

                if user_number > cpu_number:
                    print(f"{user.username} Won the round!\n")
                    stage_score += 1
                    stage_rounds_won += 1
                else:
                    print(f"{user.username} Lost the round!\n")

            total_score += stage_score
            total_rounds_won += stage_rounds_won

            print(f"Stage {stage + 1} Score: {stage_score}")
            print(f"Total Score: {total_score}")

            if stage < self.total_stages - 1:
                if total_rounds_won == 0:
                    print("Game over. You didn't win any stages.")
                    break
                choice = input("Do you want to proceed to the next stage? (1 for yes, 0 for no): ")
                while choice not in ('1', '0'):
                    choice = input("Invalid choice. Do you want to proceed to the next stage? (1 for yes, 0 for no): ")

                if choice == '0':
                    break

            if total_rounds_won == self.total_rounds:
                total_stages_won += 1
                total_score += 3
                print("Congratulations! You gained an additional 3 points for winning the stage.")

        if total_stages_won == 0:
            print("Game over. You didn't win any stages.")
        else:
            print(f"\nTotal Points Earned: {total_score}")
            print(f"Number of Rounds Won: {total_rounds_won}")

        score_manager = Score()
        score_manager.save_scores(user.username, total_score, total_rounds_won, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def show_top_scores(self):
        score_manager = Score()
        scores = score_manager.load_scores()
        if scores:
            scores.sort(key=lambda x: int(x[1]), reverse=True)  
            os.system('cls')
            print("\nTop 10 Scores:")
            for i, (username, score, rounds_won, date) in enumerate(scores[:10], 1):
                print(f"{i}. {username}: {score}, Rounds Won: {rounds_won}, Date: {date}")
        else:
            print("No scores recorded yet.")

    def show_user_scores(self, user):
        score_manager = Score()
        scores = score_manager.load_scores()
        if scores:
            user_scores = [score for score in scores if score[0] == user.username]
            if user_scores:
                os.system('cls')
                print(f"\n{user.username}'s Scores:")
                for i, (_, score, rounds_won, date) in enumerate(user_scores, 1):
                    print(f"{i}. Score: {score}, Rounds Won: {rounds_won}, Date: {date}")
            else:
                print("No scores recorded for this user.")
        else:
            print("No scores recorded yet.")

    def logout(self):
        from main import Main
        main = Main()
        main.main()

    def game_menu(self, user):
        while True:
            print("\nWELCOME TO DICE GAME\n")
            print("1. Play Game")
            print("2. Show Top Scores")
            print("3. Show Your Scores")
            print("4. Logout")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.play_game(user)
            elif choice == '2':
                self.show_top_scores()
            elif choice == '3':
                self.show_user_scores(user)
            elif choice == '4':
                self.logout()
                break
            else:
                print("Invalid choice")

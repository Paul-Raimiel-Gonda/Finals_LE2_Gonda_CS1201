
from utils.user import User
from utils.score import Score
import random
import os
from datetime import datetime

#MAIN GAME MENU
class DiceGame:
    def __init__(self):
        self.current_user = None
        self.total_rounds = 3
        self.total_stages = 3
        self.scores = []

#FUNCTION TO START GAME
    def play_game(self, user):
        total_score = 0
        total_rounds_won = 0
        current_stage = 1 
        
        

        while True:  
            stage_score = 0
            stage_rounds_won = 0
            os.system('cls')
            print(f"\nStage {current_stage} ✧\n")

            for _ in range(self.total_rounds):  #generate a random integer 1-6 for both the user and cpu
                user_number = random.randint(1, 6)
                cpu_number = random.randint(1, 6)

                print(f"{user.username} rolled: {user_number}\nCPU rolled: {cpu_number}\n")

                while user_number == cpu_number:
                    print("It's a draw! Rolling again...\n") #If the round ends in a draw, roll again until either the user or cpu wins
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
            total_rounds_won += stage_rounds_won  #add the points

            print(f"Stage Score: {stage_score}")
            print(f"Total Score: {total_score}")

            if stage_rounds_won == 0:
                print("Game over. You didn't win any stages.")  #Lose the game if you didn't win a single round in a stage
                break

            if total_rounds_won == self.total_rounds:  
                total_score += 3  #Add additional 3 points if you've won all 3 rounds in a stage
                print("Congratulations! You won all rounds in this stage and gained 3 ✧ additional points!")
                print(f"Total Score: {total_score} ✧")

            choice = input("Do you want to proceed to the next stage? (1 for yes, 0 for no): ") #ask the user if they want to proceed to the next stage
            while choice not in ('1', '0'):
                choice = input("Invalid choice. Do you want to proceed to the next stage? (1 for yes, 0 for no): ")

            if choice == '0':
                break

            current_stage += 1 

        print(f"\nTotal Points Earned: {total_score} ✧")
        print(f"Number of Rounds Won: {total_rounds_won} ✧")

        score_manager = Score()  
        score_manager.save_scores(user.username, total_score, total_rounds_won, datetime.now().strftime("%Y-%m-%d %H:%M:%S")) #track the data


#SHOW TOP TEN SCORES 
    def show_top_scores(self):
        score_manager = Score()
        scores = score_manager.load_scores()  #PROCEED TO score.py
        if scores:
            scores.sort(key=lambda x: int(x[1]), reverse=True)  #SORT THE SCORES INTO HIGHEST TO LOWEST
            os.system('cls')
            print("\n✧ Top 10 Scores:")
            for i, (username, score, rounds_won, date) in enumerate(scores[:10], 1):             
                print(f"{i}. {username}: {score}, Rounds Won: {rounds_won}, Date: {date}")
        else:
            print("No scores recorded yet.")

#SHOW THE RECORD OF THE USER's SCORES
    def show_user_scores(self, user):
        score_manager = Score()
        scores = score_manager.load_scores()  #PROCEED TO score.py
        if scores:
            user_scores = [score for score in scores if score[0] == user.username]  #Filters the score, only takes the score of the current user
            if user_scores:
                os.system('cls')
                print(f"\n{user.username}'s Scores:")
                for i, (_, score, rounds_won, date) in enumerate(user_scores, 1):
                    print(f"{i}. Score: {score}, Rounds Won: {rounds_won}, Date: {date}")         #JUST SHOWS THE RECORD OF SCORES OF THE USER
            else:
                print("No scores recorded for this user.")
        else:
            print("No scores recorded yet.")

#GO BACK TO THE SIGN UP AND LOGIN MENU
    def logout(self):
        from main import Main
        main = Main()
        main.main()

#THE MENU FOR DICE GAME
    def game_menu(self, user):
        os.system('cls')
        CEND = '\33[0m'
        CMAGENTA = '\33[35m'
        CBOLD = '\33[1m'
        
        while True:
            os.system('cls')
            print(CMAGENTA + CBOLD + """
    ================================================================================
        _____                               _____                                 
     __|__   |__  ____  ______  ______   __|___  |__  ____    ____    __  ______  
    |     \     ||    ||   ___||   ___| |   ___|    ||    \  |    \  /  ||   ___| 
    |      \    ||    ||   |__ |   ___| |   |  |    ||     \ |     \/   ||   ___| 
    |______/  __||____||______||______| |______|  __||__|\__\|__/\__/|__||______| 
        |_____|                             |_____|                                
                                                                                    
    ================================================================================
    """ + CEND)
            print("\t\t\t1. Play Game")
            print("\t\t\t2. Show Top Scores ✧")
            print("\t\t\t3. Show Your Scores")
            print("\t\t\t4. Logout")

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
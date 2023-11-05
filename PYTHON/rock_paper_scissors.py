"""
For this project, you will individually create a program that has a "player" and a "computer" advisary. The computer should randomly choose it's decision based on a list of actions it can take ("Rock", "Paper" or "Scissors"). The player should then have a chance to input their decision. If player and computer choose the same decision then display ("Game Tied"), If the player chooses "Rock" and the computer chooses "Paper" display ("You lose"), if the player chooses "Scissors" and the computer chooses "Rock" display ("You Lose") and if the player chooses "Paper" and the computer chooses "Scissors" then display ("You lose") -- Vice versa for other descisions.

Continue to ask the player for their input until they say "I quit", at which time the game will then end and display ("Thank you for playing").

In this project, you will need to use the random.randint function to enable to computer to make a random decision. Full documentation on the use of this function is attached in a link to this assignment.

Once completed, commit your code to github and submit the link to this assignment.
"""

import random

class RockPaperScissors():
    
    def __init__(self):
        self.opponent_call = ""
        self.player_call = ""
        self.opponent_wins = 0
        self.player_wins = 0
        self.ties = 0
        pass
    
    def opponent_call_grab(self):
        r_int = random.randint(1,3)
        match r_int:
            case 1:
                self.opponent_call = "Rock"
                pass
            case 2:
                self.opponent_call = "Paper"
                pass
            case 3:
                self.opponent_call = "Scissors"
                pass
        pass
    
    def player_call_grab(self):
        call_selected = False
        player_input = ""
        while call_selected == False:
            player_input = input("Rock|R|r, Paper|P|p, or Scissors|S|s? ")
            match player_input:
                case "Rock" | "R" | "r":
                    self.player_call = "Rock"
                    call_selected = True
                    pass
                case "Paper" | "P" | "p":
                    self.player_call = "Paper"
                    call_selected = True
                    pass
                case "Scissors" | "S" | "s":
                    self.player_call = "Scissors"
                    call_selected = True
                    pass
                case _:
                    print("Unable to recognize input, please try again!")
                    pass
        pass

    def calculate_outcome(self):
        if self.player_call == self.opponent_call:
            print(f"Player's {self.player_call} and opponent's {self.opponent_call} clash! Its a tie!")
            self.ties += 1
        elif self.player_call == "Rock" and self.opponent_call == "Scissors":
            print(f"Player's {self.player_call} and opponent's {self.opponent_call} clash! Player wins!")
            self.player_wins += 1
        elif  self.player_call == "Rock" and self.opponent_call == "Paper":
            print(f"Player's {self.player_call} and opponent's {self.opponent_call} clash! Opponent wins!")
            self.opponent_wins += 1
        elif  self.player_call == "Paper" and self.opponent_call == "Rock":
            print(f"Player's {self.player_call} and opponent's {self.opponent_call} clash! Player wins!")
            self.player_wins += 1
        elif  self.player_call == "Paper" and self.opponent_call == "Scissors":
            print(f"Player's {self.player_call} and opponent's {self.opponent_call} clash! Opponent wins!")
            self.opponent_wins += 1
        elif  self.player_call == "Scissors" and self.opponent_call == "Rock":
            print(f"Player's {self.player_call} and opponent's {self.opponent_call} clash! Opponent wins!")
            self.opponent_wins += 1
        elif  self.player_call == "Scissors" and self.opponent_call == "Paper":
            print(f"Player's {self.player_call} and opponent's {self.opponent_call} clash! Player wins!")
            self.player_wins += 1
        pass
    
    def reset_game(self):
        self.opponent_call = ""
        self.player_call = ""
        pass
    
    def print_stats(self):
        print(f"Player: {self.player_wins} Opponent: {self.opponent_wins} Tied: {self.ties}")
        pass

    def sequence(self):
        self.opponent_call_grab()
        self.player_call_grab()
        self.calculate_outcome()
        self.print_stats()
        pass

def play_again():
    player_input = input("Would you like to play again? Y/N: ")
    if player_input == "N" or player_input == "n":
        program_active = False

program_active = True
game = RockPaperScissors()
while program_active:
    game.sequence()
    play_again()
print("Thank you for playing!")
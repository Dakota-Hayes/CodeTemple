"""
Python Blackjack
For this project you will make a Blackjack game using Python. Click here to familiarize yourself with the the rules of the game. You won't be implementing every rule "down to the letter" with the game, but we will doing a simpler version of the game. This assignment will be given to further test your knowledge on object-oriented programming concepts.

Rules:
1. The game will have two players: the Dealer and the Player. The game will start off with a deck of 52 cards. The 52 cards will consist of 4 different suits: Clubs, Diamonds, Hearts and Spades. For each suit, there will be cards numbered 1 through 13.



Note: No wildcards will be used in the program
2. When the game begins, the dealer will shuffle the deck of cards, making them randomized. After the dealer shuffles, it will deal the player 2 cards and will deal itself 2 cards from. The Player should be able to see both of their own cards, but should only be able to see one of the Dealer's cards.
3. The objective of the game is for the Player to count their cards after they're dealt. If they're not satisfied with the number, they have the ability to 'Hit'. A hit allows the dealer to deal the Player one additional card. The Player can hit as many times as they'd like as long as they don't 'Bust'. A bust is when the Player is dealt cards that total more than 21.
4. If the dealer deals the Player cards equal to 21 on the first deal, the Player wins. This is referred to as Blackjack. Blackjack is NOT the same as getting cards that equal up to 21 after the first deal. Blackjack can only be attained on the first deal.
5. The Player will never see the Dealer's hand until the Player chooses to 'stand'. A Stand is when the player tells the dealer to not deal it anymore cards. Once the player chooses to Stand, the Player and the Dealer will compare their hands. Whoever has the higher number wins. Keep in mind that the Dealer can also bust.


This will be an exercise of how well you understand OOP(Object Oriented Programming). In this project, you will be using "Pair-Programming" to complete the assignment.
"""
import random

class Blackjack():

    def __init__(self):
        #print("Init")
        self.dealer_hand = []
        self.player_hand = []
        self.player_hand_value = 0
        self.dealer_hand_value = 0
        self.dealer_wins = 0
        self.player_wins = 0
        self.cards_remaining = 52
        self.available_cards = []
        self.shuffled_deck = []
        self.dealer_stay = True
        self.player_stay = True
        self.card_template = {
            "Suite" : "NA",
            "Value" : [0,0],
            "Name" : "NA",
        }
        pass
    
    def reset(self):
        #print("Reset")
        self.dealer_hand = []
        self.player_hand = []
        self.player_hand_value = 0
        self.dealer_hand_value = 0
        self.cards_remaining = 52
        self.available_cards = []
        self.shuffled_deck = []
        self.dealer_stay = True
        self.player_stay = True
        pass

    def create_cards(self):
        #print("Create Cards")
        suites = ["Hearts","Clubs","Spades","Diamonds"]
        royals = ["Jack","Queen","king"]
        for suite in suites:
            for i in range(10):
                new_card = {
                    "Suite" : "NA",
                    "Value" : [0,0],
                    "Name" : "NA",
                }
                new_card["Suite"] = suite
                if i == 0:
                    new_card["Value"][0] = 1
                    new_card["Value"][1] = 11
                    new_card["Name"] = str(f"Ace of {suite}")
                else:
                    new_card["Value"][0] = i + 1
                    new_card["Value"][1] = 0
                    new_card["Name"] = str(f"{i+1} of {suite}")
                self.available_cards.append(new_card)
            for royal in royals:
                new_card = {
                    "Suite" : "NA",
                    "Value" : [0,0],
                    "Name" : "NA",
                }
                new_card["Value"][0] = 10
                new_card["Value"][1] = 0
                new_card["Suite"] = suite
                new_card["Name"] = str(f"{royal} of {suite}")
                self.available_cards.append(new_card)
        
    def print_details(self):
        print(
        #self.dealer_hand,"- Dealer Hand",
        #self.player_hand,"- Player Hand",
        #self.player_hand_value,"- Player Hand Value",
        #self.dealer_hand_value,"- Dealer Hand Value",
        #self.dealer_wins,"- Dealer Wins",
        #self.player_wins,"- Player Wins",
        #self.cards_remaining,"- Cards Remaining",
        #self.available_cards,"- Available Cards",
        #self.shuffled_deck,"- Shuffled Deck",
        #self.dealer_stay,"- Dealer Stay",
        #self.player_stay,"- Player Stay",
        #self.card_template, "- Card Template"
        )
        pass

    def shuffle(self):
        #print("Shuffle")
        self.create_cards()
        selected_randoms = []
        self.shuffled_deck = self.available_cards 
        for card in self.available_cards:
            not_found = True
            while not_found:
                r_int = random.randint(1,52)
                if r_int not in selected_randoms:
                    selected_randoms.append(r_int)
                    not_found = False
                    self.shuffled_deck[r_int - 1] = card  
        pass

    def deal(self, dealt):
        #print(f"Deal {dealt}")
        if dealt == "Player":
            self.player_hand.append(self.shuffled_deck.pop(0))
        elif dealt == "Dealer":
            self.dealer_hand.append(self.shuffled_deck.pop(0))
        pass
    
    def calculate_hand(self):
        #print("Calculate Hand")
        self.player_hand_value = 0
        self.dealer_hand_value = 0
        for card in self.player_hand:
            if card["Value"] == [1,11]:
                self.player_hand_value += card["Value"][1]
                if self.player_hand_value > 21:
                    self.player_hand_value -= card["Value"][1]
                    self.player_hand_value += card["Value"][0]
            else:
                self.player_hand_value += card["Value"][0]
        for card in self.dealer_hand:
            if card["Value"] == [1,11]:
                self.dealer_hand_value += card["Value"][1]
                if self.dealer_hand_value > 21:
                    self.dealer_hand_value -= card["Value"][1]
                    self.dealer_hand_value += card["Value"][0]
            else:
               self.dealer_hand_value += card["Value"][0]
        pass

    def calculate_outcome(self):
        #print("Calculate Outcome")
        print("Dealer Hand:",self.dealer_hand_value)
        for card in self.dealer_hand:
            print(card["Name"])
        print("")
        print("Player Hand:",self.player_hand_value)
        for card in self.player_hand:
            print(card["Name"])
        print("")
        if self.dealer_hand_value > 21:
            print("Dealer Busts!")
            self.dealer_stay = False
        if self.player_hand_value > 21:
            print("Player Busts!")
            self.player_stay = False
        if self.dealer_hand_value == 21 and len(self.dealer_hand) == 2:
            print("Dealer Hits Blackjack!")
            self.dealer_stay = False
        if self.player_hand_value == 21 and len(self.player_hand) == 2:
            print("Player Hits Blackjack!")
            self.player_stay = False
        if self.player_hand_value <= 21:
            if self.player_hand_value > self.dealer_hand_value:
                self.player_wins += 1
                print("Player Wins")
            elif self.dealer_hand_value > 21:
                self.player_wins += 1
                print("Player Wins")
        if self.dealer_hand_value <= 21:
            if self.dealer_hand_value > self.player_hand_value:
                self.dealer_wins += 1
                print("Dealer Wins")
            elif self.player_hand_value > 21:
                self.dealer_wins += 1
                print("Dealer Wins")
        if self.dealer_hand_value > 21 and 21 < self.player_hand_value:
            print("Tie")
        if self.dealer_hand_value == self.player_hand_value:
            print("Tie")
        print(f"Player {self.player_hand_value}, Dealer {self.dealer_hand_value}.")
        print(f"Score - Player: {self.player_wins} Dealer: {self.dealer_wins}")
        pass
    
    def dealer_hit(self):
        #print("Dealer Hit")
        if self.dealer_hand_value <= 15:
            self.deal("Dealer")
            self.calculate_hand()
            return True
        print("Dealer Stands")
        return False
    
    def player_hit(self):
        #print("Player Hit")
        if self.player_hand_value < 21:
            ui = input(f"Would you like to hit? Hand: {self.player_hand_value} Y/N? ")
            if ui == "Y":
                self.deal("Player")
                self.calculate_hand()
                return True
            print("Player Stands")
            return False
        else:
            return False
    
    def check_for_stay(self):
        #print("Check for Stay")
        print("Dealer Hand:")
        print(self.dealer_hand[0]["Name"])
        print("")
        print("Player Hand:",self.player_hand_value)
        for card in self.player_hand:
            print(card["Name"])
        print("")
        while self.dealer_stay == True or self.player_stay == True:
            if self.dealer_stay == True:
                self.dealer_stay = self.dealer_hit()
            if self.player_stay == True:
                self.player_stay = self.player_hit()
        pass

    def sequence(self):
        self.shuffle()
        self.deal("Player")
        self.deal("Player")
        self.deal("Dealer")
        self.deal("Dealer")
        self.calculate_hand()
        self.check_for_stay()
        self.calculate_outcome()
        #self.print_details()
        pass

#main runtime program
run_program = True
blackjack_program = Blackjack()
print("Lets play Blackjack!")
while run_program: 
    blackjack_program.sequence()
    user_input = input("Would you like to play again? Y/N? ")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    if user_input == "N":
        run_program = False
    else:
        blackjack_program.reset()
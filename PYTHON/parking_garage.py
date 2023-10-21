import random

"""
Your assignment for today is to create a parking garage class to get more familiar with Object Oriented Programming(OOP). 


Your parking garage class should have the following methods:

By the end of this project each student should be able to:
- Explain and/or demonstrate creating classes
- Explain and/or demonstrate creating class methods
- Explain and/or demonstrate class instantiation


When the project is completed, commit the final changes and submit your GitHub link.
"""

class ParkingGarage():
    """
        You will need a few attributes as well:
        - tickets -> list
        - parkingSpaces -> list
        - currentTicket -> dictionary
    """
    def __init__(self):
        self.ticket_counter = 0
        self.remaining_tickets = 5
        self.remaining_parking = 5
        self.past_tickets = []
        self.tickets = []
        self.parking_spaces = [1,2,3,4,5]
        self.current_ticket = {"paid": False, "parking_spot": 0, "ticket_number": 0}
        pass
    """
        takeTicket
        - This should decrease the amount of tickets available by 1
        - This should decrease the amount of parkingSpaces available by 1
    """
    def takeTicket(self):
        if self.remaining_parking > 0 and self.remaining_parking > 0:
            self.ticket_counter += 1
            self.current_ticket["paid"] = False
            self.current_ticket["parking_spot"] = self.parking_spaces.pop(0)
            self.remaining_tickets -= 1
            self.remaining_parking -= 1
            self.current_ticket["ticket_number"] = self.ticket_counter
            self.tickets.append(self.current_ticket)
            self.current_ticket = {"paid" : False, "parking_spot" : 0, "ticket_number" : 0}
            print("Welcome! Here is your ticket!")
        else:
            print("Parking garage full!")
        pass
    """
        payForParking
        - Display an input that waits for an amount from the user and store it in a variable
        - If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
        - This should update the "currentTicket" dictionary key "paid" to True
    """    
    def payForParking(self):
        if self.remaining_tickets < 5:
            payment = input("Please type how much you would like to pay for your ticket: ")
            if payment != "":
                print("test")
                print("Payment made, please leave within 15 minutes!")
                self.tickets[0]["paid"] = True
        else:
            print("There are no cars in the parking garage!")
        pass
    """
        leaveGarage
        - If the ticket has been paid, display a message of "Thank You, have a nice day"
        - If the ticket has not been paid, display an input prompt for payment
        - Once paid, display message "Thank you, have a nice day!"
        - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
        - Update tickets list to increase by 1 (meaning add to the tickets list)
    """
    def leaveGarage(self):
        if self.remaining_tickets < 5:
            if self.tickets[0]["paid"] == True:
                print("Thank you, have a nice day!")
                self.parking_spaces.append(self.tickets[0]["parking_spot"])
                self.past_tickets.append(self.tickets.pop(0))
                self.remaining_tickets += 1
                self.remaining_parking += 1
            else:
                print("No payment provided, please pay!")
                payment = input("Please type how much you would like to pay for your ticket: ")
                if payment != "":
                    print("Thank you, have a nice day!")
                    self.tickets[0]["paid"] = True
                    self.parking_spaces.append(self.tickets[0]["parking_spot"])
                    self.past_tickets.append(self.tickets.pop(0))
                    self.remaining_tickets += 1
                    self.remaining_parking += 1
                else:
                    self.leaveGarage()
        else:
            print("There are no cars in the parking garage!")
        pass

garage_1 = ParkingGarage()
garage_1.takeTicket()
garage_1.payForParking()
garage_1.leaveGarage()
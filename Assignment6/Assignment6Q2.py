import random

class RockPaperScissors:
    def __init__(self, rounds):
        self.rounds = rounds
        self.currentRound = 0
        self.userWins = 0
        self.computerWins = 0
        self.choices = ["rock", "paper", "scissors"]
    
    def getComputerChoice(self):
        return random.choice(self.choices)
    
    def findWinner(self, userChoice, computerChoice):
        if userChoice == computerChoice:
            return "tie!"
        elif (userChoice == "rock" and computerChoice == "scissors") or \
             (userChoice == "scissors" and computerChoice == "paper") or \
             (userChoice == "paper" and computerChoice == "rock"):
            self.userWins += 1
            return "You win the round"
        else:
            self.computerWins += 1
            return "Computer wins the round"
    
    def checkWinner(self):
        if self.userWins > self.computerWins:
            return "You won!"
        elif self.computerWins > self.userWins:
            return "Computer won!"
        else:
            return "Tie!"
    
    def play(self):
        while self.currentRound < self.rounds:
            self.currentRound += 1
            print("Round", self.currentRound)
            userChoice = input("Enter rock, paper, or scissors: ").lower()
            if userChoice not in self.choices:
                print("Invalid choice")
                continue
            computerChoice = self.getComputerChoice()
            print("Computer chose: ",computerChoice)
            print(self.findWinner(userChoice, computerChoice))
            print()
        
        print(self.checkWinner())

rounds = int(input("Enter number of rounds: "))
game = RockPaperScissors(rounds)
game.play()



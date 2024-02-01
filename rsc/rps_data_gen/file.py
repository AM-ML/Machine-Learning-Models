from random import randint
from csv import writer

def get_outcome(user_choice, computer_choice):
    outcomes = {"rock": {"rock": 0, "paper": -1, "scissors": 1},
                "paper": {"rock": 1, "paper": 0, "scissors": -1},
                "scissors": {"rock": -1, "paper": 1, "scissors": 0}}

    return outcomes[user_choice][computer_choice]

def write_data(csv_writer):
    choices = ["rock", "paper", "scissors"]
    
    user_choice = choices[randint(0, 2)]
    computer_choice = choices[randint(0, 2)]
    
    outcome = get_outcome(user_choice, computer_choice)
    
    data = [user_choice, computer_choice, outcome]
    csv_writer.writerow(data)

def main():
    with open("rps.csv", "a", newline="\n") as file:
        csv_writer = writer(file)
        for _ in range(1, 5000001):
            write_data(csv_writer)

if __name__ == '__main__':
    main()

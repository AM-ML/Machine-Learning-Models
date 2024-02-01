from random import randint

def f():
	num = randint(0, 2)

	choices = ["rock", "paper", "scissors"]

	computer_choice = choices[num]
	user_choice = input("enter your choice: ").strip().lower()

	print(f"you: {user_choice}")
	print(f"computer: {computer_choice}\n")
	print(f"{user_choice} - {computer_choice}")
	print(f"you ", end="")

	if user_choice == "rock" and computer_choice == "paper":
		print("lose!")

	if user_choice == "rock" and computer_choice == "scissors":
		print("won!")

	if user_choice == "rock" and computer_choice == "rock":
		print("draw!")

	if user_choice == "paper" and computer_choice == "paper":
		print("draw!")

	if user_choice == "paper" and computer_choice == "rock":
		print("won!")

	if user_choice == "paper" and computer_choice == "scissors":
		print("lose!")

	if user_choice == "scissors" and computer_choice == "scissors":
		print("draw!")

	if user_choice == "scissors" and computer_choice == "paper":
		print("won!")

	if user_choice == "scissors" and computer_choice == "rock":
		print("lose!")

def main():
	f()

if __name__ == '__main__':
	main()
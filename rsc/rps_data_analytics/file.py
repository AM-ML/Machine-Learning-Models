from csv import DictReader
from collections import defaultdict

choices = defaultdict(lambda: {"played": 0, "won": 0, "lost": 0, "drawn": 0})

def process_row(row):
    user_choice = row["user_choice"]
    outcome = int(row["outcome"])

    choices[user_choice]["played"] += 1
    choices[user_choice]["won"] += outcome == 1
    choices[user_choice]["lost"] += outcome == -1
    choices[user_choice]["drawn"] += outcome == 0

def f():
    with open("rps.csv", "r") as f:
        file = DictReader(f)
        for row in file:
            process_row(row)

    print("data:")
    for choice, stats in choices.items():
        print(f"{choice}:")
        print(f"    played: {stats['played']:,} times")
        print(f"       won: {stats['won']:,} times")
        print(f"      lost: {stats['lost']:,} times")
        print(f"     drawn: {stats['drawn']:,} times\n")

def main():
    f()

if __name__ == '__main__':
    main()

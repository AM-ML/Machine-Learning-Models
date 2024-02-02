import tkinter as tk
import random

end = 0

def generate_word():
    with open('dict.txt', 'r') as file:
        words = [word.strip().lower() for word in file.readlines() if word.strip().isalpha() and len(word.strip()) >= 4]
    return random.choice(words)


class WordleGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Wordle Game")
        self.master.geometry("500x600")
        
        self.restart_game()

    def restart_game(self):
        self.word = generate_word()
        self.word_length = len(self.word)
        self.tries_left = 5
        self.current_try = 0
        self.squares = []  # Added to store Label widgets

        self.create_game_ui()

    def create_game_ui(self):
        entry_frame = tk.Frame(self.master)
        entry_frame.grid(row=0, columnspan=self.word_length, pady=10)

        self.entry_var = tk.StringVar()
        entry = tk.Entry(entry_frame, textvariable=self.entry_var, font=('Arial', 14))
        entry.pack(ipadx=10, ipady=10, padx=1, pady=1)
        entry.focus_set()  # Set focus on entry at launch
        entry.bind("<Return>", lambda event: self.check_word())  # Bind Enter key to check_word

        for i in range(self.tries_left):
            row_squares = []
            for j in range(self.word_length):
                square = tk.Label(self.master, text="", width=2, font=('Arial', 14), relief="solid")
                square.grid(row=i + 1, column=j, ipadx=10, ipady=10, padx=1, pady=1)
                row_squares.append(square)
            self.squares.append(row_squares)

        submit_button = tk.Button(self.master, text="Submit", command=self.check_word)
        submit_button.grid(row=self.tries_left + 1, columnspan=self.word_length, pady=10)
        submit_button.bind("<Return>", lambda event: self.check_word())  # Bind Enter key to check_word for the button

    def check_word(self):
        user_word = self.entry_var.get()

        if len(user_word) != self.word_length:
            return  # Do not proceed if the word length is incorrect

        for i in range(self.word_length):
            square = self.squares[self.current_try][i]
            square.config(text=user_word[i])  # Fill the square with the corresponding character

            if user_word[i] == self.word[i]:
                square.config(bg='green', fg='#fff')
            elif user_word[i] in self.word:
                square.config(bg='yellow', fg='#fff')

        self.current_try += 1

        if self.current_try == self.tries_left or user_word == self.word:
            self.display_result()
            self.entry_var.disabled = True
            end = 1
        self.entry_var.set("")

    def display_result(self):
        result_label = tk.Label(self.master, text=f"The word was: {self.word}", font=('Arial', 14))
        result_label.grid(row=self.current_try + 1, columnspan=self.word_length, pady=10)
        for square_row in self.squares:
            for square in square_row:
                square.config(state='disabled')


if __name__ == "__main__":
    root = tk.Tk()
    game = WordleGame(root)
    root.mainloop()


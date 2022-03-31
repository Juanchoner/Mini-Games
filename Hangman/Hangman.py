import  tkinter
from assets import styles
from Hangman import words
from random import choice

class HangmanScreen(tkinter.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=styles.BACKGROUND)
        self.controller = controller

        self.show_lines = tkinter.StringVar()

        self.random_word()
        self.create_widgets()

    def random_word(self):
        self.word = choice(words.WORDS)
        lines = ''
        for letter in range(len(self.word)):
            lines += '_ '
        self.show_lines.set(lines)
        self.attempts = 0

    def click_letter(self, letter_button: str):
        if self.word.find(letter_button) == -1:
            self.attempts += 1
        else:
            for pos_letter in range(len(self.word)):
                if self.word[pos_letter] == letter_button:
                    quit_spaces = self.show_lines.get().replace(' ', '')
                    only_lines = list(quit_spaces)
                    only_lines[pos_letter] = letter_button
                    self.show_lines.set(' '.join(only_lines))
        if self.show_lines.get().replace(' ', '') == self.word: 
            print('Has ganado')
            self.random_word()
        elif self.attempts == 6: 
            print('Game Over!!!')
            self.random_word()

    def back_menu(self):
        self.random_word()
        self.controller.show_frame('MenuGames')

    def create_widgets(self):
        tkinter.Label(self, text='Juago del ahorcado').grid(column=0, row=0)
        tkinter.Label(self, textvariable=self.show_lines).grid(column=0, row=1)

        letters = tkinter.Frame(self)
        letters.grid(column=0, row=2)
        num_column = 0
        num_row = 0
        for letter in words.LETTERS:
            tkinter.Button(letters, text=letter, command=lambda l=letter:self.click_letter(l)).grid(column=num_column, row=num_row)
            num_column += 1
            if num_column == 10:
                num_row += 1
                num_column = 0
        
        tkinter.Button(self, text='⏮', command=self.back_menu).grid(column=0, row=3, sticky=tkinter.NSEW)

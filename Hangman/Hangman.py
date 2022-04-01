import  tkinter
from tkinter import messagebox
from assets import styles
from Hangman import words
from random import choice
from pathlib import Path
import os

class HangmanScreen(tkinter.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=styles.BACKGROUND)
        self.controller = controller

        self.root_path = Path(__file__).parent.parent
        self.show_lines = tkinter.StringVar()

        self.hangman_images = {
            0: os.path.join('assets', 'Hangman', 'Gallow.png'),
            1: os.path.join('assets', 'Hangman', 'HangmanHead.png'),
            2: os.path.join('assets', 'Hangman', 'HangmanBody.png'),
            3: os.path.join('assets', 'Hangman', 'HangmanArmOne.png'),
            4: os.path.join('assets', 'Hangman', 'HangmanArmTwo.png'),
            5: os.path.join('assets', 'Hangman', 'HangmanLegOne.png'),
            6: os.path.join('assets', 'Hangman', 'HangmanLegTwo.png')
        }

        self.hangman_img = tkinter.PhotoImage()

        self.random_word()
        self.create_widgets()

    def random_word(self):
        self.word = choice(words.WORDS)
        lines = ''
        for letter in range(len(self.word)):
            lines += '_ '
        self.show_lines.set(lines)
        self.attempts = 0
        self.hangman_img.configure(file=os.path.join(self.root_path, self.hangman_images[self.attempts]))

    def click_letter(self, letter_button: str):
        if self.word.find(letter_button) == -1:
            self.attempts += 1
            self.hangman_img.configure(file=os.path.join(self.root_path, self.hangman_images[self.attempts]))
        else:
            for pos_letter in range(len(self.word)):
                if self.word[pos_letter] == letter_button:
                    quit_spaces = self.show_lines.get().replace(' ', '')
                    only_lines = list(quit_spaces)
                    only_lines[pos_letter] = letter_button
                    self.show_lines.set(' '.join(only_lines))
        if self.show_lines.get().replace(' ', '') == self.word:
            msg = 'Has ganado esta partida 😀\nel juego se reiniciará'
            messagebox.showinfo('Felicidades!!!', msg)
            self.random_word()
        elif self.attempts == 6:
            msg = f'Has perdido esta partidad\nLa palabra era: {self.word}\nel juego se reiniciará'
            messagebox.showinfo('Suerte para la próxima', msg)
            self.random_word()

    def back_menu(self):
        self.random_word()
        self.controller.show_frame('MenuGames')

    def create_widgets(self):
        tkinter.Label(self, text='Juago del ahorcado', **styles.TITLES).grid(column=0, row=0)
        tkinter.Label(self, image=self.hangman_img).grid(column=0, row=1)
        tkinter.Label(self, textvariable=self.show_lines, **styles.LABELS).grid(column=0, row=2)

        letters = tkinter.Frame(self)
        letters.configure(background=styles.BACKGROUND)
        letters.grid(column=0, row=3, sticky=tkinter.NSEW)
        num_column = 0
        num_row = 0
        for letter in words.LETTERS:
            tkinter.Button(letters, text=letter, command=lambda l=letter:self.click_letter(l)).grid(column=num_column, row=num_row, sticky=tkinter.NSEW)
            num_column += 1
            if num_column == 10:
                num_row += 1
                num_column = 0

        tkinter.Button(self, text='⏮', command=self.back_menu).grid(column=0, row=4, sticky=tkinter.NSEW)

        self.grid_columnconfigure(0, weight=1)
        for i in range(10):
            letters.grid_columnconfigure(i, weight=1)

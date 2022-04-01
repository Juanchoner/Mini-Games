import tkinter
from assets import styles
from pathlib import Path
import os

class MenuGames(tkinter.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=styles.BACKGROUND)
        self.controller = controller

        self.root_path = Path(__file__).parent

        self.game_images = {
            0: os.path.join('assets', 'Menu', 'RockPaperScissors.png'),
            1: os.path.join('assets', 'Menu', 'GuessNumber.png'),
            2: os.path.join('assets', 'Menu', 'DiceSimulator.png'),
            3: os.path.join('assets', 'Menu', 'Hangman.png'),
            4: os.path.join('assets', 'Menu', 'TicTacToe.png')
        }

        self.rock_paper_scissors_img = tkinter.PhotoImage(file=os.path.join(self.root_path, self.game_images[0]))
        self.guess_number_img = tkinter.PhotoImage(file=os.path.join(self.root_path, self.game_images[1]))
        self.dice_simulator_img = tkinter.PhotoImage(file=os.path.join(self.root_path, self.game_images[2]))
        self.hangman_img = tkinter.PhotoImage(file=os.path.join(self.root_path, self.game_images[3]))
        self.tictactoe_img = tkinter.PhotoImage(file=os.path.join(self.root_path, self.game_images[4]))

        self.create_widgets()

    def create_widgets(self):
        tkinter.Label(self, text='Mini Games', **styles.TITLES).grid(column=0, row=0)

        games_images = tkinter.Frame(self)
        games_images.configure(background=styles.BACKGROUND)
        games_images.grid(column=0, row=1)
        tkinter.Button(games_images, image=self.rock_paper_scissors_img, command=lambda: self.controller.show_frame("RockPaperScissorsScreen")).grid(column=0, row=0)
        tkinter.Button(games_images, image=self.guess_number_img, command=lambda: self.controller.show_frame("GuessNumberScreen")).grid(column=0, row=1)
        tkinter.Button(games_images, image=self.dice_simulator_img, command=lambda: self.controller.show_frame("DiceSimulatorScreen")).grid(column=1, row=0)
        tkinter.Button(games_images, image=self.hangman_img, command=lambda: self.controller.show_frame("HangmanScreen")).grid(column=1, row=1)
        tkinter.Button(games_images, image=self.tictactoe_img, command=lambda: self.controller.show_frame("TicTacToeScreen")).grid(column=0, row=2)

        self.grid_columnconfigure(0, weight=1)

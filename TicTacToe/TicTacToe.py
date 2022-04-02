import tkinter
from tkinter import messagebox
from assets import styles
from pathlib import Path
import os

class TicTacToeScreen(tkinter.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=styles.BACKGROUND)
        self.controller = controller

        self.root_path = Path(__file__).parent.parent
             
        self.reference_buttons = {}

        self.sign_images = {
            0: os.path.join('assets', 'TicTacToe', 'Empty.png'),
            1: os.path.join('assets', 'TicTacToe', 'X.png'),
            2: os.path.join('assets', 'TicTacToe', 'O.png')
        }

        self.sing_empty = tkinter.PhotoImage(file=os.path.join(self.root_path, self.sign_images[0]))
        self.sign_x = tkinter.PhotoImage(file=os.path.join(self.root_path, self.sign_images[1]))
        self.sign_o = tkinter.PhotoImage(file=os.path.join(self.root_path, self.sign_images[2]))

        self.toggle = 1
        self.attempts = 0

        self.board_spaces = ['' for i in range(9)]

        self.create_widgets()

    def reset_game(self):
        self.toggle = 1
        self.attempts = 0
        for value in self.reference_buttons.values():
            value.configure(image=self.sing_empty, state=tkinter.NORMAL)
        for spaces in range(0, 9):
            self.board_spaces[spaces] = ''

    def check_spaces(self, sign_player: str):
        flag = False
        #Verticals
        if self.board_spaces[0] == sign_player and self.board_spaces[1] == sign_player and self.board_spaces[2] == sign_player:
            flag = True
        elif self.board_spaces[3] == sign_player and self.board_spaces[4] == sign_player and self.board_spaces[5] == sign_player:
            flag = True
        elif self.board_spaces[6] == sign_player and self.board_spaces[7] == sign_player and self.board_spaces[8] == sign_player:
            flag = True
        #Horizontals
        elif self.board_spaces[0] == sign_player and self.board_spaces[3] == sign_player and self.board_spaces[6] == sign_player:
            flag = True
        elif self.board_spaces[1] == sign_player and self.board_spaces[4] == sign_player and self.board_spaces[7] == sign_player:
            flag = True
        elif self.board_spaces[2] == sign_player and self.board_spaces[5] == sign_player and self.board_spaces[8] == sign_player:
            flag = True
        #Diagonals
        elif self.board_spaces[0] == sign_player and self.board_spaces[4] == sign_player and self.board_spaces[8] == sign_player:
            flag = True
        elif self.board_spaces[2] == sign_player and self.board_spaces[4] == sign_player and self.board_spaces[6] == sign_player:
            flag = True

        if flag:
            msg = f'A ganado el jugador con el simbolo: {sign_player}\nel juego se reiniciará'
            messagebox.showinfo('Atención', msg)
            self.reset_game()
            return
        if self.attempts == 9:
            msg = f'EMPATE el juego se reiniciará'
            messagebox.showinfo('Atención', msg)
            self.reset_game()

    def clic_button(self, id_button: int):
        if self.toggle == 1:
            self.toggle = 0
            self.reference_buttons[id_button].configure(image=self.sign_x, state=tkinter.DISABLED)
            self.board_spaces[id_button - 1] = 'X'
            self.check_spaces('X')
        else:
            self.toggle = 1
            self.reference_buttons[id_button].configure(image=self.sign_o, state=tkinter.DISABLED)
            self.board_spaces[id_button - 1] = 'O'
            self.check_spaces('O')
        self.attempts += 1

    def back_menu(self):
        self.reset_game()
        self.controller.show_frame('MenuGames')

    def create_widgets(self):
        tkinter.Label(self, text='Tic-Tac-Toe', **styles.TITLES).grid(column=0, row=0)

        board = tkinter.Frame(self)
        board.grid(column=0, row=1)
        ref = 1
        for colunm in range(3):
            for row in range(3):
                self.board_buttons =  tkinter.Button(board, image=self.sing_empty, command=lambda l=ref:self.clic_button(l), bg=styles.BACKGROUND)
                self.board_buttons.grid(column=colunm, row=row)
                self.reference_buttons[ref] = self.board_buttons
                ref +=1

        tkinter.Button(self, text='⏮', command=self.back_menu).grid(column=0, row=2, sticky=tkinter.NSEW)
        self.grid_columnconfigure(0, weight=1)

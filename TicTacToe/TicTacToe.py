from email.mime import image
import tkinter
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

        self.create_widgets()

    def clic_button(self, id_button: int):
        if self.toggle == 1:
            self.reference_buttons[id_button].configure(image=self.sign_x)
            self.toggle = 0
        else:
            self.reference_buttons[id_button].configure(image=self.sign_o)
            self.toggle = 1
        
    def back_menu(self):
        for value in self.reference_buttons.values():
            value.configure(image=self.sing_empty)
        self.controller.show_frame('MenuGames')

    def create_widgets(self):
        tkinter.Label(self, text='Tic-Tac-Toe').grid(column=0, row=0)

        board = tkinter.Frame(self)
        board.grid(column=0, row=1)
        ref = 1
        for colunm in range(3):
            for row in range(3):
                self.board_buttons =  tkinter.Button(board, image=self.sing_empty, command=lambda l=ref:self.clic_button(l))
                self.board_buttons.grid(column=colunm, row=row)
                self.reference_buttons[ref] = self.board_buttons
                ref +=1

        tkinter.Button(self, text='⏮', command=self.back_menu).grid(column=0, row=2)
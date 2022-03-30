import tkinter
from assets import styles
import random
from pathlib import Path
import os

class RockPaperScissorsScreen(tkinter.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background = styles.BACKGROUND)
        self.controller = controller
        self.options = ["PIEDRA", "PAPEL", "TIJERA"]

        self.root_path = Path(__file__).parent.parent

        self.elements = {
            0: os.path.join('assets', 'RockPaperScissors', 'Rock.png'),
            1: os.path.join('assets', 'RockPaperScissors', 'Paper.png'),
            2: os.path.join('assets', 'RockPaperScissors', 'Scissors.png'),
            3: os.path.join('assets', 'RockPaperScissors', 'None.png')
        }

        self.user_rock = tkinter.PhotoImage(file=os.path.join(self.root_path, self.elements[0]))
        self.user_paper = tkinter.PhotoImage(file=os.path.join(self.root_path, self.elements[1]))
        self.user_scissors = tkinter.PhotoImage(file=os.path.join(self.root_path, self.elements[2]))

        self.machine_element = tkinter.PhotoImage(file=os.path.join(self.root_path, self.elements[3]))

        self.show_machine_selection = tkinter.StringVar()

        self.winning_message = tkinter.StringVar()

        self.creat_widgets()

    def machine_selection(self):
        selection = random.choice(self.options)
        self.show_machine_selection.set(selection)
        return selection

    def what_is(self, option_user, option_machine):
        user = self.options.index(option_user)
        machine = self.options.index(option_machine)
        return user, machine

    def start_game(self, option):
        user_selection = option
        machine_selection = self.machine_selection()
        user, machine = self.what_is(user_selection, machine_selection)
        self.machine_element.configure(file=os.path.join(self.root_path, self.elements[machine]))
        if user == 0 and machine == 1: self.winning_message.set('Gana máquina')
        elif user == 0 and machine == 2: self.winning_message.set('Gana usuario')
        elif user == 1 and machine == 2: self.winning_message.set('Gana máquina')
        elif user == 1 and machine == 0: self.winning_message.set('Gana usuario')
        elif user == 2 and machine == 0: self.winning_message.set('Gana máquina')
        elif user == 2 and machine == 1: self.winning_message.set('Gana usuario')
        else: self.winning_message.set('EMPATE')

    def back_menu(self):
        self.show_machine_selection.set('')
        self.winning_message.set('')
        self.machine_element.configure(file=os.path.join(self.root_path, self.elements[3]))
        self.controller.show_frame("MenuGames")

    def creat_widgets(self):
        tkinter.Label(self, text='Pieda papel y tijera', **styles.TITLES).grid(column=0, row=0, sticky = tkinter.NSEW)
        tkinter.Label(self, text='Humano: Seleciona tu opción', **styles.LABELS).grid(column=0, row=1)

        elements = tkinter.Frame(self, background=styles.BACKGROUND)
        elements.grid(column=0, row=2)
        tkinter.Button(elements, image=self.user_rock, command=lambda:self.start_game(self.options[0])).grid(column=0, row=0)
        tkinter.Button(elements, image=self.user_paper, command=lambda:self.start_game(self.options[1])).grid(column=1, row=0)
        tkinter.Button(elements, image=self.user_scissors, command=lambda:self.start_game(self.options[2])).grid(column=0, row=1)
        
        tkinter.Label(self, text='Máquina a seleccionado:', **styles.LABELS).grid(column=0, row=5, sticky = tkinter.NSEW)
        tkinter.Label(self, image=self.machine_element, **styles.LABELS).grid(column=0, row=6, sticky = tkinter.NSEW)
        tkinter.Label(self, textvariable=self.winning_message, **styles.LABELS).grid(column=0, row=7, sticky = tkinter.NSEW)
        tkinter.Button(self, text='⏮', command=self.back_menu).grid(column=0, row=8, sticky=tkinter.NSEW)

        self.grid_columnconfigure(0, weight=1)

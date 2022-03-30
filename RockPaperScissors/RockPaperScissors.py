import tkinter
from assets import styles
import random

class RockPaperScissorsScreen(tkinter.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background = 'red')
        self.controller = controller
        self.options = ["PIEDRA", "PAPEL", "TIJERA"]

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
        self.controller.show_frame("MenuGames")

    def creat_widgets(self):
        tkinter.Label(self, text='Pieda papel y tijera').grid(column=0, row=0, sticky = tkinter.NSEW)
        tkinter.Label(self, text='Humano: Seleciona tu opción').grid(column=0, row=1)
        tkinter.Button(self, text=self.options[0], command=lambda:self.start_game(self.options[0])).grid(column=0, row=2, sticky = tkinter.NSEW)
        tkinter.Button(self, text=self.options[1], command=lambda:self.start_game(self.options[1])).grid(column=0, row=3, sticky = tkinter.NSEW)
        tkinter.Button(self, text=self.options[2], command=lambda:self.start_game(self.options[2])).grid(column=0, row=4, sticky = tkinter.NSEW)
        tkinter.Label(self, text='Máquina a seleccionado: ').grid(column=0, row=5, sticky = tkinter.NSEW)
        tkinter.Label(self, textvariable=self.show_machine_selection).grid(column=0, row=6, sticky = tkinter.NSEW)
        tkinter.Label(self, textvariable=self.winning_message).grid(column=0, row=7, sticky = tkinter.NSEW)
        tkinter.Button(self, text='⏮', command=self.back_menu).grid(column=0, row=8, sticky=tkinter.NSEW)

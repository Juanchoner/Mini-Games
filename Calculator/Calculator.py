import tkinter
from assets import styles

class CalculatorScreen(tkinter.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=styles.BACKGROUND)
        self.controller = controller

        self.content_buttons = [
            '(',')','CE','AC',
            '7','8','9','/',
            '4','5','6','*',
            '1','2','3','-',
            '0','.','=','+',
        ]

        self.content_screen = tkinter.StringVar()
        self.show_operation = ''

        self.create_widgets()
    
    def solve_operation(self):
        try:
            res = eval(self.show_operation)
            res = str(res)
        except SyntaxError:
            res = 'Syntax error'
        self.show_operation = res

    def clic_button(self, content: str):
        if content == self.content_buttons[3]: self.show_operation = ''
        elif content ==  self.content_buttons[2]: self.show_operation = self.show_operation[:-1]
        elif content ==  self.content_buttons[18]: self.solve_operation()
        else: self.show_operation += content    
        self.content_screen.set(self.show_operation)

    def back_menu(self):
        self.content_screen.set('')
        self.show_operation = ''
        self.controller.show_frame('MenuGames')

    def create_widgets(self):
        tkinter.Label(self, text='Calculadora', **styles.TITLES).grid(column=0, row=0)
        tkinter.Entry(self,textvariable=self.content_screen, font=('sans serif', 16)).grid(column=0, row=1, sticky=tkinter.NSEW)

        buttons = tkinter.Frame(self)
        buttons.grid(column=0, row=2, sticky=tkinter.NSEW)
        c = 0
        r = 0
        for button in range(len(self.content_buttons)):
            tkinter.Button(buttons, 
                            text=self.content_buttons[button], 
                            width=5,
                            height=3,
                            command=lambda con=self.content_buttons[button]: self.clic_button(con)).grid(
                            column=c,
                            row=r,
                            sticky=tkinter.NSEW)
            c += 1
            if c == 4:
                r += 1
                c = 0
        
        tkinter.Button(self, text='⏮', command=self.back_menu).grid(column=0, row=3, sticky=tkinter.NSEW)
        
        self.grid_columnconfigure(0, weight=1)
        for c in range(0, 4):
            buttons.grid_columnconfigure(c, weight=1)

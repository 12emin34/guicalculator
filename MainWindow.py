import tkinter

import numexpr


class CalculatorApp(tkinter.Frame):
    def __init__(self, expression, equation, master=None):
        self.expression = expression
        self.expression = ""
        self.equation = tkinter.StringVar()
        super().__init__(master)
        self.master = master
        root.configure(background="gray")
        root.title("Calculator")
        root.geometry("400x315")
        root.resizable(0, 0)
        self.create_widgets()

    def create_widgets(self):
        expression_field = tkinter.Entry(root, textvariable=self.equation, font="Helvetica 14")
        expression_field.grid(columnspan=4, ipadx=88, ipady=40)
        self.equation.set('')
        button1 = tkinter.Button(root, text=' 1 ', fg='black', bg='light gray',
                                 command=lambda: self.press(1), height=2, width=10)
        button1.grid(row=2, column=0, )

        button2 = tkinter.Button(root, text=' 2 ', fg='black', bg='light gray',
                                 command=lambda: self.press(2), height=2, width=10)
        button2.grid(row=2, column=1, )

        button3 = tkinter.Button(root, text=' 3 ', fg='black', bg='light gray',
                                 command=lambda: self.press(3), height=2, width=10)
        button3.grid(row=2, column=2, )

        button4 = tkinter.Button(root, text=' 4 ', fg='black', bg='light gray',
                                 command=lambda: self.press(4), height=2, width=10)
        button4.grid(row=3, column=0, )

        button5 = tkinter.Button(root, text=' 5 ', fg='black', bg='light gray',
                                 command=lambda: self.press(5), height=2, width=10)
        button5.grid(row=3, column=1, )

        button6 = tkinter.Button(root, text=' 6 ', fg='black', bg='light gray',
                                 command=lambda: self.press(6), height=2, width=10)
        button6.grid(row=3, column=2, )

        button7 = tkinter.Button(root, text=' 7 ', fg='black', bg='light gray',
                                 command=lambda: self.press(7), height=2, width=10)
        button7.grid(row=4, column=0, )

        button8 = tkinter.Button(root, text=' 8 ', fg='black', bg='light gray',
                                 command=lambda: self.press(8), height=2, width=10)
        button8.grid(row=4, column=1, )

        button9 = tkinter.Button(root, text=' 9 ', fg='black', bg='light gray',
                                 command=lambda: self.press(9), height=2, width=10)
        button9.grid(row=4, column=2, )

        button0 = tkinter.Button(root, text=' 0 ', fg='black', bg='light gray',
                                 command=lambda: self.press(0), height=2, width=10)
        button0.grid(row=5, column=1, )

        plus = tkinter.Button(root, text=' + ', fg='black', bg='light gray',
                              command=lambda: self.press("+"), height=2, width=10)
        plus.grid(row=2, column=3, )

        minus = tkinter.Button(root, text=' - ', fg='black', bg='light gray',
                               command=lambda: self.press("-"), height=2, width=10)
        minus.grid(row=3, column=3, )

        multiply = tkinter.Button(root, text=' * ', fg='black', bg='light gray',
                                  command=lambda: self.press("*"), height=2, width=10)
        multiply.grid(row=4, column=3, )

        divide = tkinter.Button(root, text=' / ', fg='black', bg='light gray',
                                command=lambda: self.press("/"), height=2, width=10)
        divide.grid(row=5, column=3, )

        equal = tkinter.Button(root, text=' = ', fg='black', bg='light gray',
                               command=self.equalpress, height=2, width=10)
        equal.grid(row=5, column=2, )

        clear = tkinter.Button(root, text='Clear', fg='black', bg='light gray',
                               command=self.clear, height=2, width=10)
        clear.grid(row=1, column='3', )

    def press(self, num):
        self.num = num
        self.expression = self.expression + str(num)
        self.equation.set(self.expression)

    def equalpress(self):
        try:
            total = str(numexpr.evaluate(self.expression))
            self.equation.set(total)
            self.expression = ""
        except (ZeroDivisionError, SyntaxError):
            self.equation.set(" error ")
            self.expression = ""

    def clear(self):
        self.expression = ""
        self.equation.set("")


root = tkinter.Tk()
app = CalculatorApp(expression="", equation="", master=root)
app.mainloop()

#############################################################################
#
#
#
#
#
#
#
#
#################################################################################
from tkinter import *
import tkinter as tk
import copy
import math


class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("303x338")
        self.window.resizable(False, False)
        self.window.title("My Calculator")


        self.input = ""
        self.result = ""
        # self.backspace_symbol = '⌫'
        self.expression = StringVar()
        self.e = Entry(width=40, textvariable=self.expression, bg='White', font="ariel 30").place(x=0, y=0)

        self.para = self.button()
    def func(self, para):
        if para == "C":
            self.input = ""
            self.expression.set(self.input)
        elif para == '⌫':
            self.backspace = str(copy.deepcopy(self.input))
            print(self.backspace)
            self.backspace = self.backspace.rstrip(self.backspace[-1])
            self.expression.set(self.backspace)
            # print(self.backspace)
            self.input  = self.backspace

        elif para == "=":
            if input != "":
                lastchar = self.input[-1]
                if lastchar.isdigit():
                    self.result = eval(self.input)
                    self.expression.set(self.result)
                    self.input = str(self.result)
                else:
                    self.result = "ERROR"
                    self.expression.set(self.result)


        elif para == 'sin':
            pass
            # if para == "sin":
            #     self.result = math.sin(int(self.input))
            #     print(self.result)
            #     self.expression.set(str(self.result))
        else:
            self.input = self.input + str(para)
            self.expression.set(f"sin({self.input})")

    def solve(self, para):

        if para == "=":
            if input != "":
                if "sin" in self.input:
                    self.equation = self.input.replace()
                    if str(self.input).isdigit():
                        print(self.input)
                        self.input = math.sin(int(self.input))
                        print(self.input)

                        self.expression.set(str(self.input))
                lastchar = self.input[-1]
                if lastchar.isdigit():
                    self.result = eval(self.input)
                    self.expression.set(self.result)
                    self.input = str(self.result)
                else:
                    self.result = "ERROR"
                    self.expression.set(self.result)





    def clear(self, para):
        if para == "C":
            if input != "":
                self.input = ""
                self.expression.set(self.input)


    def backspace(self):
        if input != "":
            self.backspace = self.input
            print(self.e.get())
            length = len(self.backspace) - 1
            self.input.delete(length, END)
            # self.backspace = str(copy.deepcopy(self.input))
            # print(self.backspace)
            # self.backspace = self.backspace.rstrip(self.backspace[-1])
            # self.expression.set(self.backspace)
            # # print(self.backspace)
            # self.input = self.backspace

    def show(self, para):
        self.input = str(self.input) + str(para)
        self.expression.set(self.input)


    def button(self):
        Button(width=7, height=3, text='⌫', bg='lightgrey', command= self.backspace).place(x=2.5,y=107)
        Button(width=7, height=3, text='7', bg='white', command= lambda: self.show('7')).place(x=64.5,y=107)
        Button(width=7, height=3, text='8', bg='white', command= lambda: self.show('8')).place(x=124.5,y=107)
        Button(width=7, height=3, text='9', bg='white', command= lambda: self.show('9')).place(x=184.5,y=107)

        Button(width=7, height=3, text='x2', bg='lightgrey', command= lambda: self.show('**2')).place(x=2.5,y=164)
        Button(width=7, height=3, text='4', bg='white', command= lambda: self.show('4')).place(x=60,y=164)
        Button(width=7, height=3, text='5', bg='white', command= lambda: self.show('5')).place(x=120,y=164)
        Button(width=7, height=3, text='6', bg='white', command= lambda: self.show('6')).place(x=180,y=164)

        Button(width=7, height=3, text='√', bg='lightgrey', command= lambda: self.show('**(1/2)')).place(x=2.5,y=222)
        Button(width=7, height=3, text='1', bg='white', command= lambda: self.show('1')).place(x=60,y=222)
        Button(width=7, height=3, text='2', bg='white', command= lambda: self.show('2')).place(x=120,y=222)
        Button(width=7, height=3, text='3', bg='white', command= lambda: self.show('3')).place(x=180,y=222)


        Button(width=7, height=3, text='C', bg='lightgrey', command= lambda: self.clear('C')).place(x=2.5,y=50)
        Button(width=7, height=3, text='sin', bg='lightgrey', command= lambda: self.show(f'sin{self.input}')).place(x=60,y=50)
        Button(width=7, height=3, text='cos', bg='lightgrey', command= lambda: self.show('cos')).place(x=120,y=50)
        Button(width=7, height=3, text='tan', bg='lightgrey', command= lambda: self.show('tan')).place(x=180,y=50)

        Button(width=7, height=3, text='/', bg='lightgrey', command= lambda: self.show('/')).place(x=240,y=50)
        Button(width=7, height=3, text='*', bg='lightgrey', command= lambda: self.show('*')).place(x=240,y=107)
        Button(width=7, height=3, text='-', bg='lightgrey', command= lambda: self.show('-')).place(x=240,y=164)
        Button(width=7, height=3, text='+', bg='lightgrey', command= lambda: self.show('+')).place(x=240,y=222)

        Button(width=7, height=3, text='( )', bg='lightgrey', command= lambda: self.show('()')).place(x=2.5,y=280)
        Button(width=7, height=3, text='.', bg='lightgrey', command= lambda: self.show('.')).place(x=60,y=280)
        Button(width=7, height=3, text='0', bg='white', command= lambda: self.show('0')).place(x=120,y=280)
        Button(width=7, height=3, text='+/-', bg='lightgrey', command= lambda: self.show('*-1')).place(x=180,y=280)
        Button(width=7, height=3, text='=', bg='lightgrey', command= lambda: self.solve('=')).place(x=240,y=280)





    # def func(self, para):
    #
    #     if para == "C":
    #         self.input = ""
    #         self.expression.set(self.input)
    #     elif para == "=":
    #         self.result = eval(self.input)
    #         self.expression.set(self.result)
    #     else:
    #         self.input = self.input + str(para)
    #         self.expression.set(self.input)



    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    Calc = Calculator()
    Calc.run()


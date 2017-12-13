import tkinter as tk
from math import *
class Application(tk.Frame):
    root = tk.Tk()
    root.title('Calculator')
    expression= tk.Entry(root)
    expression.grid(row=6, columnspan=4)
    res=tk.Label(root, text='Result:')
    res.grid(row=0, column=2)
    buttons={}
    def __init__(self, master=None):
        super().__init__(master)
        #self.create_widgets()
        self.expression.bind('<Return>', self.evaluate)
        self.buttons.append(tk.Button(master, text='1', command= lambda:self.pushedNum(1)))
        self.buttons.append(tk.Button(master, text='2', command= lambda:self.pushedNum(2)))
        self.buttons.append(tk.Button(master, text='3', command= lambda:self.pushedNum(3)))
        self.buttons.append(tk.Button(master, text='4', command= lambda:self.pushedNum(4))
        self.buttons.append(tk.Button(master, text='5', command= lambda:self.pushedNum(5))
        self.buttons.append(tk.Button(master, text='6', command= lambda:self.pushedNum(6))
        self.buttons.append(tk.Button(master, text='7', command= lambda:self.pushedNum(7))
        self.buttons.append(tk.Button(master, text='8', command= lambda:self.pushedNum(8))
        self.buttons.append(tk.Button(master, text='9', command= lambda:self.pushedNum(9))
        self.buttons.append(tk.Button(master, text='+', command= lambda:self.pushedNum('+'))
        self.buttons.append(tk.Button(master, text='-', command= lambda:self.pushedNum('-'))
        self.buttons.append(tk.Button(master, text='*', command= lambda:self.pushedNum('*')).grid(row=3 ,column=3 )
        self.buttons.append(tk.Button(master, text='/', command= lambda:self.pushedNum('/')).grid(row=2 ,column=3 )
        self.buttons.append(tk.Button(master, text='^1/x', command= lambda:self.pushedNum('**(1/)')).grid(row=1 ,column=1 )
        self.buttons.append(tk.Button(master, text='^x', command= lambda:self.pushedNum('**')).grid(row=1 ,column=0 )
        self.buttons.append(tk.Button(master, text='CE', command= lambda:self.pushedNum('CE')).grid(row=5 ,column=0 )
        self.buttons.append(tk.Button(master, text='<[X]', command= self.backsp).grid(row=1 ,column=2 )
        self.buttons.append(tk.Button(master, text='=', command= self.evaluate).grid(row=5 ,column=2 )
        self.buttons.append(tk.Button(master, text='.', command= lambda:self.pushedNum('.')).grid(row=1 ,column=3 )
        self.buttons.append(tk.Button(master, text='0', command= lambda:self.pushedNum(0)).grid(row=5 ,column=1 )
        for x in self.buttons:
            x.configure(sticky=W)
    def backsp(self):
        self.expression.delete(len(self.expression.get())-1)
    def evaluate(self, event):
        self.res.configure(text=str(eval(self.expression.get())))
    def evaluate(self):
        self.res.configure(text=str(eval(self.expression.get())))
    def pushedNum(self, num):
        self.length= len(str(self.expression.get()))
        self.expression.insert(self.length, str(num))

app = Application()
app.mainloop()

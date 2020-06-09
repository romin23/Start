from tkinter import *
import math
root = Tk()
root.title("Calculator")                    #Title of Window

root.iconbitmap('icon.ico')

#====================================================================Variables==========================================================
n1 = int()
operation = str()

#==================================================================Display screen=====================================================

en = Entry(root,width=13,borderwidth = 2.5,bg = '#001437', fg = '#7898FB', font = ('Verdana',30) )
en.grid(row=0,column =0,columnspan=4)

#====================================================================Functions========================================================
def but_clk(val):
    curr = en.get()
    en.delete(0,END)
    en.insert(0,str(curr)+str(val))

def clear():
    en.delete(0, END)
    click.set('Trig')

def addd():
    nu1 = en.get()
    global n1
    global operation
    operation = 'add'
    n1 = int(nu1)
    en.delete(0, END)

def subb():
    nu1 = en.get()
    global n1
    global operation
    operation = 'sub'
    n1 = int(nu1)
    en.delete(0, END)

def mul():
    nu1 = en.get()
    global n1
    global operation
    operation = 'mul'
    n1 = int(nu1)
    en.delete(0, END)

def div():
    nu1 = en.get()
    global n1
    global operation
    operation = 'div'
    n1 = int(nu1)
    en.delete(0, END)

def pow():
    nu1 = en.get()
    global n1
    global operation
    operation = 'pow'
    n1 = int(nu1)
    en.delete(0, END)

def fact():
    nu1 = en.get()
    global n1
    global operation
    operation = 'fact'
    n1 = int(nu1)
    en.delete(0, END)



def equal():
    n2 = en.get()
    en.delete(0,END)
    
    if operation == 'add':
        en.insert(0, n1+int(n2))
    
    
    elif operation == 'sub':
        en.insert(0, n1-int(n2))
    
    elif operation == 'mul':
        en.insert(0, n1*int(n2))
    
    elif operation == 'div':
        en.insert(0, n1/int(n2))
    
    elif operation == 'pow':
        en.insert(0, n1**int(n2))
    
    elif operation == 'fact':
        facto = 1
        for i in range(n1,0,-1):
            facto*=i
        en.insert(0, facto)
    
    trigono = str(click.get())
    if trigono == 'Sin':
        n3 = math.radians(int(n2))
        ans = math.sin((n3))
        ans = round(ans,2)
        en.insert(0, ans)
    
    elif trigono == 'Cos':
        n3 = math.radians(int(n2))
        ans = math.cos((n3))
        ans = round(ans,2)
        en.insert(0, ans)
    
    elif trigono == 'Tan':
        n3 = math.radians(int(n2))
        ans = math.tan((n3))
        ans = round(ans,2)
        en.insert(0, ans)

    


#====================================================================Button============================================================


but_pow = Button(root, text='Pow', padx =11,pady =25,command = pow, font = ('Verdana',15),bg = '#B8FB3C',fg = '#001437').grid(row=1, column = 1)

click = StringVar()
click.set('Trig')
dr = OptionMenu(root, click ,'Sin','Cos','Tan')
dr.config(width=4, font=('Helvetica', 12),bg = '#B8FB3C',fg = '#001437')
dr.grid(row=1, column = 0,sticky="nsew")
dr['menu'].config(font=('calibri',(15)),bg = '#001437', fg = '#B8FB3C')

but_fact = Button(root, text='!', padx =27,pady =25,command = fact, font = ('Verdana',15),bg = '#B8FB3C',fg = '#001437').grid(row=1, column = 2)

but_mul = Button(root, text='*', padx =23,pady =25,command = mul, font = ('Verdana',15),bg = '#B8FB3C',fg = '#001437').grid(row=1, column = 3)

but1 = Button(root, text='1', padx =25,pady =25, font = ('Verdana',15) ,command =lambda: but_clk(1),bg = '#001437', fg = '#7898FB'  ).grid(row=2, column = 0)

but2 = Button(root, text='2', padx =25,pady =25, command = lambda: but_clk(2), font = ('Verdana',15),bg = '#001437', fg = '#7898FB'  ).grid(row=2, column = 1)

but3 = Button(root, text='3', padx =25,pady =25, command = lambda: but_clk(3), font = ('Verdana',15),bg = '#001437', fg = '#7898FB'  ).grid(row=2, column = 2)

but_div = Button(root, text='/', padx =25,pady =25,command = div, font = ('Verdana',15),bg = '#B8FB3C',fg = '#001437').grid(row=2, column = 3)

but4 = Button(root, text='4', padx =25,pady =25, command = lambda: but_clk(4), font = ('Verdana',15),bg = '#001437', fg = '#7898FB'  ).grid(row=3, column = 0)

but5 = Button(root, text='5', padx =25,pady =25, command = lambda: but_clk(5), font = ('Verdana',15),bg = '#001437', fg = '#7898FB'  ).grid(row=3, column = 1)

but6 = Button(root, text='6', padx =25,pady =25, command = lambda: but_clk(6), font = ('Verdana',15),bg = '#001437', fg = '#7898FB'  ).grid(row=3, column = 2)

but7 = Button(root, text='7', padx =25,pady =25, command = lambda: but_clk(7), font = ('Verdana',15),bg = '#001437', fg = '#7898FB'  ).grid(row=4, column = 0)

but8 = Button(root, text='8', padx =25,pady =25, command = lambda: but_clk(8), font = ('Verdana',15),bg = '#001437', fg = '#7898FB'  ).grid(row=4, column = 1)

but9 = Button(root, text='9', padx =25,pady =25, command = lambda: but_clk(9), font = ('Verdana',15),bg = '#001437', fg = '#7898FB' ).grid(row=4, column = 2)

but0 = Button(root, text='0', padx =25,pady =25, command = lambda: but_clk(0), font = ('Verdana',15),bg = '#001437', fg = '#7898FB'  ).grid(row=5, column = 0)

#photo = PhotoImage(file = r"C:\Gfg\circle.png")
but_add = Button(root, text='+' ,padx =21,pady =25,command = addd, font = ('Verdana',15),bg = '#B8FB3C',fg = '#001437').grid(row=4, column = 3)

but_sub = Button(root, text='-', padx =25,pady =25,command = subb, font = ('Verdana',15),bg = '#B8FB3C',fg = '#001437').grid(row=3, column = 3)



but_clr = Button(root, text='C', padx =25,pady =25,command =clear, font = ('Verdana',15),bg = '#001437', fg = '#B8FB3C' ).grid(row=5, column = 1)

but_equal = Button(root, text='=', padx =63,pady =25,command = equal, font = ('Verdana',15),bg = '#B8FB3C',fg = '#001437').grid(row=5, column =2,columnspan=2 )



root.mainloop()
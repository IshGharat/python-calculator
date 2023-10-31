from tkinter import *

# Create a Tkinter window
window =Tk()

# Set the window size and title
window.geometry("380x500")
window.title("CodeRunner Calculator")

# Set the background color and window icon
window.configure(bg="#3A3839")
window.iconbitmap("logo.ico")

# Initialize the expression string variable
expression=""

# Function to append the pressed number or operator to the expression
def press(n):
    global expression
    expression+=str(n)
    equation.set(expression)

# Function to evaluate the expression and display the result
def equal():
    try:
        global expression
        total=str(eval(expression))
        equation.set(total)
        expression=""
    except:
        equation.set("Error")
        expression=""

# Function to clear the expression
def clear():
    global expression
    expression=""
    equation.set("0")

# Function to remove the last character from the expression
def backspace():
    global expression
    expression=expression.rstrip(expression[-1])
    equation.set(expression)

# Create frames to organize the widgets
expression_frame=Frame(window,bg="#3A3839")
buttons_frame=Frame(window,bg="#3A3839")
expression_frame.pack()
buttons_frame.pack(padx=10,pady=10)

# Define font styles for the widgets
font_entry=('Cambria',20,'bold')
font_button=('Microsoft Sans Serif',12,'bold')

# Create a StringVar to hold the equation for the Entry widget
equation=StringVar()
equation.set("0")

# Create an Entry widget to display the equation
equation_field=Entry(expression_frame,textvariable=equation,font=font_entry,justify='right')
equation_field.pack(ipadx=10,ipady=10,pady=20,padx=20)

# Create buttons for numbers and operators
button0=Button(buttons_frame,text='0',font=font_button,relief='ridge',bg="#3A3839",fg="#0BDFFF",borderwidth=1,width=8,height=3,command=lambda:press(0))
button1=Button(buttons_frame,text='1',font=font_button,relief='ridge',bg="#3A3839",fg="#0BDFFF",borderwidth=1,width=8,height=3,command=lambda:press(1))
button2=Button(buttons_frame,text='2',font=font_button,relief='ridge',bg="#3A3839",fg="#0BDFFF",borderwidth=1,width=8,height=3,command=lambda:press(2))
button3=Button(buttons_frame,text='3',font=font_button,relief='ridge',bg="#3A3839",fg="#0BDFFF",borderwidth=1,width=8,height=3,command=lambda:press(3))
button4=Button(buttons_frame,text='4',font=font_button,relief='ridge',bg="#3A3839",fg="#0BDFFF",borderwidth=1,width=8,height=3,command=lambda:press(4))
button5=Button(buttons_frame,text='5',font=font_button,relief='ridge',bg="#3A3839",fg="#0BDFFF",borderwidth=1,width=8,height=3,command=lambda:press(5))
button6=Button(buttons_frame,text='6',font=font_button,relief='ridge',bg="#3A3839",fg="#0BDFFF",borderwidth=1,width=8,height=3,command=lambda:press(6))
button7=Button(buttons_frame,text='7',font=font_button,relief='ridge',bg="#3A3839",fg="#0BDFFF",borderwidth=1,width=8,height=3,command=lambda:press(7))
button8=Button(buttons_frame,text='8',font=font_button,relief='ridge',bg="#3A3839",fg="#0BDFFF",borderwidth=1,width=8,height=3,command=lambda:press(8))
button9=Button(buttons_frame,text='9',font=font_button,relief='ridge',bg="#3A3839",fg="#0BDFFF",borderwidth=1,width=8,height=3,command=lambda:press(9))
multiply=Button(buttons_frame,text='*',font=font_button,relief='ridge',bg="#3A3839",fg="#0BDFFF",borderwidth=1,width=8,height=3,command=lambda:press("*"))
divide=Button(buttons_frame,text='/',font=font_button,relief='ridge',bg="#3A3839",fg="#0BDFFF",borderwidth=1,width=8,height=3,command=lambda:press("/"))
plus=Button(buttons_frame,text='+',font=font_button,relief='ridge',bg="#3A3839",fg="#0BDFFF",borderwidth=1,width=8,height=3,command=lambda:press("+"))
minus=Button(buttons_frame,text='-',font=font_button,relief='ridge',bg="#3A3839",fg="#0BDFFF",borderwidth=1,width=8,height=3,command=lambda:press("-"))
decimal=Button(buttons_frame,text='.',font=font_button,relief='ridge',bg="#3A3839",fg="#0BDFFF",borderwidth=1,width=8,height=3,command=lambda:press("."))

# Create buttons for special operations
clear=Button(buttons_frame,text='AC',font=font_button,relief='ridge',bg="#3A3839",fg="#0BDFFF",borderwidth=1,width=8,height=3,command=clear)
equal=Button(buttons_frame,text='=',font=font_button,relief='ridge',bg="#3A3839",fg="#0BDFFF",borderwidth=1,width=8,height=3,command=equal)
backspace=Button(buttons_frame,text='<-',font=font_button,relief='ridge',bg="#3A3839",fg="#0BDFFF",borderwidth=1,width=8,height=3,command=backspace)

# Grid layout to organize the buttons
clear.grid(row=0,column=0,columnspan=2,sticky='nsew')
backspace.grid(row=0,column=2,columnspan=2,sticky='nsew')

multiply.grid(row=1,column=0)
button7.grid(row=1,column=1)
button8.grid(row=1,column=2)
button9.grid(row=1,column=3)

divide.grid(row=2,column=0)
button4.grid(row=2,column=1)
button5.grid(row=2,column=2)
button6.grid(row=2,column=3)

plus.grid(row=3,column=0)
button1.grid(row=3,column=1)
button2.grid(row=3,column=2)
button3.grid(row=3,column=3)

minus.grid(row=4,column=0)
decimal.grid(row=4,column=1)
button0.grid(row=4,column=2)
equal.grid(row=4,column=3)

# Start the Tkinter event loop
window.mainloop()

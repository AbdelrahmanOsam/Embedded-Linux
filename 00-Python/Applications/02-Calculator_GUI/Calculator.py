'''**********************************************************************'''
'''
* AUTHOR  : Abdelrahman Osam Khaled
* Date    : 24 May , 2023
* Version : V1.0	
'''
'''**********************************************************************'''
# Import tkinter module in python code
from tkinter import *



#Declare expression variable of screen
expression = ""

def press(num):
    # point out the global expression variable
    global expression
 
    # concatenation of string
    expression = expression + str(num)
 
    # update the expression by using set method
    equation.set(expression)
def EqualPress():
    # Try and except statement is used
    # for handling the errors like zero
    # division error etc.
 
    # Put that code inside the try block
    # which may generate the error
    try:
 
        global expression
 
        # eval function evaluate the expression
        # and str function convert the result
        # into string
        total = str(eval(expression))
 
        equation.set(total)
 
        # initialize the expression variable
        # by empty string
        expression = ""
 
    # if error is generate then handle
    # by the except block
    except:
 
        equation.set(" error ")
        expression = ""
		
def Clear():
    global expression
    expression = ""
    equation.set("")
 
 
# Driver code
if __name__ == "__main__":
		# Create a window
		 # create a GUI window
    window1 = Tk()
 
    # set the background colour of GUI window
    window1.configure(background="black")
 
    # set the title of GUI window
    window1.title("Simple Calculator")
 
    # set the configuration of GUI window
    window1.geometry("495x375")
 
    # StringVar() is the variable class
    # we create an instance of this class
    equation = StringVar()
 
    # create the text entry box for
    # showing the expression .
    expression_field = Entry(window1, textvariable=equation)
 
    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    expression_field.grid(columnspan=4, ipadx=185)

# Create the Calculator buttons
button1 = Button(window1, text=' 1 ', fg='black', bg='white',command=lambda: press(1), height=4, width=17)
button1.grid(row=2, column=0)

button2 = Button(window1, text=' 2 ', fg='black', bg='white',command=lambda: press(2), height=4, width=17)
button2.grid(row=2, column=1)

button3 = Button(window1, text=' 3 ', fg='black', bg='white',command=lambda: press(3), height=4, width=16)
button3.grid(row=2, column=2)

button4 = Button(window1, text=' 4 ', fg='black', bg='white',command=lambda: press(4), height=4, width=17)
button4.grid(row=3, column=0)

button5 = Button(window1, text=' 5 ', fg='black', bg='white',command=lambda: press(5), height=4, width=17)
button5.grid(row=3, column=1)

button6 = Button(window1, text=' 6 ', fg='black', bg='white',command=lambda: press(6), height=4, width=16)
button6.grid(row=3, column=2)

button7 = Button(window1, text=' 7 ', fg='black', bg='white',command=lambda: press(7), height=4, width=17)
button7.grid(row=4, column=0)

button8 = Button(window1, text=' 8 ', fg='black', bg='white',command=lambda: press(8), height=4, width=17)
button8.grid(row=4, column=1)

button9 = Button(window1, text=' 9 ', fg='black', bg='white',command=lambda: press(9), height=4, width=16)
button9.grid(row=4, column=2)

button0 = Button(window1, text=' 0 ', fg='black', bg='white',command=lambda: press(0), height=4, width=17)
button0.grid(row=5, column=0)

plus = Button(window1, text=' + ', fg='black', bg='white',command=lambda: press("+"), height=4, width=15)
plus.grid(row=2, column=3)

minus = Button(window1, text=' - ', fg='black', bg='white',command=lambda: press("-"), height=4, width=15)
minus.grid(row=3, column=3)

multiply = Button(window1, text=' x ', fg='black', bg='white',command=lambda: press("*"), height=4, width=15)
multiply.grid(row=4, column=3)

divide = Button(window1, text=' / ', fg='black', bg='white',command=lambda: press("/"), height=4, width=15)
divide.grid(row=5, column=3)

equal = Button(window1, text=' = ', fg='black', bg='white',command=EqualPress, height=4, width=16)
equal.grid(row=5, column=2)

Decimal= Button(window1, text='.', fg='black', bg='white',command=lambda: press('.'), height=4, width=17)
Decimal.grid(row=5, column='1')

clear = Button(window1, text='Clear', fg='black', bg='white',command=Clear, height=4, width=17)
clear.grid(row=6, column=0)

buttonOFF = Button(window1,text = "OFF",fg = "red", bg ="white",command=window1.destroy, height=4, width=17)
buttonOFF.grid(row=6, column=1)




# Call the main loop which is used when the application is ready to run to keep the code displaying 
window1.mainloop()
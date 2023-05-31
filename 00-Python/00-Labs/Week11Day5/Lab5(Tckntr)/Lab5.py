from tkinter import *
window = Tk()

window.title("Hello from tkinter")
window.geometry("500x500")

Label1 = Label(window, text = "Abdelrahman")
Label2 = Label(window, text = "RIGHT")
Label3 = Label(window, text = "BOTTOM")
Label4 = Label(window, text = "LEFT")


Label1.pack(side = TOP)

b1=Button(window , text = "TOP",command = Label1)
#Label2.pack(side = RIGHT)
#Label3.pack(side = LEFT)
#Label4.pack(side = BOTTOM)
b1.pack(side=TOP)

window.mainloop()
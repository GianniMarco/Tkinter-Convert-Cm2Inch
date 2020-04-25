import sys
from tkinter import *
from tkinter import messagebox

cm = Tk()
cm.title("Cm2Inch converter")

text = StringVar()

askcm = Label(text="cm:").grid(column=0, row=1)
entcm = Entry(cm, textvariable=text)
entcm.grid(column=1, row=1)

def OKfunc():
	numcm = entcm.get()
	messagebox.showinfo("Conerted!", "cm: {0}\ninch: {1}".format(numcm, cent2inch(numcm)))
	text.set("")

def cent2inch(convert):
	try:
		inches = float(convert) * 2.54
		return float(inches)
	except:
		messagebox.showerror("Invalid input", "Invalid input")
		return "Error"

OK = Button(cm, text="OK", command=OKfunc)
OK.grid(column=1, row =2, sticky="e")

cm.mainloop()
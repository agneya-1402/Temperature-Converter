from tkinter import *

a=Tk()
a.title("Temperature Converter")
#a.geometry("150x145")

def Fahr():#degree to fahrehneit
    b=int(entry.get())
    ans=(b*9/5)+32
    L1=Label(a,text="Fahrenheit :"+str(ans),bg="red",fg="white")
    L1.grid(row=1,column=1)

def Cel():#Fahrenheit to Celsius
    Temp2=int(entry.get())
    ans=(Temp2-32)*5/9
    L2=Label(a,text="Celsius :"+str(ans),bg="red",fg="white")
    L2.grid(row=1,column=1)

entry=Entry(a,bd=15)
entry.grid(row=0,column=1)

b1=Button(a,text="Celsius to Fahrenheit",bg="green",fg="white",activebackground="red",command=Fahr)
b1.grid(row=2,column=0)

b2=Button(a,text="Fahrenheit to Celsius",command=Cel,bg="blue",fg="white",activebackground="red")
b2.grid(row=3,column=0)

L1=Label(a,text="Enter Temperature :")
L1.grid(row=0,column=0)

a.mainloop()
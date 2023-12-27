from tkinter import *
from PIL import Image,ImageTk
import tkinter.messagebox as msg

root=Tk()
root.wm_geometry("900x600")
Label(text="Happy Travels", font="algerian 24").grid(row=0,column=4)

name=Label(root,text="Name")
phone=Label(root,text="Ph-No.")
email=Label(root,text="E-mail")
gender=Label(root,text="Gender")
age=Label(root,text="Age")
payment=Label(root,text="Amount Paid")

name.grid(row=1,column=3)
phone.grid(row=2,column=3)
email.grid(row=3,column=3)
gender.grid(row=4,column=3)
age.grid(row=5,column=3)
payment.grid(row=6,column=3)

def getvals():    
    print(f"{namevalue.get(),phonevalue.get(),emailvalue.get(),gendervalue.get(),agevalue.get(),paymentvalue.get(),myslider.get()}\n")
    msg.showinfo("Trip Booked",f"{namevalue.get(),phonevalue.get(),emailvalue.get(),gendervalue.get(),agevalue.get(),paymentvalue.get(),myslider.get()}")
    with open("record.txt","a") as f:
        f.write(f"{namevalue.get(),phonevalue.get(),emailvalue.get(),gendervalue.get(),agevalue.get(),paymentvalue.get(),myslider.get()}\n")
        
namevalue=StringVar() 
phonevalue=StringVar()
emailvalue=StringVar()
gendervalue=StringVar()
agevalue=StringVar()
paymentvalue=StringVar()
foodvalue=IntVar()

nameentry=Entry(root,textvariable=namevalue)
phoneentry=Entry(root,textvariable=phonevalue)
emailentry=Entry(root,textvariable=emailvalue)
genderentry=Entry(root,textvariable=gendervalue)
ageentry=Entry(root,textvariable=agevalue)
paymententry=Entry(root,textvariable=paymentvalue)

nameentry.grid(row=1,column=4)
phoneentry.grid(row=2,column=4)
emailentry.grid(row=3,column=4)
genderentry.grid(row=4,column=4)
ageentry.grid(row=5,column=4)
paymententry.grid(row=6,column=4)
foodvalue=Checkbutton(text="Want to prebook your meal?")
foodvalue.grid(row=7,column=4)
Label(root,text="What would you like to have?",font="arialblack 9").grid(row=8,column=4)
var=IntVar()
radio1=Radiobutton(root,text="Breakfast",variable=var,value=1).grid(row=9,column=4)
radio2=Radiobutton(root,text="Lunch",variable=var,value=2).grid(row=10,column=4)
radio3=Radiobutton(root,text="Dinner",variable=var,value=3).grid(row=11,column=4)
radio4=Radiobutton(root,text="All of you want",variable=var,value=4).grid(row=12,column=4)
radio5=Radiobutton(root,text="None",variable=var,value=5).grid(row=13,column=4)
Label(root,text="Please give us rating").grid(row=14,column=4)
myslider=Scale(from_=0, to=5,orient=HORIZONTAL)
myslider.grid(row=15,column=4)
Button(text="Apply", command=getvals).grid(row=16,column=4)

root.mainloop()
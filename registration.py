from tkinter import*
root=Tk()
root.geometry("700x400")

def getvals():
    print("Accepted")

Label(root, text="Registration Form", font="ar 25 bold").grid(row=0, column=3)
#Field Name
name=Label(root, text="Name")
gender=Label(root, text="Gender")
phone=Label(root, text="Phone")
emergency=Label(root, text="Emergency")
payment=Label(root, text="Payment mood")

#packing filed
name.grid(row=1, column=2)
gender.grid(row=2, column=2)
phone.grid(row=3, column=2)
emergency.grid(row=4, column=2)
payment.grid(row=5, column=2)

#variable for storing data
namevalue=StringVar
gendervalue=StringVar
phonevalue=StringVar
emergencyvalue=StringVar
paymentvalue=StringVar
checkvalue=IntVar

#Creating entry field
nameentry= Entry(root,textvariable=namevalue)
genderentry= Entry(root,textvariable=gendervalue)
phoneentry= Entry(root,textvariable=phonevalue)
emergencyentry= Entry(root,textvariable=emergencyvalue)
paymententry= Entry(root,textvariable=paymentvalue)

#Packing entry field
nameentry.grid(row=1,column=3)
genderentry.grid(row=2,column=3)
phoneentry.grid(row=3,column=3)
emergencyentry.grid(row=4,column=3)
paymententry.grid(row=5,column=3)

#checkbox creating
checkbtn=Checkbutton(text="Remember me?",variable=checkvalue)
checkbtn.grid(row=6,column=3)

#Submit button
Button(text="Submit",command=getvals).grid(row=7,column=3)

root.mainloop()
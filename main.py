import csv
import smtplib
from tkinter import *
from tkinter import messagebox
import datetime as dt

now = dt.datetime.now()
current_date = now.date()
current_time = now.time()

def send_message():

    if sender_address.get() == "":
        messagebox.askretrycancel("warning","Please enter required information")
    else:
    
        address_info = address.get()
    
        email_body_info = email_body.get()

        sender_info = sender_address.get()

        password_info = password.get()
    
        server = smtplib.SMTP('smtp.outlook.com',587)
    
        server.starttls()
    
        server.login(sender_info,password_info)
    
        print("Login successful")
    
        server.sendmail(sender_info,address_info,email_body_info)

    
        messagebox.askokcancel("Congratulations",f"Message sent successfully at {now}.")
    # print(f"Message sent successfully at {x}.")
    with open("data.csv", 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data[0].keys())
        for item in data:
            writer.writerow(item.values())

    
        address_entry.delete(0,END)
        email_body_entry.delete(0,END)
        password_entry.delete(0,END)
        sender_address_entry.delete(0,END)
         
def cnn():
    messagebox.askyesno("Warning","Are you sure to exit?")
    gui.destroy()
       

data =[{'From': 'email', 'To': "email", 'time': str(current_time),"Date":str(current_date)}]
     

gui = Tk()
gui.maxsize(width=500,height=500)
gui.geometry("500x500")

gui.title("Email Sender App")
gui.iconbitmap("application_software_gmail_mail_1836.ico")
heading = Label(text="Enter the information",bg="green",fg="black",font="20",width="500",height="3")


heading.pack()
gui.configure(background = "green")

sender_address_field = Label(text="Sender's Email :",bg="green",fg="black",font="10")
sender_address_field.place(x=15,y=70)

sender_address = StringVar()
sender_address_entry = Entry(bg="white",fg = "black",bd=5,font="bold",textvariable=sender_address,width="30")
sender_address_entry.place(x=15,y=100)

sender_password_field = Label(text="Sender's Password :",bg="green",fg="black",font="10")
sender_password_field.place(x=15,y=140)

password = StringVar()
password_entry = Entry(bg="white",fg = "black",bd=5,font="bold",textvariable=password,width="30")
password_entry.place(x=15,y=170)

address_field = Label(text="Recipient Email :",bg="green",fg="black",font="10")
address_field.place(x=15,y=210)

address = StringVar()
address_entry = Entry(bg="white",fg = "black",bd=5,font="bold",textvariable=address,width="30")
address_entry.place(x=15,y=240)

email_body_field = Label(text="Message :",bg="green",fg="black",font="10")
email_body_field.place(x=15,y=280)

email_body = StringVar()
email_body_entry = Entry(bg="white",fg = "black",bd=5,font="bold",textvariable=email_body,width="30")
email_body_entry.place(x=15,y=320,height="30")

button = Button(gui,text="Send Message",command=send_message,width="30",height="2",bg="light grey")
button.place(x=15,y=400)
button1= Button(gui,text="Cancel",bg="light grey",width="30",height="2",command=cnn)
button1.place(x=270,y=400)
filename = 'data.csv'
print(f'Data saved to {filename}.')
gui.mainloop()
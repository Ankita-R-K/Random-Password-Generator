# this project is to generate random password and copy it to clipboard
# Import required libraries and modules
from tkinter import *
import random, string
import pyperclip
# create window
root = Tk()
root.geometry("400x400")
root.resizable(0,0)
root.title("RANDOM PASSWORD GENERATOR")
heading = Label(root, text = 'PASSWORD GENERATOR APPLICATION' , font ='arial 15 bold' , fg = 'green').pack(pady = 20)

# Select password length
pass_label = Label(root, text = 'PASSWORD LENGTH', font = 'arial 14 bold' , fg = 'orange').pack(pady = 10)
pass_len = IntVar()
length = Spinbox(root, from_ = 8, to_ = 32 , textvariable = pass_len , width = 15).pack()

# Function to generate the password
pass_str = StringVar()
def Generator():
    password = ''

    for x in range (0,4):
        password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) + random.choice(string.punctuation)
    for y in range(pass_len.get()- 4):
        password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)
Button(root, text = "GENERATE PASSWORD" , command = Generator , fg = 'blue',font = 'arial 10 bold' ).pack(pady= 10)

Entry(root , textvariable = pass_str).pack()
# Function to copy the password
def Copy_password():
    pyperclip.copy(pass_str.get())

Button(root, text = 'COPY TO CLIPBOARD', command = Copy_password, fg = 'black' , font = 'arial 10 bold').pack(pady=10)

root.mainloop()
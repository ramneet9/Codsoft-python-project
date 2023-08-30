from tkinter import *
import string
import random
import pyperclip

def generator():
    small_alphabets=string.ascii_lowercase
    capital_alphabets=string.ascii_uppercase
    numbers=string.digits
    special_characters=string.punctuation

    all=small_alphabets+capital_alphabets+numbers+special_characters
    password_length=int(length_box.get())
    if choice.get()==1:
        passwordField.insert(0,random.sample(small_alphabets,password_length))
    if choice.get()==2:
        passwordField.insert(0,random.sample(small_alphabets+capital_alphabets,password_length))
    if choice.get()==3:
        passwordField.insert(0,random.sample(all,password_length))

def copy():
    random_password=passwordField.get()
    pyperclip.copy(random_password)

def delete():
    passwordField.delete(0, END)

root=Tk()
root.config(bg="black")
choice=IntVar()
root.geometry('450x500')
Font=('arial',15,'bold')
passwordLabel=Label(root,text="password generator",font=('times new roman',21,'bold'),bg="orange",fg="white")
passwordLabel.pack(pady=10,side='top',fill=BOTH)

weakradioButton=Radiobutton(root,text="weak",value=1,variable=choice,font=Font)
weakradioButton.pack(pady=5,side='top')

mediumradioButton=Radiobutton(root,text="medium",value=2,variable=choice,font=Font)
mediumradioButton.pack(pady=5,side='top')

strongradioButton=Radiobutton(root,text="strong",width=10,value=3,variable=choice,font=Font)
strongradioButton.pack(pady=5,side='top')

lengthLabel=Label(root,text="password length",font=Font,bg="orange",fg="white")
lengthLabel.pack(pady=5,side='top')

length_box=Spinbox(root,from_=8,to_=18,width=5,font=Font)
length_box.pack(pady=5,side='top')

generateButton=Button(root,text="Generate",font=Font,command=generator)
generateButton.pack(pady=5,side='top')

passLabel=Label(root,text="display-box",font=Font,bg="orange",fg="white")
passLabel.pack(pady=5,side='top',fill=BOTH)

passwordField=Entry(root,width=29,bd=2)
passwordField.pack(pady=5,side="top")

copyButton=Button(root,text="Copy",font=Font,command=copy)
copyButton.pack(pady=5,side='top')

deleteButton=Button(root,text="Delete",font=Font,command=delete)
deleteButton.pack(pady=5,side='top')

root.mainloop()
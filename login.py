from customtkinter import *
from PIL import Image
from tkinter import messagebox

def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','All fields are required')
    elif usernameEntry.get()=='ad' and passwordEntry.get()=='1234':
        messagebox.showinfo('Success','Login is successful')
        root.destroy()
        import ems
    else:
        messagebox.showerror('Error','wrong input')

root = CTk()
root.geometry('1100x780')
root.resizable(0, 0)
root.title('login page')
image= CTkImage(Image.open('cover.png'),size=(930,478))
imageLabel=CTkLabel(root,image=image, text='')
imageLabel.place(x=0,y=0)
headinglabel=CTkLabel(root,text='Employee Management System',font=('Goudy Old Style',20,'bold'),text_color='dark blue')
headinglabel.place(x=20, y=100)

usernameEntry= CTkEntry(root,placeholder_text='Enter your Username',width=180)
usernameEntry.place(x=50, y=150)

passwordEntry= CTkEntry(root,placeholder_text='Enter your Password',width=180,show='*')
passwordEntry.place(x=50, y=200)

loginButton=CTkButton(root, text='Login',cursor='hand2',command=login)
loginButton.place(x=70, y=250)

root.mainloop()

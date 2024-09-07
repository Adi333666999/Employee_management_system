from customtkinter import *
from PIL import Image
from tkinter import messagebox, ttk
import database

# Functon

def delete_all():
    result = messagebox.askyesno('Confirm', 'Do you really want to delete all records?')
    if result:
        database.deleteall_records()


def show_all():
    treeview_data()
    searchEntry.delete(0, END)
    searchBox.set('Search By')

def search_employee():
    if searchEntry.get() == '':
        messagebox.showerror('Error', 'Enter value to search')
    elif searchBox.get() == 'Search By':
        messagebox.showerror('Error', 'Please select option')
    else:
        searched_data = database.search(searchBox.get(), searchEntry.get())
        tree.delete(*tree.get_children())
        for employee in searched_data:
            tree.insert('', END, values=employee)


def delete_employee():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror('ERROR', 'Select data to delete')
    else:
        database.delete(idEntry.get())
        treeview_data()
        clear()
        messagebox.showerror('Error', 'Data deleted')

def update_employee():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror('ERROR', 'Select data to update')
    else:
        # Get selected ID
        selected_id = idEntry.get()  # Added this line

        database.update(selected_id, nameEntry.get(), phoneEntry.get(), roleBox.get(), genderBox.get(), salaryEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo('Success', 'Data updated')


def selection(event):
    selected_item = tree.selection()
    if selected_item:
        row = tree.item(selected_item)['values']
        clear()
        idEntry.insert(0, row[0])
        nameEntry.insert(0, row[1])
        phoneEntry.insert(0, row[2])
        roleBox.set(row[3])
        genderBox.set(row[4])
        salaryEntry.insert(0, row[5])


def clear(value = False):
    if value:
        tree.selection_remove(tree.focus())
    idEntry.delete(0, END)
    nameEntry.delete(0, END)
    phoneEntry.delete(0, END)
    roleBox.set('Web Developer')
    genderBox.set('Male')
    salaryEntry.delete(0, END)


def treeview_data():
    employees = database.fetch_employees()
    tree.delete(*tree.get_children())
    for employee in employees:
        tree.insert('', END, values=employee)

def add_employee():
    if idEntry.get() == '' or phoneEntry.get() == '' or nameEntry.get() == '' or salaryEntry.get() == '':
        messagebox.showerror('Error', 'All fields are required')
    elif database.id_exists(idEntry.get()):
        messagebox.showerror('Error', 'Id already exists')
    elif not idEntry.get().startswith('EMP'):
        messagebox.showerror('Error', "Invaild ID format. Use EMP followed by number (e.g. 'EMP1')")

    else:
        database.insert(idEntry.get(),nameEntry.get(),phoneEntry.get(), roleBox.get(),genderBox.get(),salaryEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo('Success', 'Data added')

# Initialize main window
window = CTk()
window.geometry('1100x780+50+50')
window.resizable(0, 0)
window.title('Employee Management System')
window.configure(fg_color='#161C30')

# Logo image
logo = CTkImage(Image.open('bg.PNG'), size=(930,158))
logoLabel = CTkLabel(window, image=logo, text='')
logoLabel.grid(row=0, column=0, columnspan=2)

# Left frame for form inputs
leftFrame = CTkFrame(window, fg_color='#161C30')
leftFrame.grid(row=1, column=0, padx=20, pady=20, sticky='n')

# Entry for ID
idLabel = CTkLabel(leftFrame, text='Id', font=('arial', 18, 'bold'), text_color='white')
idLabel.grid(row=0, column=0, padx=20, pady=15, sticky='w')
idEntry = CTkEntry(leftFrame, font=('arial', 18), width=180)
idEntry.grid(row=0, column=1)

# Entry for Name
nameLabel = CTkLabel(leftFrame, text='Name', font=('arial', 18, 'bold'), text_color='white')
nameLabel.grid(row=1, column=0, padx=20, pady=15, sticky='w')
nameEntry = CTkEntry(leftFrame, font=('arial', 18), width=180)
nameEntry.grid(row=1, column=1)

# Entry for Phone
phoneLabel = CTkLabel(leftFrame, text='Phone no', font=('arial', 18, 'bold'), text_color='white')
phoneLabel.grid(row=2, column=0, padx=20, pady=15, sticky='w')
phoneEntry = CTkEntry(leftFrame, font=('arial', 18), width=180)
phoneEntry.grid(row=2, column=1)

# ComboBox for Role
roleLabel = CTkLabel(leftFrame, text='Role', font=('arial', 18, 'bold'), text_color='white')
roleLabel.grid(row=3, column=0, padx=20, pady=15, sticky='w')
role_options = ['Web Developer', 'Cloud Architect', 'Network Engineer', 'Consultant', 'Data Scientist', 'Technical Writer', 'DevOps Engineer']
roleBox = CTkComboBox(leftFrame, values=role_options, width=180, font=('arial', 18), state='readonly')
roleBox.grid(row=3, column=1)
roleBox.set(role_options[0])

# ComboBox for Gender
genderLabel = CTkLabel(leftFrame, text='Gender', font=('arial', 18, 'bold'), text_color='white')
genderLabel.grid(row=4, column=0, padx=20, pady=15, sticky='w')
gender_options = ['Male', 'Female', 'Transgender']
genderBox = CTkComboBox(leftFrame, values=gender_options, width=180, font=('arial', 18), state='readonly')
genderBox.grid(row=4, column=1)
genderBox.set('Male')

# Entry for Salary
salaryLabel = CTkLabel(leftFrame, text='Salary', font=('arial', 18, 'bold'), text_color='white')
salaryLabel.grid(row=5, column=0, padx=20, pady=15, sticky='w')
salaryEntry = CTkEntry(leftFrame, font=('arial', 18), width=180)
salaryEntry.grid(row=5, column=1)

# Right frame for search and table
rightFrame = CTkFrame(window)
rightFrame.grid(row=1, column=1, padx=20, pady=20, sticky='n')

# ComboBox for search
search_options = ['Id', 'Name', 'Phone', 'Role', 'Gender', 'Salary']
searchBox = CTkComboBox(rightFrame, values=search_options, state='readonly')
searchBox.grid(row=0, column=0, padx=10, pady=10)
searchBox.set('Search By')

searchEntry = CTkEntry(rightFrame)
searchEntry.grid(row=0, column=1, padx=10, pady=10)

searchButton = CTkButton(rightFrame, text='Search', width=100, command=search_employee)
searchButton.grid(row=0, column=2, padx=10, pady=10)

showallButton = CTkButton(rightFrame, text='Show All', width=100, command=show_all)
showallButton.grid(row=0, column=3, padx=10, pady=10)

# Treeview for displaying data
tree = ttk.Treeview(rightFrame, height=13)
tree.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

tree['columns'] = ('Id', 'Name', 'Phone', 'Role', 'Gender', 'Salary')

for col in tree['columns']:
    tree.heading(col, text=col)
    tree.column(col, width=100)

tree.column('Id', width=72)
tree.column('Name', width=100)
tree.column('Phone', width=100)
tree.column('Role', width=200)
tree.column('Gender', width=100)
tree.column('Salary', width=100)

tree.config(show='headings')

# Styling for Treeview
style = ttk.Style()

style.configure('Treeview.Heading', font=('arial', 18, 'bold'))
style.configure('Treeview', font=('arial', 10, 'bold'), rowheight=20, background='#161C30', foreground='white')

scrollbar = ttk.Scrollbar(rightFrame,orient=VERTICAL, command = tree.yview)
scrollbar.grid(row=1, column=4, sticky='ns')

tree.config(yscrollcommand=scrollbar.set)


# Buttons frame
buttonFrame = CTkFrame(window, fg_color='#161C30')
buttonFrame.grid(row=2, column=0,columnspan=2, pady=10)

newButton = CTkButton(buttonFrame, text='New Employee', font=('arial', 15, 'bold'), width=160, command=lambda: clear(True))
newButton.grid(row=0, column=0, padx=5, pady=5)

addButton = CTkButton(buttonFrame, text='Add Employee', font=('arial', 15, 'bold'), width=160, command=add_employee)
addButton.grid(row=0, column=1, padx=5, pady=5)

updateButton = CTkButton(buttonFrame, text='Update Employee', font=('arial', 15, 'bold'), width=160, command=update_employee)
updateButton.grid(row=0, column=2, padx=5, pady=5)

deleteButton = CTkButton(buttonFrame, text='Delete Employee', font=('arial', 15, 'bold'), width=160, command=delete_employee)
deleteButton.grid(row=0, column=3, padx=5, pady=5)

deleteallButton = CTkButton(buttonFrame, text='Delete All', font=('arial', 15, 'bold'), width=160, command=delete_all)
deleteallButton.grid(row=0, column=4, padx=5, pady=5)

treeview_data()

window.bind('<ButtonRelease>', selection)

# Start the Tkinter event loop
window.mainloop()

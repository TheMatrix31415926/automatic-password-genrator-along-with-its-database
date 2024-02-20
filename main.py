from tkinter import messagebox
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    # Password Generator Project
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {
        "email": email,
        "password": password
    }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Opps", message="Please make sure you haven't left any field empty")
    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                                          f"\nPassword{password}\nIs it okay to save?")
    if is_ok:
        try:
            with open("database.json", "r") as data_file:
                # Reading
                data = json.load(data_file)

        except FileNotFoundError:
            with open("database.json", "r") as data_file:
                json.dump(new_data, data_file)
        else:
            data.update(new_data)

            with open("database.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# -------------------------FIND PASSWORD------------------------------ #
def find_password():
    website = website_entry.get()
    try:
        with open("database.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")

        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists")
# ---------------------------- UI SETUP ------------------------------- #


from tkinter import *

window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

canvas = Canvas(height=200, width=200)
logo_png = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_png)
canvas.grid(column=1, row=0)

website_label = Label(text="Website")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username")
email_label.grid(column=0, row=2)
password_label = Label(text="password")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "dewanshu9004@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Button
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)
add_search_button = Button(text="Search", width=13, command=find_password)
add_search_button.grid(row=1, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)
window.mainloop()

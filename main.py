import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)
    pass_entry.delete(0,END)
    pass_entry.insert(0, string=password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    password = pass_entry.get()
    email = email_entry.get()
    new_data = {website:{"email": email, "password": password}}
    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(titie= "Oops", message="Website or Password are empty")
    else:
        ok = messagebox.askokcancel(title=website_entry.get(), message=f"These are details entered: \n{email_entry.get()} \n"
                                                                       f"Password: {password}\nIs it ok to save?")
        if ok:
            with open("data.json","r") as f:
                data = json.load(f)
                data.update(new_data)

            with open("data.json", "w") as f:
                json.dump(data, f, indent=4)

            website_entry.delete(0,END)
            pass_entry.delete(0,END)
            website_entry.focus()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200,height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo)
canvas.grid(row=0,column=1)

website_lbl = Label(text="Website:")
website_entry = Entry(width=35)
website_lbl.grid(row=1,column=0)
website_entry.grid(row=1, column = 1,columnspan=2, sticky="EW")

email_lbl = Label(text="Email/Username:")
email_entry = Entry(width=35)
email_lbl.grid(row=2,column=0)
email_entry.grid(row=2, column=1,columnspan=2,sticky="EW")
website_entry.focus()
email_entry.insert(0,"benhamo.ken@gmail.com")

pass_lbl = Label(text="Password:")
pass_entry = Entry(width=21)
generate_pass = Button(text="Generate Password", command=generate_password)
pass_lbl.grid(row=3,column=0)
pass_entry.grid(row=3, column=1,sticky="EW")
generate_pass.grid(row=3,column=2)

add = Button(text="Add", width=36, command=save)
add.grid(row=4,column=1,columnspan=2,sticky="EW")

window.mainloop()
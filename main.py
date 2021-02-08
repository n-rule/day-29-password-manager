from random import *
from tkinter import *
from tkinter import messagebox

import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    # Password Generator Project

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)
    password = ''.join(password_list)
    pyperclip.copy(password)

    entry_password.delete(0, END)
    entry_password.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    if len(entry_website.get()) < 1 or len(entry_password.get()) < 1:
        messagebox.showwarning(title='ALARM ', message='Some fields are empty!')

    else:

        is_ok = messagebox.askokcancel(title='Password Manager', message='Is it ok to save?')

        if is_ok:
            with open('data.txt', 'a') as data:
                data.write(f'{entry_website.get()} | ')
                entry_website.delete(0, END)

                data.write(f'{entry_email.get()} | ')

                data.write(f'{entry_password.get()}\n')
                entry_password.delete(0, END)

        messagebox.showinfo(message='Credentials was saved successfully')


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column='1', row='0')

label_website = Label(text="Website : ")
label_website.grid(column='0', row='1', sticky='e')

label_email = Label(text="Email/Username : ")
label_email.grid(column='0', row='2', sticky='e')

label_password = Label(text="Password : ")
label_password.grid(column='0', row='3', sticky='e')

entry_website = Entry(width='53')
entry_website.grid(column='1', row='1', columnspan='2', sticky='w')
entry_website.focus()

entry_email = Entry(width='53')
entry_email.grid(column='1', row='2', columnspan='2', sticky='w')
entry_email.insert(0, 'rule@ukr.net')

entry_password = Entry(width='34')
entry_password.grid(column='1', row='3', columnspan='1', sticky='w')

button_generate = Button(text='Generate Password', command=generate_password, width='14')
button_generate.grid(column='2', row='3')

button_generate = Button(text='Add', command=save_password, width='45')
button_generate.grid(column='1', row='4', columnspan='2')

window.mainloop()

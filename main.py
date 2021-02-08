from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pass

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    with open('data.txt', 'w') as data:
        data.write()


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
button_generate.grid(column='1', row='4',columnspan='2')




window.mainloop()
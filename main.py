from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pass

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column='1', row='0')

label_website = Label(text="Website:")
label_website.grid(column='0', row='1', sticky='e')

label_email = Label(text="Email/Username:")
label_email.grid(column='0', row='2', sticky='e')

label_password = Label(text="Password:")
label_password.grid(column='0', row='3', sticky='e')

entry_website = Entry()
entry_website.grid(column='1', row='1', columnspan='2')

button_generate = Button(text='start', command=generate_password)
button_generate.grid(column='2', row='3')




window.mainloop()
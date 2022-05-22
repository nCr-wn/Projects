import tkinter
import string
import secrets

BLUE = '#30475E'
DARK_BLUE = '#222831'
GREY = '#DDDDDD'
RED = '#F05454'


class Generate:
    def __init__(self):
        self.pw = ''
        self.chars = ''
        self.default_length = 16

    # Check for values in checkboxes
    def set_chars(self):
        if special_char_var.get():
            self.chars += string.punctuation
        if letters_var.get():
            self.chars += string.ascii_letters
        if nums_var.get():
            self.chars += string.digits

    # Generate password / clear existing values in password and chars
    def password(self):
        self.reset()
        self.set_chars()

        # If input is empty -> default password length
        if length.get() == '':
            pass
        else:
            self.default_length = int(length.get())

        # Generate password if at least 1 checkbox is checked
        if len(self.chars) > 0:
            for i in range(self.default_length):
                self.pw += secrets.choice(self.chars)
            pw_label.config(text=self.pw)
        else:
            pass

    # Clear clipboard and copy password
    def copy(self):
        window.clipboard_clear()
        window.clipboard_append(self.pw)
        pw_label.config(text='Password copied!')

    # Clear screen, password output and checkbox options
    def reset(self):
        self.pw = ''
        self.chars = ''
        pw_label.config(text='')


window = tkinter.Tk()
window.config(background=DARK_BLUE, padx=100, pady=50)
window.minsize(height=250, width=500)
generate = Generate()

# UI
# Row 0 - Password output + copy
pw_label = tkinter.Label(text='', font=('Roboto', 14), background=DARK_BLUE, foreground=GREY, pady=25, width=35)
pw_label.grid(row=0, column=0, columnspan=2)

copy_pw = tkinter.Button(text="📋 Copy", font=('Roboto', 14, 'bold'), background=BLUE, foreground=GREY, command=generate.copy)
copy_pw.grid(row=0, column=2)

# Row 1 - Checkboxes / Options for password
special_char_var = tkinter.IntVar()
special_char = tkinter.Checkbutton(text='Special characters', font=('Roboto', 14, 'bold'), background=BLUE, foreground=GREY, selectcolor=DARK_BLUE, variable=special_char_var)
special_char.grid(row=1, column=0)

letters_var = tkinter.IntVar()
letters = tkinter.Checkbutton(text='Upper and lowercase', font=('Roboto', 14, 'bold'), background=BLUE, foreground=GREY, selectcolor=DARK_BLUE, variable=letters_var)
letters.grid(row=1, column=1)

nums_var = tkinter.IntVar()
nums = tkinter.Checkbutton(text='Numbers', font=('Roboto', 14, 'bold'), background=BLUE, foreground=GREY, selectcolor=DARK_BLUE, variable=nums_var, width=8)
nums.grid(row=1, column=2)

# Row 2 - User input
length = tkinter.Entry(width=15, font=('Roboto', 14, 'bold'))
length.grid(row=2, column=1)

length_label = tkinter.Label(text='Password length', font=('Roboto', 14, 'bold'), background=DARK_BLUE, foreground=GREY)
length_label.grid(row=2, column=0)

# Row 3 - Generate password
generate = tkinter.Button(text="Generate password", font=('Roboto', 14, 'bold'), background=BLUE, foreground=GREY, command=generate.password)
generate.grid(row=3, column=1, pady=50)

window.mainloop()

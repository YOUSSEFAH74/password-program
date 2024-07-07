import string
import random
from tkinter import*
import pyperclip

def deletePass():
    passwpedFild.delete(0,END)

def generator():
    small_alph = string.ascii_lowercase
    captal_alph = string.ascii_uppercase
    numbers = string.digits
    symples = string.punctuation
    total = small_alph + numbers + symples + captal_alph
    password_len = int(len_Box.get())
    if choice.get() == 1:
        passwpedFild.insert(0, random.sample(small_alph, password_len))
    if choice.get() == 2:
        passwpedFild.insert(0, random.sample(small_alph + captal_alph, password_len))
    if choice.get() == 3:
        passwpedFild.insert(0, random.sample(total, password_len))


def copy():
    pass1 = passwpedFild.get()
    pyperclip.copy(pass1)
    with open('text12' , 'w') as file:
        file.write(pass1)
    file.close()


window = Tk()
choice = IntVar()
Font = ('arial', 13, 'bold')
window.resizable(height = None, width = None)
window.config(bg='#4d4d4d')
passwordLabel = Label(window, text='Password generator:', font=('times new roman', 20, 'bold'), bg='#8f8978'
                      , fg='white' , height= 5 ,width= 20 )
passwordLabel.grid()
window.title('Password generator')
weekRadioButton = Radiobutton(window, text='Week', value=1, variable=choice, font=Font)
weekRadioButton.grid(pady=10)

mediumRadioButton = Radiobutton(window, text='Medium', value=2, variable=choice, font=Font)
mediumRadioButton.grid(pady=10)

strongRadioButton = Radiobutton(window, text='Strong', value=3, variable=choice, font=Font)
strongRadioButton.grid(pady=10)

lengthLabel = Label(window, text='Password  Length:', font=Font, bg='#8f8978'
                    , fg='white')
lengthLabel.grid()


len_Box = Spinbox(window, from_=5, to_=50, width=5, font=Font)
len_Box.grid(pady=6)


generateButton = Button(window, text='Generate', font=Font, command=generator)
generateButton.grid(pady=10)


passwpedFild = Entry(window, width=25, bd=2, font=Font)
passwpedFild.grid(pady=10)


copyButton = Button(window, text='Copy', font=Font, command=copy)
copyButton.grid(pady=10)


delButton = Button(window, text='delete', font=Font, command=deletePass)
delButton.grid(pady=10)


window.mainloop()

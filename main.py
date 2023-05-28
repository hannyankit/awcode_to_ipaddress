# code convert
"""
A UI will be there
 1. one input box
 2. Convert Button
 3. Clipboard feature

 Input : That will take the input of AWS code
    ip-10-234-567-89.ec2.internal

 output : 10.234.567.89:8890     # after all number at last Port will be there '8890'

 ## Logic
        remove all value from start till u find number
                1. First all number should be there
                2. se
        replace hyphen with dot
        atlast hard code ':8890'


"""
import win32clipboard
from tkinter import *

tk1 = Tk()
# width * Height
tk1.geometry('600x500')
tk1.minsize(200, 200)
tk1.title("Code Generator")
tk1.configure(background='#0096DC')

# CodeConvert( '  ip-01-900-789-00.ec2.internal   ')

l1 = Label(text="Code Generator", fg='black', bg='#0096DC', padx=63, pady=43, font=("verdana", "31"), borderwidth=3,
           relief=SUNKEN)
l1.pack(pady=(20, 10))

# Showing Label "Enter the Code"
input_label = Label(tk1, text='Enter the Code ', fg='white', bg='#0096DC')
input_label.pack(pady=10)
input_label.configure(font=('verdana', 14))

# Taking code input from User from Entry Box
data = StringVar()

code_input = Entry(tk1, textvariable=data, width=30)
code_input.pack(ipady=4)
code_input.configure(font=('verdana', 11))

# Main function
def CodeConvert():
    code = code_input.get()
    num_code_list = []
    list1 = code.split('.')

    code_list = list1[0].split('-')

    for i in code_list:
        if i.isdigit():
            num_code_list.append(str(int(i)))

    value = '.'.join(num_code_list)
    output = value + ':8890'

    empty_label.config(text='Output Code :  ' + output)
    return output

# Convert Button
convert_button = Button(tk1, text='Convert', bg='white', fg='green', width=10, height=2, font=("helvetica", 13),
                        command=CodeConvert)
convert_button.pack(pady=(10, 20))


empty_label = Label(tk1, fg='green', bg='white', font=('arial', 15))
empty_label.pack(pady=20)


def copy_to_clipboard():
    text = CodeConvert()
    tk1.clipboard_clear()  # clear the clipboard contents
    tk1.clipboard_append(text)  # append the text to the clipboard


# Create a button that copies a string to the clipboard when clicked
copy_button = Button(tk1, text="Copy Output", bg='white', fg='green', command= copy_to_clipboard)
copy_button.pack()

tk1.mainloop()

"""#converter - This is a program that will allow users to input whether they want to convert from decimal number to binary or vise versa.
it will then ask for that number that they want to convert, this is also going to incorporate a tkinter interface to make it look visually appealing
"""
import tkinter as tk

#binart to decimal
def binary():
    try:
        dnum = int(entry.get())
        binary = bin(dnum)
        result.config(text="your value in Binary is:" + (binary))
    except ValueError:
        result.config(text="Please enter a decimal value")
def decimal():
    try:
        bnum = entry.get()
        decimal = int(bnum, 2)
        result.config(text="your value in Decimal is:" + (decimal))
    except ValueError:
        result.config(text="Please enter a binary value")

con = tk.Tk()
con.title("Converter")

con_label = tk.Label(con, text="Enter a number to convert:")
con_label.grid(row=0, column=0)

entry = tk.Entry(con)
entry.grid(row=0, column=1)

button_frame = tk.Frame(con)
button_frame.grid()

binary_button = tk.Button(button_frame, text="Decimal to Binary", command=binary)
binary_button.grid(row=1, column=2)

decimal_button = tk.Button(button_frame, text="Binary to Decimal", command=decimal)
decimal_button.grid(row=2, column=2)

result = tk.Label(con, text="")
result.grid(row=1, column=1)

con.mainloop()
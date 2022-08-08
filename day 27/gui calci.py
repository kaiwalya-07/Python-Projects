from tkinter import *


def mil_to_km():
    miles = float(miles_inp.get())
    km = miles * 1.690
    km_rs.config(text=f"{km}")


window = Tk()
window.title("Miles to Km convertor")
window.config(padx=20, pady=20)

miles_inp = Entry(width=7)
miles_inp.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_eq = Label(text="is equal to")
is_eq.grid(column=0, row=1)

km_rs = Label(text="0")
km_rs.grid(column=1, row=1)

km_label = Label(text="km")
km_label.grid(column=2, row=1)

calci = Button(text="Calculate", command=mil_to_km)
calci.grid(column=1, row=2)

window.mainloop()

# Mile To Kilometer Converter GUI
import tkinter

window = tkinter.Tk()
window.minsize(width=350, height=100)
window.title("Miles to Kilometers convertor")
window.config(padx=75, pady=0)


def calculate():

    calculated_value["text"] = str(round(float(inp.get()) * 1.60934, 3))


inp = tkinter.Entry(width=10)
inp.insert(string="0", index=0)
inp.grid(row=0, column=1)
inp.focus()
mile_label = tkinter.Label(text="Mile")
mile_label.grid(row=0, column=2)

equal_to_label = tkinter.Label(text="Is equal to")
equal_to_label.grid(row=1, column=0)

calculated_value = tkinter.Label(text="0")
calculated_value.grid(row=1, column=1)

label_km = tkinter.Label(text="Km")
label_km.grid(row=1, column=2)

calculate_button = tkinter.Button(text="Calculate", command=calculate)
calculate_button.grid(row=3, column=1)

window.mainloop()

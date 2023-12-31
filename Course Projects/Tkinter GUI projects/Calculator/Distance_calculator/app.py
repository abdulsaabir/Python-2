import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

METER_TO_FEET = True

def Calculate():
    global METER_TO_FEET
    if METER_TO_FEET:
            try:
                value = float(input_value.get())
                result = value * 3.28084
                formatted_result = f'{result:.3f}'
                out_value.set(str(formatted_result))

            except:
                pass
    else:
        try:
            value = float(input_value.get())
            result = value / 3.28084
            formatted_result = f'{result:.3f}'
            out_value.set(str(formatted_result))
        except:
            pass


# IT SHOULD BE EXERCISE FOR THEM
def clear_the_value():
    input_value.set('')
    out_value.set('')

def switch_the_frame():
    global METER_TO_FEET
    if METER_TO_FEET:
        input_label.configure(text='Feet')
        output_label.configure(text='Meter')
        METER_TO_FEET = False
    else:
        input_label.configure(text='Meter')
        output_label.configure(text='Feet')
        METER_TO_FEET = True

    clear_the_value()


root = tk.Tk()
root.title("Distance Calculator")
root.resizable(False, False)
# root.iconbitmap('empty.ico')

frame = ctk.CTkFrame(root)
frame.grid(padx=10, pady=10, sticky="EW")

input_value = tk.StringVar()
out_value = tk.StringVar()

input_label = ctk.CTkLabel(frame, text="Metres:")
input_label.grid(column=0, row=0, sticky="W", ipadx=5)
input_entry = ctk.CTkEntry(frame, textvariable=input_value)
input_entry.grid(column=1, row=0, sticky="EW")
input_entry.focus()

output_label = ctk.CTkLabel(frame, text="Feet:")
output_label.grid(column=0, row=1, sticky="W", ipadx=5)
output_text = ctk.CTkLabel(frame, textvariable=out_value)
output_text.grid(column=1, row=1, sticky="EW")

calculate_the_result = ctk.CTkButton(
    frame,
    text="Calculate",
    command=Calculate
)
calculate_the_result.grid(column=0, row=2, columnspan=2, sticky="EW")

switch_the_metric = ctk.CTkButton(
    frame,
    text="Switch the Converseion",
    command=switch_the_frame
)
switch_the_metric.grid(column=0, row=3, columnspan=2, sticky="EW")

for child in frame.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()
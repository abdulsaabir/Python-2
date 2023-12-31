import customtkinter as ctk
import tkinter as tk



# text sizes
FONT = 'Calibri'
MAIN_TEXT_SIZE = 150
INPUT_FONT_SIZE = 26

# colors
GREEN = '#50BFAB'
WHITE = '#F2F2F2'
BLACK = '#1F1F1F'
LIGHT_GRAY = '#E8E8E8'
GRAY = '#D9D9D9'


    
   # window setup
root = ctk.CTk(fg_color=GREEN)
root.title('')
root.geometry('400x400')
root.resizable(False, False)

# root.iconbitmap('empty.ico')

root.columnconfigure(0, weight=1)
root.rowconfigure((0, 1, 2, 3), weight=1, uniform='a')




# teh result text 
main_font = ctk.CTkFont(family=FONT, size=MAIN_TEXT_SIZE, weight='bold')
result_text = ctk.CTkLabel(root, text='10', font=main_font, text_color=WHITE)
result_text.grid(column=0, row=0, rowspan=2, sticky='nsew')



# weight frame and it's widgets
weight_frame = ctk.CTkFrame(root,fg_color=WHITE)
weight_frame.grid(column=0, row=2, sticky='nsew', padx=10, pady=10)


# grid the weight frame 
weight_frame.rowconfigure(0, weight=1, uniform='b')
weight_frame.columnconfigure(0, weight=2, uniform='b')
weight_frame.columnconfigure(1, weight=1, uniform='b')
weight_frame.columnconfigure(2, weight=3, uniform='b')
weight_frame.columnconfigure(3, weight=1, uniform='b')
weight_frame.columnconfigure(4, weight=2, uniform='b')




font = ctk.CTkFont(family=FONT, size=INPUT_FONT_SIZE)
label = ctk.CTkLabel(weight_frame, text='75kg', text_color=BLACK, font=font)
label.grid(row=0, column=2)

# buttons
minus_button = ctk.CTkButton(weight_frame, text='-', font=font,text_color=BLACK, fg_color=LIGHT_GRAY, hover_color=GRAY,corner_radius=6)
minus_button.grid(row=0, column=0, sticky='ns', padx=8, pady=8)

plus_button = ctk.CTkButton(weight_frame, text='+', font=font,text_color=BLACK, fg_color=LIGHT_GRAY, hover_color=GRAY,corner_radius=6)
plus_button.grid(row=0, column=4, sticky='ns', padx=8, pady=8)

small_plus_button = ctk.CTkButton(weight_frame, text='+',font=font, text_color=BLACK, fg_color=LIGHT_GRAY, hover_color=GRAY,corner_radius=6)
small_plus_button.grid(row=0, column=3, padx=4, pady=4)

small_minus_button = ctk.CTkButton(weight_frame, text='-',font=font, text_color=BLACK, fg_color=LIGHT_GRAY, hover_color=GRAY,corner_radius=6)
small_minus_button.grid(row=0, column=1, padx=4, pady=4)                            





# height frame
height_frame = ctk.CTkFrame(root,fg_color=WHITE)
height_frame.grid(row=3, column=0, sticky='nsew', padx=10, pady=10)


# widgets
slider = ctk.CTkSlider(
    height_frame,
    button_color=GREEN,
    button_hover_color=GRAY,
    progress_color=GREEN,
    fg_color=LIGHT_GRAY,
    from_=100,
    to=250)
slider.pack(side='left', fill='x', expand=True, pady=10, padx=10)

output_text = ctk.CTkLabel(height_frame,text='1.70m', text_color=BLACK,font=ctk.CTkFont(family=FONT, size=INPUT_FONT_SIZE))
output_text.pack(side='left', padx=20)


root.mainloop()

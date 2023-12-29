import customtkinter as ctk
import tkinter as tk



def press_number(value):
    if len(display_nums) < 9:
        display_nums.append(str(value))
        full_number = ''.join(display_nums)
        result_string.set(full_number)

def press_math(value):
    global display_nums,full_operation

    current_number = ''.join(display_nums)

    if current_number:
        full_operation.append(current_number)
    
        # if equal is clicked 
        if value == '=':
            formula = ' '.join(full_operation) 
            result = eval(formula)
            # format the result
            if isinstance(result, float):
                if result.is_integer():
                    result = int(result)
                else:
                    result = round(result, 3)
                    # update data
            full_operation.clear()
            display_nums = [str(result)]

            # update my output
            result_string.set(result)
            formula_string.set(formula)
        
        # else math operation is clicked 
        else:
            full_operation.append(value)
            display_nums.clear()

            # update output
            result_string.set('')
            formula_string.set(' '.join(full_operation))

def press_opera(value):
    global display_nums
        
    # clear the output
    if value == 'AC':
        result_string.set(0)
        formula_string.set('')

        # clear the data
        display_nums.clear()
        full_operation.clear()

    if value == '∓':
        current_number = ''.join(display_nums)
        if current_number:
            # positive / negative
            if float(current_number) > 0:
                display_nums.insert(0, '-')
            else:
                del display_nums[0]
            inverted_value = ''.join(display_nums)
            result_string.set(inverted_value)
            formula_string.set('')

    if value == '%':
        if len(display_nums) > 0:
            # get the percentage number
            current_number = float(''.join(display_nums))

            percent_number = current_number / 100

            if isinstance(percent_number, float):
                percent_number = round(percent_number, 3)

            # update and output
            result_string.set(percent_number)
            formula_string.set('')

            # update the data
            display_nums = list(str(percent_number))



# sizes 
APP_SIZE = (383, 574)
MAIN_ROWS = 7
MAIN_COLUMNS = 4

# window colors 

BLACK = '#000000'
WHITE = '#EEEEEE'

calculator = ctk.CTk(fg_color=(BLACK))

calculator.geometry(f'{APP_SIZE[0]}x{APP_SIZE[1]}')
calculator.resizable(False, False)
calculator.title('')

# calculator.iconbitmap('emtpy.ico')

# grid layout
calculator.rowconfigure(list(range(MAIN_ROWS)), weight=1, uniform='a')        
calculator.columnconfigure(list(range(MAIN_COLUMNS)), weight=1, uniform='a')



# # create output labels
formula_string = ctk.StringVar(value='')
result_string = ctk.StringVar(value='0')

display_nums= []
full_operation=[]

ctk.CTkLabel(calculator, textvariable=formula_string, font=('Helvetica',32)).grid(row=0,column=0,
                        columnspan=4,sticky='SE',padx=10)

ctk.CTkLabel(calculator, textvariable=result_string, font=('Helvetica',70)).grid(row=1,column=0,
                        columnspan=4,sticky='E',padx=10)






NUM_POSITIONS = [
	{'num': '.', 'col': 2, 'row': 6, 'span': 1},
	{'num': '0', 'col': 0, 'row': 6, 'span': 2},
	{'num': '1', 'col': 0, 'row': 5, 'span': 1},
	{'num': '2', 'col': 1, 'row': 5, 'span': 1},
	{'num': '3', 'col': 2, 'row': 5, 'span': 1},
	{'num': '4', 'col': 0, 'row': 4, 'span': 1},
	{'num': '5', 'col': 1, 'row': 4, 'span': 1},
	{'num': '6', 'col': 2, 'row': 4, 'span': 1},
	{'num': '7', 'col': 0, 'row': 3, 'span': 1},
	{'num': '8', 'col': 1, 'row': 3, 'span': 1},
	{'num': '9', 'col': 2, 'row': 3, 'span': 1}
]

for number in NUM_POSITIONS:
    button = ctk.CTkButton(calculator,text=number['num'],font=('Helvetica', 32), corner_radius=0,fg_color='#D4D4D2',text_color='BLACK',hover_color='#efefed',    command=lambda num=number['num']: press_number(num))
    button.grid(row=number['row'],column=number['col'], columnspan=number['span'],sticky='NSEW',padx=0.5,pady=0.5)



MATH_POSITIONS = [
	{'symb': '÷', 'character': '/', 'col': 3, 'row': 2, 'span': 1},
	{'symb': '*', 'character': '*', 'col': 3, 'row': 3, 'span': 1},
	{'symb': '-', 'character': '-', 'col': 3, 'row': 4, 'span': 1},
	{'symb': '+', 'character': '+', 'col': 3, 'row': 5, 'span': 1},
	{'symb': '=', 'character': '=', 'col': 3, 'row': 6, 'span': 1},
]

for symbol in MATH_POSITIONS:
    button = ctk.CTkButton(calculator,text=symbol['symb'],font=('Helvetica', 32), corner_radius=0,fg_color='#FF9500',text_color='WHITE',hover_color='#ffb143', command= lambda sym = symbol['symb']: press_math(sym))
    button.grid(row=symbol['row'],column=symbol['col'], columnspan=symbol['span'],sticky='NSEW',padx=0.5,pady=0.5)


OPERATORS = [
	{'opera': 'AC', 'col': 0, 'row': 2, 'span': 1},
	{'opera': '∓', 'col': 1, 'row': 2, 'span': 1},
	{'opera': '%', 'col': 2, 'row': 2, 'span': 1},
]


for operator in OPERATORS:
    button = ctk.CTkButton(calculator,text=operator['opera'],font=('Helvetica', 32), corner_radius=0,fg_color='#505050',text_color='WHITE',hover_color='#686868', command= lambda opera = operator['opera']: press_opera(opera))
    button.grid(row=operator['row'],column=operator['col'], columnspan=operator['span'],sticky='NSEW',padx=0.5,pady=0.5)



calculator.mainloop()



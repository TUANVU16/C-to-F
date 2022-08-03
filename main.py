from tkinter import *
from tkinter.font import BOLD

def change_To_F():
    Celcius = float(C_input.get())
    F = round(Celcius*9/5 + 32)
    F_result_label.config(text=f"{F}")
    
window = Tk()
window.title("HEllo VU")
window.config(padx=20, pady=20)



C_input = Entry(width=40)
C_input.grid(column=1, row =0)


C_label = Label(text="(° C)")
C_label.grid(column=2, row =0)

equal_label = Label(text="イコール")
equal_label.grid(column=0, row =2)

F_result_label = Label(text="0",font=BOLD)
F_result_label.grid(column=1, row =1)

F_label = Label(text="(° F)")
F_label.grid(column=2, row =1)

calculate_button = Button(text="計算", command=change_To_F)
calculate_button.grid(column=1, row =2)


window.mainloop()
#!/bin/python3

from tkinter import *
import tkinter.messagebox

index_value=1
row_value=2
def add_task():
    global index_value,row_value
    value=task.get()
    if value == "":
        tkinter.messagebox.showinfo(title="OOPS!!!",message="You have not passed any task")
    else:
        var1 = IntVar()
        Checkbutton(screen, text=value, variable=var1).grid(row=row_value, column=1)
        row_value+=1
        lb.insert(index_value, value)
        index_value+=1
        task.delete(0,'end')

def reset_all():
    pass
screen=Tk()
screen.title("~~~~ To do list  ~~~~")
# screen.config(width=400,height=400,pady=10,padx=10)

# title=Label(text=' Enter the works')
# title.grid(row=0,column=0)

task=Entry()
task.focus()
task.grid(row=0, column=1,padx=5,pady=20)
text_one=Label(text=" Enter the task ")
text_one.grid(row=0,column=0,padx=5,pady=20)


adding_button=Button(text="Add",command=add_task)
adding_button.grid(row=1,column=0,padx=10,pady=20)
task.bind('<Return>', lambda event: add_task())

clear_button=Button(text="Reset",command=add_task)
clear_button.grid(row=1,column=1,padx=10,pady=20)
task.bind('<Return>', lambda event: add_task())

check_button=Button(text="Status",command=add_task)
check_button.grid(row=1,column=2,padx=10,pady=20)
task.bind('<Return>', lambda event: add_task())



# var1 =IntVar()
# Checkbutton(screen, text="Male", variable=var1).grid(row=4,column=0)

lb =Listbox(screen)

lb.grid(row=2,column=0)

screen.mainloop()

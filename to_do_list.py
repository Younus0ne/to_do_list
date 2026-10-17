#!/bin/python3

from tkinter import *
import tkinter.messagebox
from datetime import datetime as dt

time_slots=[]
post_time_slots=[]
post_time_slots_index=0

check_boxes=[]
check_boxes_clicked=[]

task_completed=0
index_value=1
index_value_for_time=1
row_value=3

def on_click(widget):
    info = widget.grid_info()
    row = info.get("row")
    col = info.get("column")
    is_clicked=check_boxes_clicked[row-3].get()
    if is_clicked == 1:
        time=dt.now().strftime("%I:%M %p")
        time_after = Label(text=f"{time}")
        time_after.grid(row=row, column=2)
        post_time_slots.append(time_after)
    #print(f"Clicked box at Row: {row}, Column: {col}, clicked value {is_clicked} ")

def add_task():
    global index_value,row_value,index_value_for_time,post_time_slots_index
    value=task.get()
    if value == "":
        tkinter.messagebox.showinfo(title="OOPS!!!",message=" 🤔 You have not passed any task")
    else:
        time = dt.now().strftime("%I:%M %p")
        var1 = IntVar()
        check_boxes_clicked.append(var1)
        chk=Checkbutton(screen, text=value, variable=var1)
        chk.config(command=lambda w=chk: on_click(w))
        chk.grid(row=row_value, column=0)
        time_ob=Label(text=f"{time}")
        time_ob.grid(row=row_value,column=1)
        row_value+=1
        post_time_slots_index+=1
        check_boxes.append(chk)
        time_slots.append(time_ob)
        index_value_for_time+=1
        task.delete(0,'end')

def reset_all():
    global index_value, row_value ,task_completed,index_value_for_time
    task_completed=0
    row_value=3
    check_boxes_clicked.clear()
    for i in time_slots:
        i.destroy()
    time_slots.clear()
    for i in post_time_slots:
        i.destroy()
    post_time_slots.clear()
    for i in check_boxes:
        i.destroy()
    check_boxes.clear()
    index_value=index_value_for_time = 1

def check_status():
    global task_completed
    if len(check_boxes_clicked) == 0:
        tkinter.messagebox.showinfo(title="Task status", message=f"To Do list is empty. 🫣 ")
    else:
        for i in check_boxes_clicked:
            if i.get() == 1:
                task_completed+=1
        if len(check_boxes_clicked) == task_completed:
            tkinter.messagebox.showinfo(title="Task status", message=f" 🥳 CONGRATULATIONS You have completed ALL tasks")
        else:
            tkinter.messagebox.showinfo(title="Task status", message=f"You have completed {task_completed} tasks. 🫡 ")
        task_completed=0

def delete_it():
    global index_value, row_value, task_completed,index_value_for_time
    try:
        index_of_task=lb.curselection()[0]
    except IndexError:
        tkinter.messagebox.showinfo(title="Option invalid", message=f"🤔 Select the task to delete. ")
    else:
        if  task_completed != 0 :
                    task_completed -= 1
        del check_boxes_clicked[index_of_task]
        check_boxes[index_of_task].destroy()
        del check_boxes[index_of_task]
        del time_slots[index_of_task]
        index_value -=1
        index_value_for_time-=1

screen=Tk()
screen.title("~~~~ To do list  ~~~~")

info="""*Type the task and cilck 'Add' or press Enter
*Select the task in the 'Task list' and cilck 'Delete' to delete the task
*Cilck the box of the task when it is done
*Click 'Status' to see your progress
*Click 'Reset' to restart the application"""
#tkinter.messagebox.showinfo(title="GUIDE",message=f"{info}")

text_one=Label(text=" Enter the task ")
text_one.grid(row=0,column=0,padx=5,pady=20)
task=Entry()
task.focus()
task.grid(row=0, column=1,padx=5,pady=20)

adding_button=Button(text="Add",command=add_task)
adding_button.grid(row=0,column=2,pady=20,padx=5)
task.bind('<Return>', lambda event: add_task())

clear_button=Button(text="Reset",command=reset_all)
clear_button.grid(row=0,column=3,padx=10,pady=20)

divider =Frame(screen, height=3, bg="black")
divider.grid(row=1, column=0, columnspan=4,sticky="ew", padx=10, pady=10)

tasks=Label(text="Task's")
tasks.grid(row=2,column=0,padx=10)
task_set_on=Label(text="Task set on")
task_set_on.grid(row=2,column=1,padx=10)
task_complete=Label(text="Task completed on ")
task_complete.grid(row=2,column=2,padx=10)

screen.mainloop()
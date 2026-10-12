#!/bin/python3

from tkinter import *
import tkinter.messagebox

check_boxes=[]
check_boxes_clicked=[]
task_completed=0
index_value=1
row_value=3
def add_task():
    global index_value,row_value
    value=task.get()
    if value == "":
        tkinter.messagebox.showinfo(title="OOPS!!!",message=" 🤔 You have not passed any task")
    else:
        var1 = IntVar()
        check_boxes_clicked.append(var1)
        chk=Checkbutton(screen, text=value, variable=var1)
        chk.grid(row=row_value, column=1)
        row_value+=1
        check_boxes.append(chk)

        lb.insert(index_value, value)
        index_value+=1
        task.delete(0,'end')

def reset_all():
    global index_value, row_value ,task_completed
    task_completed=0
    row_value=3
    check_boxes_clicked.clear()
    for i in check_boxes:
        i.destroy()
    check_boxes.clear()
    lb.delete(first=0,last=index_value)
    index_value = 1

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
    global index_value, row_value, task_completed
    try:
        index_of_task=lb.curselection()[0]
    except IndexError:
        tkinter.messagebox.showinfo(title="Option invalid", message=f"🤔 Select the task to delete. ")
    else:
        if check_boxes_clicked[index_of_task].get() ==1 and task_completed != 0 :
                    task_completed -= 1
        del check_boxes_clicked[index_of_task]
        check_boxes[index_of_task].destroy()
        del check_boxes[index_of_task]
        lb.delete(first=index_of_task, last=None)
        index_value -=1

screen=Tk()
screen.title("~~~~ To do list  ~~~~")

task=Entry()
task.focus()
task.grid(row=0, column=1,padx=5,pady=20)
text_one=Label(text=" Enter the task ")
text_one.grid(row=0,column=0,padx=5,pady=20)

adding_button=Button(text="Add",command=add_task)
adding_button.grid(row=1,column=0,padx=10,pady=20)
task.bind('<Return>', lambda event: add_task())

deleting_button=Button(text="Delete",command=delete_it)
deleting_button.grid(row=1,column=1,padx=10,pady=20)

clear_button=Button(text="Reset",command=reset_all)
clear_button.grid(row=1,column=2,padx=10,pady=20)

check_button=Button(text="Status",command=check_status)
check_button.grid(row=1,column=3,padx=10,pady=20)

lb =Listbox(screen)
lb.grid(row=2,column=0)

screen.mainloop()

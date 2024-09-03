from tkinter import *

root = Tk()
root.title("To Do List")
root.geometry("400x650+400+100")
root.resizable(False,False)

todolist = []

def openFile():
    try:
        global todolist
        with open("tasklist.txt","r") as file:
            tasks = file.readlines()
        for task in tasks:
            if task != "\n":
                todolist.append(task)
                listbox.insert(END,task)
    except:
        file = open("tasklist.txt","w")
        file.close()

def addTask():
    task = task_entry.get()
    task_entry.delete(0,END)

    if task != "":
        with open("tasklist.txt","a") as file:
            file.write(f"{task}\n")
        todolist.append(task)
        listbox.insert(END,task)

def deleteTask():
    global todolist
    task = str(listbox.get(ANCHOR))
    if task in todolist:
        todolist.remove(task)
        with open("tasklist.txt","w") as file:
            for task in todolist:
                file.write(f"{task}\n")
        listbox.delete(ANCHOR)

#icon
icon = PhotoImage(file="images/task.png")
root.iconphoto(False,icon)

#top bar
top = PhotoImage(file="images/topbar.png")
Label(root,image=top).pack()

dock = PhotoImage(file="images/dock.png")
Label(root,image=dock,bg="#32405b").place(x=30,y=25)

note = PhotoImage(file="images/task.png")
Label(root,image=note,bg="#32405b").place(x=30,y=25)

heading = Label(root,text="TO-DO LIST",font="arial 25 bold",bg="#32405b",fg="white")
heading.place(x=130,y=20)

#main function
frame = Frame(root,width=400,height=50,bg="white")
frame.place(x=0,y=180)

#task = StringVar()
task_entry = Entry(frame,width=18,font="arial 20",bd = 0)
task_entry.place(x=10,y=10)
task_entry.focus()

button = Button(frame,text="Add",width=6,height=1,font="arial 20",bg="#5a95ff",fg="#fff",bd=0,cursor="hand2",command=addTask)
button.place(x=300,y=0)

#listbox
frame1 = Frame(root,bd=3,width=700,height=280,bg="#32405b")
frame1.pack(pady=(160,0))

listbox = Listbox(frame1,font=("arial",12),width=40,height=16,bg="#32405b",fg="white",cursor="hand2",selectbackground="#5a95ff",bd=0)
listbox.pack(side=LEFT,fill=BOTH,padx=2)
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT,fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openFile()

#delete
delete = PhotoImage(file="images/delete.png")
Button(root,image=delete,bd=0,cursor="hand2",command=deleteTask).pack(side=BOTTOM,pady=15)



root.mainloop()
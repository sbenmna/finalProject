import tkinter as tk
from tkinter import ttk

def showTasks():
    category = categoryVar.get()
    taskListbox.delete(0, tk.END)  # Clear the listbox
    for task, is_done in tasks.get(category, []):
        status = "Done" if is_done else "Not Done"
        taskListbox.insert(tk.END, f"{task} - {status}")

def addTask():
    category = categoryVar.get()
    task = taskEntry.get()
    tasks.setdefault(category, []).append((task, False))
    showTasks()

def toggleTask():
    selected_task = taskListbox.curselection()
    if selected_task:
        index = selected_task[0]
        task, is_done = tasks[categoryVar.get()][index]
        tasks[categoryVar.get()][index] = (task, not is_done)
        showTasks()

def deleteTask():
    selected_task = taskListbox.curselection()
    if selected_task:
        index = selected_task[0]
        tasks[categoryVar.get()].pop(index)
        showTasks()

# Sample data structure to hold tasks
tasks = {
    "House": [("Clean the house", False), ("Do laundry", False)],
    "School": [("Finish homework", False), ("Study for exam", False)],
    "Gym": [("Workout for 30 minutes", False)]
}

# Create the main window
root = tk.Tk()
root.title("Task Manager Pro")

# Set window size
root.geometry("500x520")

# Category dropdown
categoryVar = tk.StringVar(root)
categoryVar.set("House")  # Set default category
categoryDropdown = ttk.Combobox(root, values=["House", "School", "Gym"], textvariable=categoryVar, font=("Arial", 12), justify="center")
categoryDropdown.pack(pady=(10, 0))

# Listbox to display tasks
taskListbox = tk.Listbox(root, font=("Arial", 12), selectbackground="#D9EDF7", selectforeground="black")
taskListbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Button to show tasks
showTasksButton = tk.Button(root, text="Show Tasks", command=showTasks, font=("Arial", 12), bg="#5BC0DE", fg="white")
showTasksButton.pack(pady=(0, 10))

# Entry to add tasks
taskEntry = tk.Entry(root, font=("Arial", 12))
taskEntry.pack(pady=(0, 10), fill=tk.BOTH, expand=True)

# Button to add task
addTaskButton = tk.Button(root, text="Add Task", command=addTask, font=("Arial", 12), bg="#5CB85C", fg="white")
addTaskButton.pack()

# Button to toggle task completion
toggleTaskButton = tk.Button(root, text="Toggle Task", command=toggleTask, font=("Arial", 12), bg="#F0AD4E", fg="white")
toggleTaskButton.pack(pady=(10, 0))

# Button to delete selected task
deleteTaskButton = tk.Button(root, text="Delete Task", command=deleteTask, font=("Arial", 12), bg="#D9534F", fg="white")
deleteTaskButton.pack(pady=(0, 20))

# Start the main event loop
root.mainloop()
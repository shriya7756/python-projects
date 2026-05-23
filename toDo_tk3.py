
# Main window
root = tk.Tk()
root.title("To-Do List")

# Input field for adding tasks
task_entry = tk.Entry(root, width=35)
task_entry.pack(pady=10)

# Add Task button
add_button = tk.Button(root, text="Add Task", width=20, command=add_task)
add_button.pack(pady=5)

# Complete Task button
complete_button = tk.Button(root, text="Complete Task", width=20, command=complete_task)
complete_button.pack(pady=5)

# Display Tasks button
display_button = tk.Button(root, text="Display Tasks", width=20, command=display_tasks)
display_button.pack(pady=5)

# Delete Task button
delete_button = tk.Button(root, text="Delete Task", width=20, command=delete_task)
delete_button.pack(pady=5)

# Quit button
quit_button = tk.Button(root, text="Quit", width=20, command=quit_app)
quit_button.pack(pady=5)

# Listbox to display tasks
task_listbox = tk.Listbox(root, width=35, height=10)
task_listbox.pack(pady=10)

# Run the application
root.mainloop()
```

### Step-by-Step Explanation

1. **Importing Tkinter**:  
   We import the `tkinter` module and the `messagebox` submodule to handle GUI elements and display messages to the user.

2. **Global Task List**:  
   We create a global list `task_list` to store all tasks. Each task added by the user is appended to this list.

3. **Adding Tasks (`add_task` function)**:  
   - The `task_entry.get()` retrieves the user input from the text field.
   - If the input is not empty, the task is added to `task_list`, the task is displayed, and the text field is cleared.
   - If the input is empty, a warning message is shown using `messagebox.showwarning`.

4. **Completing Tasks (`complete_task` function)**:  
   - This function gets the selected task from the `Listbox` using `task_listbox.curselection()`.
   - If a task is selected, it is removed from the `task_list` and the display is updated. If no task is selected, an error message is shown.

5. **Deleting Tasks (`delete_task` function)**:  
   - This function works similarly to the `complete_task` function but simply removes the selected task from the `task_list`.

6. **Displaying Tasks (`display_tasks` function)**:  
   - The `update_task_list()` function is called to display all tasks in the `Listbox`.

7. **Updating the Listbox (`update_task_list` function)**:  
   - This function clears the current tasks displayed in the `Listbox` and then inserts the updated `task_list`.

8. **Quitting the Application (`quit_app` function)**:  
   - The `root.quit()` function is used to terminate the application when the "Quit" button is clicked.

9. **Main GUI Window (`root`)**:  
   - We create the main window using `tk.Tk()` and give it a title.
   - Widgets such as buttons, text entry fields, and list boxes are added to the window with `.pack()` to organize them in the window.

10. **Buttons**:  
    - We create buttons for each function: Add Task, Complete Task, Display Tasks, Delete Task, and Quit. Each button is linked to its respective function.

11. **Listbox**:  
    - The `Listbox` widget displays all the tasks stored in `task_list`. When the user adds or deletes tasks, this list is updated.

12. **Main Loop (`root.mainloop()`)**:  
    - This starts the Tkinter event loop, keeping the window open and responding to user input until the user quits.

### Running the Application

Save the code in a `.py` file (e.g., `todo_list.py`) and run it using:

```bash
python todo_list.py
```

This will open a window where you can add tasks, complete them, display tasks, delete tasks, and quit the application.

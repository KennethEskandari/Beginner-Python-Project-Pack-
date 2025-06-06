tasks = []  # Fixed variable name

# Add A Task To Function
def add_task(description):
    tasks.append({'description': description, 'Completed': False}) 
    print("Task added successfully!")

# View Tasks
def view_tasks():
    if not tasks:
        print("Clear!")
        return
    for i, task in enumerate(tasks):  
        status = "Completed!" if task['Completed'] else "Not Completed!" 
        print(f"{i + 1}. {task['description']} - {status}") 

# Mark Task As Completed
def completed_task(index):
    if 0 <= index < (tasks):
        tasks[index]['Completed'] = True
        print("Task marked as completed successfully!")
    else:
        print("Invalid task number!")

# Delete Task
def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
        print("Task deleted successfully!")
    else:
        print("Invalid task number!")

        
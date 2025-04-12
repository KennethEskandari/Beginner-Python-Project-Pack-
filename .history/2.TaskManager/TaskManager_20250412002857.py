tasks = []  # Fixed variable name

# Add A Task To Function
def add_task(description):
    tasks.append({'description': description, 'Completed': False})  # Fixed variable name and spacing
    print("Task added successfully!")

# View Tasks
def view_tasks():
    if not tasks:
        print("Clear!")
        return
    for i, task in enumerate(tasks):  # Fixed loop syntax
        status = "Completed!" if task['Completed'] else "Not Completed!"  # Fixed key access and spacing
        print(f"{i + 1}. {task['description']} - {status}")  # Fixed formatting


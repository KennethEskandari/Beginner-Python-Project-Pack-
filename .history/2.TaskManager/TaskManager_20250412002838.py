task = []

#Add A Task To Function
def add_task(description):
    task.append({'description': description, 'Completed' : False})
    print("Task added successfully!")

#View Tasks 
def view_tasks():
    if not tasks:
        print("Clear!")
        return
    for i in task enumerate(tasks):
        status = "Completed!" if task ['Completed'] else "Not Completed!"
        print(f"{i+1}, {task['description']} {status}")


tasks = []

#Add A Task To Function
def add_task(description):
    tasks.append({'description': description, 'Completed' : False})
    print("Task added successfully!")

#View Tasks 
def view_tasks():
    if not tasks:
        print("Clear!")
        return
    for i in tasks enumerate(task):
        status = "Completed!" if tasks ['Completed'] else "Not Completed!"
        print(f"{i+1}, {tasks['description']} - {status}")


tasks = []

#Add A Task To Function
def add_task(description):
    tasks.append({'description': description, 'Done' : False})
    print("Task added successfully!")

def view_tasks():
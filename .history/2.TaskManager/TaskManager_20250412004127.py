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

# Save Tasks To File
def save_tasks(filename = 'tasks.txt'):
    with open(filename, 'w') as file:
        for task in tasks:
            line = f"{task['description']}||{task['completed']}\n"
            file.write(line)
        print("Tasks saved successfully!")

#Load Tasks
def load_tasks(filename = 'tasks.txt'):
    import os
    if not os.path.exists(filename):
        print("File not found!")
        return
    with open(filename,'r') as file:
        for line in file: 
            description, completed = line.strip().split('||')
            tasks.append({'description': description, 'completed': completed == 'True'})
        print("Tasks loaded successfully!")

# Main Function
def main():
    while True: 
        print("\nTask Manager Menu:")
        print("1. View Tasks")
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
        print("2. Add Task")
        print("3. Mark Task As Completed")
        print("4. Delete Task")
        print("5. Save Tasks")

        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            view_tasks()
        elif choice == '2':
            description = input("Enter task description: ")
            add_task(description)
        elif choice == '3':
            index = int(input("Enter task number to mark as completed: ")) - 1
            completed_task(index)
        elif choice == '4':
            index = int(input("Enter task number to delete: ")) - 1
            delete_task(index)
        elif choice == '5':
            save_tasks()
        else:
            print("Invalid choice! Please try again.")
        if input("Do you want to continue? (y/n): ").lower() != 'y':
            break

#Run It 
if __name__ == "__main__":
    load_tasks()
    main()
    save_tasks()
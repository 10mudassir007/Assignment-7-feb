# Initialize variables
task_description = ""
due_date = ""
priority = ""

# Prompt user to add a task
add_task = input("Do you want to add a task? (yes/no): ")

if add_task == 'yes':
    # Get task details
    task_description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    priority = input("Enter priority (urgent, important, less important): ")

    # Categorize the task based on priority
    if priority == 'urgent':
        print(f"Task added: {task_description} (Due: {due_date}) - This is an urgent task.")
    elif priority == 'important':
        print(f"Task added: {task_description} (Due: {due_date}) - This is an important task.")
    elif priority == 'less important':
        print(f"Task added: {task_description} (Due: {due_date}) - This is a less important task.")
    else:
        print("Invalid priority entered. Task not categorized.")
else:
    print("No task added. Exiting program.")

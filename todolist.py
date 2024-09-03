#create an empty list named tasks
tasks = []
#define a function to add a task
def addTask():
    task = input('Enter a new Task: ')
    tasks.append(task)
    print(f"Task: '{task}' added to the list.")
#define a function to list all tasks
def listTasks():
    if not tasks:
        print('There are no tasks currently')
    else:
        for i,task in enumerate(tasks):
            print(f"{i+1}. {task}")
#define a function to delete a task
def deleteTask():
    if not tasks:
        print('There are no tasks currently')
    else:
        listTasks()
        task = int(input('Enter the number of the task you want to delete: '))
        if task <= 0 or task > len(tasks):
            print('Invalid task number')
        else:
            del tasks[task-1]
            print(f"Task '{task}' deleted")
#call the functions
#check if module name is main or not.
if __name__ == '__main__':
    print("Welcome to the To-Do List App")

    while True:
        print("\n")

        print("What would you like to do?")
        print("1. Add a task")
        print("2. List all tasks")
        print("3. Delete a task")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            addTask()

        elif choice == "2":
            listTasks()

        elif choice == "3":
            deleteTask()

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")

    print("See you next time!")
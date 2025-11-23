# To Create To Do List Using Dict
d1 = {}

def add_task(task_id, task_description):
    d1[task_id] = task_description
    print(d1)

def remove_task(task_id):
    if task_id in d1:
        del d1[task_id]
    print(d1)

def view_tasks():
    print(d1)

def clear_tasks():
    d1.clear()
    print(d1)

def update_task(task_id, new_description):
    if task_id in d1:
        d1[task_id] = new_description
    print(d1)

def task_exists(task_id):
    print(task_id in d1) 

while True:

    choosed_option = int(input("\nChoose an option:\n1. Add Task\n2. Remove Task\n3. View Tasks\n4. Clear Tasks\n5. Update Task\n6. Check Task Existence\n7. Exit\n"))

    match choosed_option:
        case 1:
            task_id = input("Enter Task ID: ")
            task_description = input("Enter Task Description: ")
            add_task(task_id,task_description)
        case 2:
            task_id = input("Enter Task ID: ")
            remove_task(task_id)
        case 3:
            view_tasks()
        case 4:
            clear_tasks()
        case 5:
            task_id = input("Enter Task ID: ")
            new_description = input("Enter Task Description: ")
            update_task(task_id,new_description)
        case 6:
            task_id = input("Enter Task ID: ")
            task_exists(task_id)
        case 7:
            print("Exiting.....")
            break
        case _:
            print("Enter Number Again....")

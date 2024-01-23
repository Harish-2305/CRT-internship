import os
def add_task(tasks):
    while True:
        description=input("\nEnter the Task : ")
        if len(description)<3:
            print("Enetr the Valid task with min length of 3")
        else:
            break
    while True:
        due_date=input("Enter the due date in dd/mm/yyyy format: ")
        if due_date=="":
            print("The due date can't be empty, kindly enter the date:")
        else:
            try:
                date_check=due_date.split('/')
                if 1<=int(date_check[0])<=31:
                    if 1<=int(date_check[1])<=12:
                        if int(date_check[2])>=2024:
                            break
                        else:
                            print("\nenter valid date")
                    else:
                        print("\nenter valid date")
                else:
                    print("\nenter valid date")
            except:
                print("\nEnter only date not word or letters")
    status= "incomplete"
    while True:
        print("""Optios to set priority:
                   1.High
                   2.Medium
                   3.Low""")
        priority=input("Enter your choice >")
        priority_option=('1','2','3')
        if priority in priority_option:
            if priority == '1':
                priority_type="High"
                tasks.append({"description": description, "due_date": due_date, "priority": priority, "priority_type":priority_type,"status":status})
                print("\nTask added Successfully ")
                save_task_to_file(tasks,file_path)
                break
            elif priority == '2':
                priority_type="Medium"
                tasks.append({"description": description, "due_date": due_date, "priority": priority, "priority_type":priority_type,"status":status})
                print("\nTask added Successfully ")
                save_task_to_file(tasks,file_path)
                break
            elif priority == '3':
                priority_type="Low"
                tasks.append({"description": description, "due_date": due_date, "priority": priority, "priority_type":priority_type,"status":status})
                print("\nTask added Successfully ")
                save_task_to_file(tasks,file_path)
                break
            else:
                print("\nEnter the validt one!")


def view_task(tasks):
    if not tasks:
        print("\nNo task avalable")
    else:
        while True:
            print("""\nOptions to view Tasks:
                1.View all tasks
                2.View high priority tasks
                3.View medium priority tasks
                4.View low priority tasks""")
            view=input("Enter your choice >")
            view_tasks=('1','2','3','4')
            if view in view_tasks:
                if view == '1':
                    print("\nAll Tasks: ")
                    for index,task in enumerate(tasks,start=1):
                        print(f"{index}. {task['description']} - Due date: {task['due_date']} - priority: {task['priority_type']} - Status:{task['status']}")
                    break
                elif view == '2':
                    print("\nTasks with high priority:")
                    index=1
                    for task in tasks:
                        if task['priority']== '1':
                            print(f"{index}. {task['description']} - Due date: {task['due_date']} - Status:{task['status']}")
                            index+=1
                    if index==1:
                        print("No tasks are found with the High priority")
                    break
                elif view == '3':
                    print("\nTasks with Medium priority:")
                    for task in tasks:
                        index=1
                        if task['priority']=='2':
                            print(f"{index}. {task['description']} - Due date: {task['due_date']} - Status:{task['status']}")
                            index+=1
                    if index==1:
                        print("\nNo tasks are found with the Meduim priority")
                    break
                elif view == '4':
                    print("\ntasks with the low priority:")
                    index=1
                    for task in tasks:
                        if task['priority']=='3':
                            print(f"{index} . {task['description']} - Due date: {task['due_date']} - Status:{task['status']}")
                            index+=1
                    if index ==1:
                        print("\nNo tasks are found with the Low priority")
                    break
            else:
                print("\nEnter the valid choice !")


def delete_task(tasks):
    while True:
        if not tasks:
            print("\nNo tasks available! kindly add the tasks ")
            break
        else:
            print("\nAll tasks")
            for index,task in enumerate(tasks,start=1):
                print(f"{index}. {task['description']} - Due date: {task['due_date']} - priority: {task['priority_type']} - Status:{task['status']}")
            print("\nTo exit form deleting the tasks enter '0'")
            task_index=int(input("Choose the index of the task to delete > "))
            if 1<=task_index<=len(tasks):
                del tasks[task_index-1]
                save_task_to_file(tasks,file_path)
                print("\nTask deleted successfully")
                break
            elif task_index == 0:
                print("\nExiting form the deleting task process") 
                break
            else:
                print("\nEnter the valid task index !")

def complete_task(tasks):
    if not tasks:
        print("\nNo task available")
    else:
        while True:
            print("\nAll tasks:")
            for index,task in enumerate(tasks,start=1):
                print(f"{index}. {task['description']} - Due date: {task['due_date']} - priority: {task['priority_type']} - Status:{task['status']}")
            print("To exit from the marking completion option of task enter '0'.")
            task_index=int(input("Enter the task index to mark as the completed : "))
            if 1<=task_index<=len(tasks):
                if tasks[task_index-1]['status']=="completed":
                    print("\nThe task have already marked as completed")
                    print("Exiting from the option of marking tasks complete")
                    break
                else:
                    tasks[task_index-1]['status']="completed"
                    save_task_to_file(tasks,file_path)
                    print("\nTask has been marked as completed successfully! ")
                    break
            elif task_index == 0:
                print("\nExiting from the option of marking tasks complete")
                break
            else:
                print("\nEnter the valid index !")


def save_task_to_file(tasks,file_path):
    with open(file_path, 'w') as f:
        for task in tasks:
            f.write(f"{task['description']}|{task['due_date']}|{task['priority']}|{task['priority_type']}|{task['status']}\n")


def load_tasks_from_file(file_path):
    tasks=[]
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            for line in f:
                description, due_date, priority, priority_type, status=line.strip().split('|')
                tasks.append({"description": description, "due_date": due_date, "priority": priority, "priority_type":priority_type, "status":status})
    return tasks
             
                   
tasks=[]
file_path="todo_list_tasks.txt"
tasks=load_tasks_from_file(file_path)
print("TODO list ~ makes your task unforgettable ~")
while True:
    print(""" \nOptions:
            1.Add Task
            2.View Tasks
            3.Delete Tasks
            4.Mark task as complete
            5.Exit
            """)
    choice=input("Enter your choice >")
    if choice=='1':
        add_task(tasks)
    elif choice == '2':
        view_task(tasks)

    elif choice == '3':
        delete_task(tasks)
    elif choice == '4':
        complete_task(tasks)
        
    elif choice == '5':
    
        print("\nExisting the TO-DO list !!")
        break
    else:
        print("\nEnter the valid choice form option! ")
    

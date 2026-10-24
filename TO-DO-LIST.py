def store_task():
    task=[]
    print("-------T0-D0-LIST--------")
    number_of_task=int(input("enter how many task you want to add: "))
    for i in range(1,number_of_task+1):
        task_list=input(f"task {i} = ")
        task.append(task_list)
    print("your task are saved.....")
    while True:
        list_function=int(input("enter what you want to do? \n 1.ADD \n 2.DELETE \n 3.UPDATE \n 4.VIEW \n 5.EXIT/STOP \n"))
        if list_function==1:
            add=input("enter what you want to add: ")
            task.append(add)
            print("new task is added......")
        elif list_function == 2:
            delete= input("enter what you want too delete: ")
            if delete in task:
                task.remove(delete)
                print(delete,"is deleted for the task......")
            else:
                print("task not found...")
        elif list_function == 3:
            update=input("enter what you want to update: ")
            if update in task:
                updated=input("enter new task: ")
                ind=task.index(update)
                task[ind]=updated
                print(task)
            else:
                print("task is invalid....")
        elif list_function==4:
            print("to-do-list=",task)
        elif list_function==5:
            print("closing the program......")
            break
        else:
            print("invalid input")


store_task()
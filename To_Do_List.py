#a function that adds to the list
#a function to delete
#a function to print the tasks
#prepare the list

def add(new_task):
    tasks.append(new_task)
    print("new task added >-<")

def delete(del_task):
    tasks.pop(del_task-1)
    print("Task deleted.\nWell Done ^-^!")

def display(tasks):
    i=0
    while i<len(tasks):
        print(f"{i+1}.{tasks[i]}")
        i=i+1
def run_it():
    print("Now tell me, what do you like to do?")
    print("1.Add a new task!    2.I've finished a task ^0^  3.What's on my list?")
    operation=int(input())
    while operation==1 or operation==2 or operation==3:
        if operation==1:
            print("Let's Do It !!")
            new_task=input("Enter the task: ")
            add(new_task)
            break
        elif operation==2:
            print("Wow! you did a great job for sure!")
            del_task=int(input("Now tell me, what's the number of the task you finished?: "))
            delete(del_task)
            break
        elif operation==3:
            print("Here's your list, Sweetheart: ")
            display(tasks)
            break
    else:
        print("Ummm, guess you entered a wrong input ..'-'")
def other_ord():
    op=input("Any other orders?: ")
    if op.lower()=="yes":
        run_it()
        return True
    elif op.lower()=="no":
        print("Ok cutie! That's all ^3^")
        return False
    else:
        print("ummm, sorry? guess that was wrong")
        other_ord()
        return True
tasks=[]
print("* * * Welcome to your cute To-Do list \>o</ * * *\n")
run_it()
other_ord()
while True:
    if not other_ord():
        break
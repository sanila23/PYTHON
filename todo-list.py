print("**MY TO-DO LIST**")
print("\n 1.Add an element:\n 2.Delete an element: \n 3.Exit.")

def mylist(todo_list):
    print("TO DO LIST")
    print()
todo_list=[]
runing=True
while runing:
    user=int(input("\nEnter your choice:"))
    if user==1:
        new=input("Enter new element TO-DO:").lower()
        print(f"\nyour current to-do list is.")
        mylist(todo_list)
        todo_list.append(new)
        print(todo_list)
    elif user==2:
        while True:
            itemName=input("\n Enter the element to delete:")
            if itemName in todo_list:
                    choice=input(f"\n Are you sure you want to delete {itemName} from TO-DO List?(y/n):")
                    if choice=="y":
                        todo_list.remove(itemName)
                        print("your updated todo list is:")
                        mylist(todo_list)
                        print(todo_list)
                        break

            else:
                    print("element not found")

    elif user==3:
        ask=input("\nAre you sure you want to exit?(y/n):")
        if ask=="y":
            runing=False
    else:
            print("invalid choice!!")
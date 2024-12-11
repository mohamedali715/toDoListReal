
#Name of program: to do list
#My name: Mohamed Ali
#description:shows a menu allowing you to add and remove items from your to do list and also prints and resets the list at the users command until they quit the program
#date program was finished: 12/10/2024

#toDoList holds a list of strings representing to do items
toDoList = [] #list for our to do items
def save_list():
    """
    save_list saves your list data when you quit the program
    :return: nothing
    """
    global toDoList
    with open("data.txt.", "w") as file:
        file.writelines(item + "\n" for item in toDoList)

def load_list():
    """
    load_list loads the data saved by the save_list function
    :return: nothing is returned
    """
    global toDoList
    with open("data.txt", "r") as file:
        toDoList = [line.strip() for line in file]
#adds task to list
def add_item(item):
    """
    add_item adds item to the end of the to do list
    :param item: item - a string containing the task to  be added
    :return: nothing is returned
    """
    toDoList.append(item) #adds task to to do list and tells user
    print("task added")
def remove_item():
    """
    remove_item lists out the toDoList so user can remove one of the tasks
    after getting input from the user and after checking if the number inputed is on
    the toDoList and that the toDoList is not empty, you can quit by pressing q
    :return: nothing is returned
    """
    print("Your current list:")
    if toDoList: #checks if list is empty if soo the rest of the code wont run
        for c in range(0, len(toDoList)):
            print(str(c + 1) + ". " + toDoList[c])
    else:
        print("list is empty")
        show_menu()
    while True: #loops so user can remove multiple tasks
        #choice holds a string of user input thats supposed to be either a number on the list or q
        choice = input("which one to remove or q to quit ")
        if choice == "q": #checks if user inputs q so it can quit
            break
        if choice.isdigit()==True: #checks if input is a number if so the rest of the code will run
            choice = int(choice) - 1
            if choice >= len(toDoList) or int(choice) < 0:  # checks if number is on the list
                print("invalid choice")
            else:
                toDoList.pop(choice) #after checking if the input is on the list it will remove the task
                print("item removed")
                for c in range(0, len(toDoList)):
                    print(str(c + 1) + ". " + toDoList[c])

        else:
            print("invalid choice")



    print("task removed")
def reset_list():
    """
    reset_list resets the to do list
    :return: nothing is returned
    """
    toDoList.clear() #
    print("list cleared")






def print_list():
    """
    print_list prints the to do list as long as its not empty if its empty it will inform the user
    :return: nothing is returned
    """
    if toDoList:
        for c in range(0, len(toDoList)):
            print(str(c + 1) + ". " + toDoList[c])
    else:
        print("The list is currently empty.")
def show_menu():
    """
    show_menu shows the menu that allows the user to add and remove items from the toDoList
    also allows you to reset and print the the toDoList and you can quit by pressing q
    :return: nothing is returned
    """
    while True:
        print("press 1 to add task to list")
        print("press 2 to remove task from list")
        print("press 3 to reset list")
        print("press 4 to print your list")
        print("press q to exit")
        #A string of user input
        l = input("")
        if l == "1":
            l = input("Enter task to add ")
            add_item(l)
        elif l == "2":
            remove_item()
        elif l == "3":
            reset_list()
        elif l == "4":
            print_list()
        elif l == "q":
            save_list()
            print("bye!")
            break
        else:
            print("That is not one of the options")


#main
load_list()
show_menu()
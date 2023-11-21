tasks = []

while True:
     userInput = input("Enter a command (add, remove, view, exit): ").lower()

     if userInput == "add":
          task = input("Enter the name task: ")
          tasks.append(task)
          print("The task added. ")

     elif userInput == "remove":
          if not tasks:
               print("There are no tasks!")
          else:
               task = input("Enter the name task to remove: ")
               if task in tasks:
                    tasks.remove(task)
                    print("The task removed.")   
               else:
                    print("The tasks not found!")      
     elif userInput == "view":
          if not tasks:
               print("There are no tasks!")
          else:
               for element in tasks:
                print(element) 

     elif userInput == "exit":
               toExit = input("Are you sure to exit! (yes/no) ").lower()
               if toExit == "yes":
                    break
     else:
          print("Invalid choice!! Please try again")          
               



    
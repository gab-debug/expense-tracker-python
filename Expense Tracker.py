import os
import json

if not os.path.exists("expenses.json"):      # To create the file automatically if it hasn't been created
    with open("expenses.json", "w") as file:
        json.dump([], file)
        
with open("expenses.json", "r") as file:     # To open the created file
    expenses = json.load(file)
print("\nWelcome to the Expense Tracker! You can add your expenses and view them anytime. select 1 to add an item, 2 to view expenses, and 3 to exit the program.")
while True:
    print("\n1. Add an item")
    print("2. View expenses")
    print("3. Exit")
    try:
        
        choice = int(input("What do you want to do?   "))

        if choice == 1:
            item = input("Enter item: ")
            amount = float(input("Enter amount: "))
            new_expense = {
                "item": item, 
                "amount": amount
            }
            expenses.append(new_expense)     

            with open("expenses.json", "w") as file: # ensures each entry is saved to the json file
                json.dump(expenses, file, indent=4)

        elif choice == 2:
            print(expenses)

        elif choice == 3:
            break

        else:
            print("\nInvalid choice!! You have to choose 1, 2 or 3")    
    
    except ValueError:                                # to handle the the input error of the user
        print("\nInvalid input!")
# Imports
import json # Need for storing our data
import datetime # Track when transactions happen
import os # Checking if files exist, create directories
from collections import defaultdict  #Greate for grouping data by catergory

# Helper/ utility functions
def show_menu():
    print("\n==== Budget Tracker ===")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View All Transactions")
    print("4. View Balance")
    print("5. Spending by Category")
    print("6. Monthly Summary")
    print("7. Exit")

def load_trans():
    try:
        with open("budget_trx.json", "r") as file:
             return json.load(file)
    except FileNotFoundError :
        return []
    except json.JSONDecodeError:
        return []
    
def save_trans(trans):
    with open("budget_trx.json", "w") as file:
        json.dump(trans, file, indent=4)

# Feature functions 
def add_income():
    try: 
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("Amount must be positive!")
            return 
    except ValueError:
            print("Please enter a valid number!")
            return
    category = input("Enter category (salary/gift/sale/other): ")
    description = input("Enter description: ")
    today = str(datetime.date.today())
    new_transaction = {
                "amount": amount ,
                "category": category,
                "type": "income",
                "date": today,
                "description": description
            }
    trans = load_trans()
    trans.append(new_transaction)
    save_trans(trans)
    print("Income added successfully!")

def add_expense():
     try: 
        amount = float(input("Enter amount: "))
        if amount <= 0:
             print("Amount must be positive!")
             return 
     except ValueError:
             print("Please enter a valid number!")
             return
     category = input("Enter category (food/gas/housing/utility/other): ")
     description = input("Enter description: ")
     today = str(datetime.date.today())
     new_transaction = {
                "amount": amount ,
                "category": category,
                "type": "expense",
                "date": today,
                "description": description
            }
     trans = load_trans()
     trans.append(new_transaction)
     save_trans(trans)
     print("Expense added successfully, sadly!")


     

# Main Function

def main():
   

    while True:
        show_menu()
        choice = input("\nChoose Option: ")

        if choice == "1":
            add_income()
        elif choice == "2":
             add_expense()
        elif choice == "3":
            print("Coming soon!")
        elif choice == "4":
            print("Coming soon!")
        elif choice == "5":
            print("Coming soon!")
        elif choice == "6":
            print("Coming soon!")
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-7.")
           


if __name__ == "__main__":
    main()
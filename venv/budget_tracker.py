# Imports
import json # Need for storing our data
import datetime # Track when transactions happen
import os # Checking if files exist, create directories
from collections import defaultdict  #Greate for grouping data by category

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


### Feature functions ###

# add_transaction
def add_transaction(transaction_type):
     try: 
        amount = float(input("Enter amount: "))
        if amount <= 0:
             print("Amount must be positive!")
             return 
     except ValueError:
             print("Please enter a valid number!")
             return
     if transaction_type == "income":
          valid_categories = ["salary", "gift","sale", "other" ]
          catergory_prompt = "Enter category (salary/gift/sale/other): "
     else: 
          valid_categories = ["food","gas", "housing", "utility", "other"]
          catergory_prompt = "Enter category (food/gas/housing/utility/other): "

     category = input(catergory_prompt)
     if category not in valid_categories:
          print(f"Invalid category. Please choose from: {', '.join(valid_categories)}")
          return
     
     description = input("Enter description: ")
     today = str(datetime.date.today().strftime("%m/%d/%Y"))
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

     transaction_type_display = "Income" if transaction_type == "income" else "Expense"
     print(f"{transaction_type_display} added succesfully")

# view all transactions

def view_all_trans():
    transactions = load_trans()

    if not transactions:
        print("No transactions found.")
        return
    
    print("\n=== All Transactions ===")
    print(f"{'Date':<12} {'Type':<10} {'Category':<15} {'Amount':<10} {'Description'}")
    print("-" * 70)

    # sort transaction by date asc
    sorted_transactions = sorted(transactions, key=lambda x: x['date'], reverse=True)

    for transaction in sorted_transactions:
        amount = f"${transaction['amount']:.2f}"
        transaction_type = transaction['type'].capitalize()
        print(f"{transaction['date']:<12} {transaction_type:<10} {transaction['category']:<15} {amount:<10} {transaction['description']}")

    print("-" * 70)
    print(f"Total transactions: {len(transactions)}")

# view_balance
def view_balance():
    transactions = load_trans()

    if not transactions: 
        print("No transactions found.")
        return
    total_income = sum(transaction['amount'] for transaction in transactions if transaction['type'] == 'income' )
    total_expenses = sum(transaction['amount'] for transaction in transactions if transaction['type'] == 'expense' )

    balance = total_income - total_expenses

    print("\n=== Balance Summary ===")
    print(f"Total Income: ${total_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Current Balance: ${balance:.2f}")

# transaction_types
def add_income():
    add_transaction("income")

def add_expense():
     add_transaction("expense")

     

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
             view_all_trans()
        elif choice == "4":
            view_balance()
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
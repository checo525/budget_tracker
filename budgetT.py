import json

# Add expenses description and amount into the list [expenses]
def add_expenses(expenses, description, amount):
    expenses.append({"description": description, "amount": amount})
    print(f"\nAdded Expenses: {description} Amount: {amount}")

# Get the remaining balance
def get_balance(budget, expenses):
    return budget - total_expenses(expenses)


# Add up the expenses
def total_expenses(expenses):
    sum = 0
    for expense in expenses:
        sum += expense["amount"]
    return sum

# Show the budget details, expenses, total spent, and remaining budget
def budget_details(budget, expenses):
    print(f"💲Total Budget: {budget}")
    print("Expenses: ")
    for expense in expenses:
        print(f"◽{expense['description']}: {expense['amount']}")
    print(f"➖Total spent: {total_expenses(expenses)}")
    print(f"💲Remaining budget: {get_balance(budget, expenses)}") 

def load_budget_data(filepath):
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data["budget"], data["expenses"]
    except (FileNotFoundError, json.JSONDecodeError):
        return 0, [] # return default values if the file already exists or is empty

def save_budget_details(filepath, budget, expenses):
    data = {
        'budget': budget,
        'expenses' : expenses
    }
    with open (filepath, 'w') as file:
        json.dump(data, file, indent=3)

def main():
    print("Welcome to this budget app\n")
    filepath = "budget_data.json" # defines the path to JSON file
    budget, expenses = load_budget_data(filepath)

    if budget == 0:
        budget= float(input("Enter your budget: "))
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Add an expense")
        print("2. Show your budget details")
        print("3. Exit the app\n")
        option = input("Enter what you would like to do (1, 2, 3): ")

        if option == "1":
            description = input("Enter expense description: ")
            amount = float(input("Enter the amount of the expense: "))
            add_expenses(expenses, description, amount)
        elif option == "2":
            budget_details(budget, expenses)
        elif option == "3":
            save_budget_details(filepath, budget, expenses)
            print("Exiting the app, Goodbye!")
            break
        else:
            print("Invalid option, please choose a valid option (1, 2 or 3)")

#allows code to run only when the script is executed, not when it’s imported.
if __name__ == "__main__":
    main()
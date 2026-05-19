def menu():
    print('========================\n' \
    'Expense Tracker\n'
    '========================\n' \
    '1. Add Expense\n' \
    '2. View Expenses\n' \
    '3. Save To File\n' \
    '4. Load From File\n' \
    '5. Exit')
    choice = input('Enter your choice: ').capitalize()
    return choice

def add_expense(expenses_list: list):
    expenses_data = dict()
    try:
        name = input('Enter the Name of the Expense: ')
        category = input('Enter the Category of the Expense: ')
        amount = input('Enter the Amount of the Expense: ')
        expenses_data['Name'] = name.capitalize()
        expenses_data['Category'] = category.capitalize()
        expenses_data['Amount'] = float(amount)
        expenses_list.append(expenses_data)
    
    except ValueError:
        print('Invalid input. Please enter a valid number for the Amount')
    return expenses_data

def view_expenses(expenses_list: list):
    print('Viewing Expenses: ')
    if len(expenses_list) < 1:
        print('No Expenses to Show')
    for expense in expenses_list:
        print(f"{expense['Category'].ljust(15)}| {expense['Name'].ljust(15)}| {expense['Amount']}")

def save_file(choice, expenses_list: list):
    choice = input('Do you want to Save in a New File? (Y/n): ').capitalize()
    if choice == 'Y':
        create_file = input('Enter the name of The File to Save: ')
        with open(create_file, 'w') as file:
            for expense_data in expenses_list:
                file.write(f"{expense_data['Category'].ljust(15)}| {expense_data['Name'].ljust(15)}| {expense_data['Amount']}\n")
    elif choice == 'N':
        with open('expenses.txt', 'w') as file:
            for expense_data in expenses_list:
                file.write(f"{expense_data['Category'].ljust(15)}| {expense_data['Name'].ljust(15)}| {expense_data['Amount']}\n")

def load_file(expenses_list: list):
    print('Loading expenses from File: ')
    expenses_list.clear()
    try:
        with open('expenses.txt', 'r') as file_handle:
            for line in file_handle:
                parts = line.strip().split('|')
                if len(parts) == 3:
                    category = parts[0].strip()
                    name = parts[1].strip()
                    amount = float(parts[2].strip())
                    expenses = {'Category': category, 'Name':name, 'Amount':amount}
                    expenses_list.append(expenses)
    except FileNotFoundError:
        print('No File Found. Please Save Your Expenses to File First')
expenses_list = list()
while True:
    choice = menu()
    if choice == '1' or choice == 'Add':
         expenses_data = add_expense(expenses_list)
    elif choice == '2' or choice == 'View':
        view_expenses(expenses_data, expenses_list)
    elif choice == '3' or choice == 'Save':
        save_file(choice)
    elif choice == '4' or choice == 'Load':
        load_file(choice)
    elif choice == '5' or choice == 'Exit':
        exit()
    else:
        print('Invalid choice. Try Again')
        continue
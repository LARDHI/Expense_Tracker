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

def add_expense(choice, lst: list):
    expenses = dict()
    try:
        name = input('Enter the Name of the Expense: ')
        category = input('Enter the Category of the Expense: ')
        amount = input('Enter the Amount of the Expense: ')
        expenses['Name'] = name.capitalize()
        expenses['Category'] = category.capitalize()
        expenses['Amount'] = float(amount)
        lst.append(expenses)
    
    except ValueError:
        print('Invalid input. Please enter a valid number for the Amount')
    return expenses

def view_expenses(choice, expenses: dict, lst: list):
    print('Viewing Expenses: ')
    if len(expenses) < 1:
        print('No Expenses to Show')
    for expense in lst:
        print(f"{expense['Category'].ljust(15)}| {expense['Name'].ljust(15)}| {expense['Amount']}")

def save_file(choice):
    choice = input('Do you want to Save in a New File? (Y/n): ').capitalize()
    if choice == 'Y':
        create_file = input('Enter the name of The File to Save: ')
        with open(create_file, 'w') as file:
            for expense in lst:
                file.write(f"{expense['Category'].ljust(15)}| {expense['Name'].ljust(15)}| {expense['Amount']}\n")
    elif choice == 'N':
        with open('expenses.txt', 'w') as file:
            for expense in lst:
                file.write(f"{expense['Category'].ljust(15)}| {expense['Name'].ljust(15)}| {expense['Amount']}\n")

#def load_file(choice):
lst = list()
while True:
    choice = menu()
    if choice == '1' or choice == 'Add':
         expense = add_expense(choice, lst)
    elif choice == '2' or choice == 'View':
        view_expenses(choice, expense, lst)
    elif choice == '3' or choice == 'Save':
        save_file(choice)
#    elif choice == '4' or choice == 'Load':
#        load_file(choice)
    elif choice == '5' or choice == 'Exit':
        exit()
    else:
        print('Invalid choice. Try Again')
        continue

'''
Landon Pack
IS 303 - A03

Expense Tracker program-

I will create a program that allows a business to enter and log their expenses before filtering and processing the data.


Inputs:
-Business name
-Expense in dollars
-Category of the expense

Processes:
- Input validation to ensure that the expense is in dollars
- Input validation to ensure that the category is valid
- Input validation to ensure the user typed yes or no to add more items
- Accumulator to track the total amount of expenses
- Filter to separate the expenses into categories
- Min/Max to find the greatest expense
- Filter all expenses over $200 into an expensive purchase category

Outputs:

- A report telling the user how many expenses they had, their most expensive expense, and how many expensive purchases they made



'''


# Inputs

business = input("Welcome! Please enter the name of your business: ").title()

print(f"Welcome {business} to the expense tracker program.")
user_input = ""

expenses = []
expense_total = 0
number_of_expenses = 0
# input validation to ensure expense is in dollars
while user_input != "no":
    expense = input("Please enter your expense amount in dollars: ")
    expense_check = expense.replace(".", "")
    while expense_check.isdigit() == False:
        print("Error: Please enter an amount in dollars: ")
        expense = input("Please enter your expense amount in dollars: ")
        expense_check = expense.replace(".", "")
        if expense_check.isdigit():
            break
    expense = float(expense)
    expense_total = expense_total + expense
    number_of_expenses += 1
    

# input validation to ensure the category is valid
    category = input("Please enter the category of your expense (business, leisure, food, travel): ").lower()
    while category not in ("business", "leisure", "food", "travel"):
        print("Error: Please enter one of the following categories (business, leisure, food, or travel)")   
        category = input("Please enter the category of your expense (business, leisure, food, travel): ").lower()
    expenses.append({"expense": expense, "category": category})
# input validation to ensure the user typed yes or no
    user_input = input("Would you like to add another expense? (yes or no): ")
    while user_input != "yes" and user_input != "no":
        print("Error: Please enter yes or no")
        user_input = input("Would you like to add another expense? (yes or no): ")

# filter to separate into categories
leisure_count = 0
business_count = 0
food_count = 0 
travel_count = 0
for expense in expenses:
    if expense['category'] == "food":
        food_count += 1
    elif expense['category'] == "travel":
        travel_count += 1
    elif expense['category'] == "business":
        business_count += 1
    elif expense['category'] == "leisure":
        leisure_count += 1


# min/max to find the greatest expense
if len(expenses) > 0:
    greatest_expense = expenses[0]
    for expense in expenses:
            if expense['expense'] > greatest_expense['expense']:
                greatest_expense = expense



expensive_purchases = []
for expense in expenses:
    if expense['expense'] > 200:
        expensive_purchases.append(expense)

# outputs
        
print(f"--- Expense Report for {business} ---")
print("Expense Breakdown:")
print(f"You had {number_of_expenses} different expenses")
print(f"{'Expenses by category':<25}")
print(f"{'Travel expenses:':<25} {travel_count}")
print(f"{'Business expenses:':<25} {business_count}")
print(f"{'Food expenses:':<25} {food_count}")
print(f"{'Leisure expenses:':<25} {leisure_count}")
print(f"{'Total expenses:':<25} ${expense_total:.2f}")
if len(expenses) > 0:
    print(f"{'Your greatest expense was:':<25} ${greatest_expense['expense']:.2f} in the category of {greatest_expense['category']}")
else:
    print("You had no expenses.")
print(f"You had {len(expensive_purchases)} expensive purchases over $200")






    

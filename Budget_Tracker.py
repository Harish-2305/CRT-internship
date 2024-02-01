import os
def add_income(budget):
    global income
    global amount
    if not budget:
        income=0
    else:
        for index,task in enumerate(budget):
            if index==len(budget)-1:
                income=int(task["balance"])
    while True:
        try:
            amount=int(input("enter the income in RS. > "))
            income+=amount
            budget.append({"category":"Income added", "amount":amount, "balance":income})
            print("\nIncome added successfully")
            save_budget(budget,file_path)
            break
        except:
            print("\nEnter only the amount in RS not in words\n")
            
def add_expense(budget):
    for index,task in enumerate(budget):
            if index==len(budget)-1:
                income=int(task["balance"])
    if not budget:
        print("\nKindly enter the income first, your income is now RS.0")
    else:
        while True:
            category=input("Enter the category:")
            if category == "":
                print("\nThe category can't be empty!")
            else:
                break
        while True:
            try:
                amount=int(input("Enter the expense:"))
                print(amount)
                income-=amount
                budget.append({"category":category, "amount":amount, "balance":income})
                print("\nThe expense have added successfully")
                save_budget(budget,file_path)
                break
            except:
                print("\nEnter only the amount in RS not in words\n")

def view_budget(budget):
    if not budget:
        print("\nThe no budget or expense have added")
    else:
        print("\nThe budget:")
        for index,task in enumerate(budget,start=1):
            if task['category']=="Income added":
                print(f"{index}. category={task['category']} -- Amount=+{task['amount']} -- balance=RS.{task['balance']}")
            else:
                print(f"{index}. category={task['category']} -- Amount=-{task['amount']} -- balance=Rs.{task['balance']}")

def balance_budget(budget):
    if not budget:
        print("\n No income or expense have been added Yet !")
    for index,task in enumerate(budget):
        if index==len(budget)-1:
            print(f"\nThe balance amount is RS.{task['balance']}")

def delete_budget(budget):
    print("hello")

def save_budget(budget,file_path):
    with open(file_path, 'w') as f:
        for task in budget:
            f.write(f"{task['category']}|{task['amount']}|{task['balance']}\n")

def load_budget(file_path):
    budget=[]
    if os.path.exists(file_path):
        with open(file_path,'r') as f:
            for line in f:
                category, amount, income=line.strip().split('|')
                budget.append({"category":category, "amount":amount, "balance":income})
    return budget
                
                   
budget=[]
file_path="budget_tacker.txt"
budget=load_budget(file_path)
print("BUDGET TRACKER ~ keep track on your budget and save it, enjoy it !") 
while True:
    
    print("""\nOptions:
                1.Add income
                2.Enter expense
                3.View budget
                4.remaining amount
                5.Exit""")
    choice=input("Enter your choice >")
    if choice=='1':
        add_income(budget)
    elif choice=='2':
        add_expense(budget)
    elif choice == '3':
        view_budget(budget)
    elif choice == '4':
        balance_budget(budget)
    elif choice =='5':
        print("\nExiting the budget tracker!")
        break
    else:
        print("\nEnter the valid option")

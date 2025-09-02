
def budget():

    income_list = []
    while True:
        income = input('Enter your encome(s):(printe done if it is done!')
        if income == 'done':
            break
        try:
            income_list.append(int(income))
        except ValueError:
            print('please enter number')
            
        total_income = sum(income_list)
    
    exp_list = []
    while True:
        expenses = input('Enter your expense(s) name and value:(print done if its done)')
        if expenses.lower() == 'done':
            break
        
        try:
            name , value = expenses.split()
            exp_list.append((name, int(value)))

        except ValueError:
            print('please enter name and value')
            
            
    
    values = [value for name , value in exp_list]
    total_expenses = sum(values)
    average_expenses = total_expenses / len(values)
    balance = total_income - total_expenses
    
    
    

    print(f'total income: {total_income}')
    print(f'total expenses : {total_expenses}')
    print(f'average expenses : {average_expenses}')
    print(f'balance : {balance}')


budget()
    
    
    
     
# This program will allow the user to access 2 different financial
# calculators: an investment calculator and a home loan repayment calculator

import math

# collect the calculator choice from the user and include a check to ensure a valid selection has been made
calculator_choice = (input('''chose either 'investment' or  'bond' from the menu below:\ninvestment: to calculate the amount of interest you'll earn on your investment\nbond: to calculate the amount you'll have to pay on a home loan\n''' ))

if calculator_choice.lower() != 'bond' and calculator_choice.lower() != 'investment':
    calculator_choice = input('''Invalid choice, input 'investment'  or 'bond':  ''')

# investment calculator
if calculator_choice.lower() == 'investment': 
    #user input
    investment_amount = int(input('How much have you invested?: '))
    investment_int_rate = int(input('''What us your interest rate? - don't add % sign: '''))
    investment_years = int(input('How many years will you be investing for?: '))
    intrest = input('Inerest Type: simple or compund?: ')

    # ensure a valid selection has been made
    if intrest != 'simple' and intrest != 'compound':
        intrest = input('Invalid Intrest Choice: simple or compound')
    
    #calculating retun
    if intrest == 'simple':
        #simple intrest formula = P(1 + r * t)
        investment_return = investment_amount * (1 + ((investment_int_rate / 100) * investment_years))
    else:
        #compound intrest formula = P (1 + r) ^ t
        investment_return = round(investment_amount * ((math.pow(1 + (investment_int_rate / 100), investment_years))),2)

    # calulate profit
    investment_profit = round((investment_return - investment_amount), 2)

    print(f''' ---- YOUR'RE RICH ----
    INVESTMENT AMOUNT: R{investment_amount}
    INTREST RATE: {investment_int_rate}%
    NO. OF YEARS: {investment_years}
    INVESTMENT RETURN: R{investment_return}  
    INVESTMENT PROFIT: R{investment_profit} ''')    

# bond calculator
elif calculator_choice.lower() == 'bond':
    #user inputs
    house_value = float(input('What is the value of your house'))
    bond_int_rate = int(input('''What us your interest rate? - don't add % sign: '''))
    bond_months = int(input('How many months would it take to repay the bond?: '))

    # calculate repayment with formula # = (i.P/(1 - (1+i)^(-n)))
    monthly_int_rate = bond_int_rate / 12
    bond_repayment = round((monthly_int_rate * house_value) / (1 - math.pow((1 + monthly_int_rate), (-bond_months))), 2)

    # calculate monthly repayments
    monthly_payments = round((bond_repayment / bond_months),2)
    
    print(f'''        ---- HOUSE REPAYMENT PLAN ----
            HOUSE VALUE: {house_value}
            INTEREST RATE: {bond_int_rate}%
            NO. OF MONTHS: {bond_months}
            TOTAL BOND REPAYMENT: R{bond_repayment}
            MONTHLY REPAYMENT: R{monthly_payments}''') 


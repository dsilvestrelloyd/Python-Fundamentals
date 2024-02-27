import math

print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")

which_calculator = input("Enter either \"investment\" or \"bond\" from the menu above to proceed:")


#convert all characters to uppercase to allow different variation of spelling of words.
# .upper() allows for string to compared against one way of spelling, allowing for more efficent use of code 
which_calculator = which_calculator.upper()


# if statement comparing user input, following line ask and store user input around home loan repayments
if which_calculator == "BOND":
    currency = input("Please enter which currency you be working with:")

    house_value = int(input("Please enter the current value of the house:"))

    bond_interest_rate = int(input("Please enter the interest rate:"))

    months_repay = int(input("Please entert the number of months you plan to repay the bond:"))

# created new varible for monthly interest to be used in calculation more seemlessly
    monthly_interest = (bond_interest_rate/100)/12

    monthly_repayment = (monthly_interest*house_value)/(1-(1+monthly_interest)**(-months_repay)) 

    # use of f-string to display currnecy of payment and 
    print(f"Your mpnthly payment is calculated to be {currency}{monthly_repayment}.")

elif which_calculator == "INVESTMENT":

    currency = input("Please enter which currency you be working with:")
    deposit = int(input("Please enter the amount of money you are depositing:"))

    invest_interest_rate = int(input("Please enter the interest rate of the investment:"))
    yearly_interest_rate = invest_interest_rate/100

    years_invest = int(input("Please enter the number of planned years investing:"))

    interest = input("Please enter \"simple\" for simple interest or \"compound\" for compound interest:")
    interest = interest.lower()


    if interest == "simple":
        return_simple_investment = deposit*(1 + yearly_interest_rate*years_invest)
    
        print(f"Your investment is calculated to reach a value of {currency}{return_simple_investment}, using simple interest")
        # print("Your investment is calculated to be a value of {return_simple_investment}.".format{return_simple_investment})

        gross_earnings = return_simple_investment - deposit
        print(f"Your earnings from your investment without charges, taxes, etc... is {currency}{gross_earnings}.")

    elif interest == "compound":
        return_compound_investment = deposit * math.pow(1+(invest_interest_rate/100),years_invest)
        
        print(f"Your investment is calculated to reach a value of {currency}{return_compound_investment}, using compound interest.")

    # did not include the else because once condition for while is be met I would to find a way to take it back to the if/elif statements directly above  
    else:
        while interest != "simple" or interest != "compound":
            interest = input("Please enter \"simple\" for simple interest or \"compound\" for compound interest:")
            interest = interest.lower()
        
        if interest == "simple":
            return_simple_investment = deposit*(1 + yearly_interest_rate*years_invest)
    
            print(f"Your investment is calculated to reach a value of {currency}{return_simple_investment}, using simple interest")
        # print("Your investment is calculated to be a value of {return_simple_investment}.".format{return_simple_investment})

            gross_earnings = return_simple_investment - deposit
            print(f"Your earnings from your investment without charges, taxes, etc... is {currency}{gross_earnings}.")

        elif interest == "compound":
            return_compound_investment = deposit * math.pow(1+(invest_interest_rate/100),years_invest)
        
            print(f"Your investment is calculated to reach a value of {currency}{return_compound_investment}, using compound interest.")
    

else:
    while which_calculator != "BOND" or which_calculator != "INVESTMENT":
    
        which_calculator = input("Please enter \'INVESTMENT\' for investment calculator or \'BOND\' for home loan repayment calculator:")
        which_calculator = which_calculator.upper()

    if which_calculator == "BOND":
        currency = input("Please enter which currency you be working with:")
        house_value = int(input("Please enter the current value of the house:"))
        bond_interest_rate = int(input("Please enter the interest rate:"))
        months_repay = int(input("Please entert the number of months you plan to repay the bond:"))

        monthly_interest = (bond_interest_rate/100)/1
        
        monthly_repayment = (monthly_interest*house_value)/(1-(1+monthly_interest)**(-months_repay))

        print(f"Your mpnthly payment is calculated to be {currency}{monthly_repayment}.")


    elif which_calculator == "INVESTMENT":

        currency = input("Please enter which currency you be working with:")

        deposit = int(input("Please enter the amount of money you are depositing:"))
        
        invest_interest_rate = int(input("Please enter the interest rate of the investment:"))
        yearly_interest_rate = invest_interest_rate/100
        
        years_invest = int(input("Please enter the number of planned years investing:"))
        
        interest = input("Please enter \"simple\" for simple interest or \"compound\" for compound interest:")
        interest = interest.lower()
        
        if interest == "simple":
            return_simple_investment = deposit*(1 + yearly_interest_rate*years_invest)
            
            print(f"Your investment is calculated to reach a value of {currency}{return_simple_investment}, using simple interest")
        # print("Your investment is calculated to be a value of {return_simple_investment}.".format{return_simple_investment})
        
            gross_earnings = return_simple_investment - deposit
            print(f"Your earnings from your investment without charges, taxes, etc... is {currency}{gross_earnings}.")

        elif interest == "compound":
            
            return_compound_investment = deposit * math.pow(1+(invest_interest_rate/100),years_invest)
            print(f"Your investment is calculated to reach a value of {currency}{return_compound_investment}, using compound interest.")

    # did not include the else because once condition for while is be met I would to find a way to take it back to the if/elif statements directly above  
        else:
            while interest != "simple" or interest != "compound":
                interest = input("Please enter \"simple\" for simple interest or \"compound\" for compound interest:")
                interest = interest.lower()
        
            if interest == "simple":
                return_simple_investment = deposit*(1 + yearly_interest_rate*years_invest)
    
                print(f"Your investment is calculated to reach a value of {currency}{return_simple_investment}, using simple interest")
        # print("Your investment is calculated to be a value of {return_simple_investment}.".format{return_simple_investment})

                gross_earnings = return_simple_investment - deposit
                print(f"Your earnings from your investment without charges, taxes, etc... is {currency}{gross_earnings}.")

            elif interest == "compound":
                return_compound_investment = deposit * math.pow(1+(invest_interest_rate/100),years_invest)
        
                print(f"Your investment is calculated to reach a value of {currency}{return_compound_investment}, using compound interest.")
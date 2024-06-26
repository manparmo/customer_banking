# Import the create_cd_account and create_savings_account functions
from savings_account import create_savings_account
from cd_account import *

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = input(f'\nWelcome to the customer banking system\n\nPlease enter the customer savings balance: ')
    savings_interest = input(f'Please enter the customer savings interest rage: ')
    savings_maturity = input(f'Please enter how many months has accrued interest: ')
   
    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(float(savings_balance), float(savings_interest), int(savings_maturity))

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f'The interest earned on the acount created during {savings_maturity} months is: ${interest_earned:,.2f}')
    print(f'The Updated Savings Balance on the acount created is: ${updated_savings_balance:,.2f}')

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = input(f'\nNow let\'s Create a CD for the user\nPlease enter the customer CD balance: ')
    cd_interest = input(f'Please enter the customer CD interest rage: ')
    cd_maturity = input(f'Please enter how many months was the balance invested: ')
    
    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(float(cd_balance), float(cd_interest), int(cd_maturity))

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f'The interest earned on the CD created during {cd_maturity} months is: ${interest_earned:,.2f}')
    print(f'The Updated CD Balance on the acount created is: ${updated_cd_balance:,.2f}')
    print(f'\n\nThank you for using this Central banking system :) print yourself a lot of money!\n')


if __name__ == "__main__":
    # Call the main function.
    main()
'''

    @Author: Shivraj Yelave
    @Date: 25-02-2024
    @Last modified by: Shivraj Yelave
    @Last modified time: 
    @Title: Monthly Payment

'''

class Payment:
    @staticmethod
    def monthly_payment(p, r, y):
        '''
        Description:
            This function calculates the monthly payment for a loan based on 
            the principal amount, annual interest rate, and loan duration in years.

        Parameters:
            p : principal amount
            r : annual interest rate (percentage)
            y : loan duration in years

        Returns:
            monthly payment amount
        '''
        # Convert inputs to integers
        p = int(p)
        r = int(r)
        y = int(y)

        # Calculate the number of monthly payments
        m = 12 * y

        # Calculate the monthly interest rate
        rm = r / (12 * 100)

        # Calculate the monthly payment using the formula for an annuity
        payment = p * rm / (1 - (1 + rm) ** -m)

        return f'{payment:.2f}'

def main():

    # Prompt the user to enter the principal amount
    principal = input("Enter the principal amount: ")

    # Prompt the user to enter the annual interest rate
    rate = input("Enter the rate of interest: ")

    # Prompt the user to enter the loan duration in years
    years = input("Enter time period in years: ")

    # Calculate and print the monthly payment
    print("Monthly payment is: ", Payment.monthly_payment(principal, rate, years))

# If the program is run directly from this location, then only run the main function
if __name__ == '__main__':
    main()

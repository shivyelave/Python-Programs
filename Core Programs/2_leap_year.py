'''


    @Author: Shivraj Yelave
    @Date: 24-02-24
    @Last modified by: Shivraj Yelave
    @Last modified time: 
    @Title: Leap year


'''

def leap_year(year):

    '''
    Description:
        This function checks if the entered year is a leap year.

    Parameters:
        year: Year entered by the user.
        
    Returns:
        True if the year is a leap year, False otherwise.
    '''
    
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Defining main Function
def main():

    year = input("Enter the year(eg: 2024): ")
    if year.isdigit() == False:
        print("Invalid Year. Enter valid year.")

    elif leap_year(int(year)):
        print(f"The Year {year} is leaf year.")
    else:
        print(f"The number {year} is not a leaf year.")
# If the program is run directly from this location then only run main function
if __name__ == '__main__':
    main()

'''


    @Author: Shivraj Yelave
    @Date: 24-02-24
    @Last modified by: Shivraj Yelave
    @Last modified time: 
    @Title: Swap two numbers


'''

def swap_numbers(num1,num2):

    '''
    Description:
        This function swap two numbers.

    Parameters:
        num1 : first number entered by user.
        num2: second number entered by user
        
    Returns:
        swapped number in list.
    '''

    temp = num1
    num1 = num2
    num2 = temp

    return [num1,num2]

# Defining main Function
def main():

    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")

    if (num1.isdigit() and num2.isdigit() and 0 < int(num1) and 0 < int(num2) ) == False:
        print(f"Invalid numbers. Enter valid positive numbers.")
    else: 
        num1 = int(num1)
        num2 = int(num2)
        print(f"Swapped numbers are: {swap_numbers(num1,num2)[0]}, {swap_numbers(num1,num2)[1]}")

# If the program is run directly from this location then only run main function
if __name__ == '__main__':
    main()
'''


    @Author: Shivraj Yelave
    @Date: 24-02-24
    @Last modified by: Shivraj Yelave
    @Last modified time: 
    @Title: Largest among three numbers.


'''

def largest(num1,num2,num3):

    '''
    Description:
        This function find largest number.

    Parameters:
        num1 : first number entered by user.
        num2: second number entered by user
        num3: third number entered by user
        
    Returns:
        largest among three numbers.
    '''

    if num1>num2 and num1>num3:
        return num1
    elif num2>num1 and num2>num3:
        return num2
    else:
        return num3


# Defining main Function
def main():

    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    num3 = input("Enter third number: ")

    if (num1.isdigit() and num2.isdigit() and num3.isdigit() and 0 < int(num1) and 0 < int(num2) and 0 < int(num3) ) == False:
        print(f"Invalid numbers. Enter valid positive numbers.")
    else: 
        num1 = int(num1)
        num2 = int(num2)
        num3 = int(num3)
        print(f"Largest number among {num1}, {num2}, {num3} is {largest(num1,num2,num3)}")

# If the program is run directly from this location then only run main function
if __name__ == '__main__':
    main()
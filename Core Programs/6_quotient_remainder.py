'''


    @Author: Shivraj Yelave
    @Date: 24-02-24
    @Last modified by: Shivraj Yelave
    @Last modified time: 
    @Title: Quotient and Remainder


'''

def quotient_remainder(divident,divisor):

    '''
    Description:
        This function calculate quotient and remainder of number.

    Parameters:
        divident : Divident entered by user.
        divisor: Divisor entered by user
        
    Returns:
        quotient and remainder in list.
    '''

    quotient = divident // divisor
    remainder = divident % divisor
    return [quotient,remainder]

# Defining main Function
def main():

    divident = input("Enter the divident: ")
    divisor = input("Enter the divisor: ")

    if (divident.isdigit() and divisor.isdigit() and 0 < int(divident) and 0 < int(divisor) ) == False:
        print(f"Invalid divident or divisor. Enter valid positive numbers.")
    else: 
        divisor = int(divisor)
        divident = int(divident)
        print(f"Quotient is ", quotient_remainder(divident,divisor)[0])
        print(f"Remainder is ", quotient_remainder(divident,divisor)[1])

# If the program is run directly from this location then only run main function
if __name__ == '__main__':
    main()
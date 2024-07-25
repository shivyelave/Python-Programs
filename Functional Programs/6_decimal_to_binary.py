'''

    @Author: Shivraj Yelave
    @Date: 25-02-2024
    @Last modified by: Shivraj Yelave
    @Last modified time: 
    @Title: Decimal to Binary

'''

class Binary:

    @staticmethod
    def to_binary(number):
        '''
        Description:
            This function converts a non-negative decimal number to its binary representation.

        Parameters:
            number : int : the non-negative decimal number to convert.

        Returns:
            str : binary representation of the decimal number.
        '''
        number = int(number)
        if number == 0:
            return '0'
        
        binary_number = ''
        i = 7  
        while i >= 0:
            if 2**i <= number:
                binary_number += '1'
                number -= 2**i
            else:
                binary_number += '0'
            i -= 1

        return binary_number

def main():
    '''
    Description:
        Main function to prompt the user for a decimal number and display its binary representation.
    '''
    # Prompt the user to enter a non-negative number
    number = input("Enter a non-negative number: ")

    if number.isdigit() and int(number) >= 0:
        # Compute and print the binary representation
        print(f"Binary number is: {Binary.to_binary(number)[:4]} {Binary.to_binary(number)[4:]}")
    else:
        print("Enter a valid non-negative integer.")

# If the program is run directly from this location, then only run the main function
if __name__ == '__main__':
    main()

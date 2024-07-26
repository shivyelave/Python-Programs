'''

    @Author: Shivraj Yelave
    @Date: 25-02-2024
    @Last modified by: Shivraj Yelave
    @Last modified time: 
    @Title: Swap nibbles and find resultant decimal number

'''

class Swap:

    @staticmethod
    def swap_nibbles(number):
        '''

        Description:
            This function converts a non-negative decimal number to its binary representation and the swap the nibbles.

        Parameters:
            number : the non-negative decimal number to convert.

        Returns:
            decimal number after swapping nibbles.
        '''
        
        
        
        
        number = int(number)
        if number == 0:
            return '0'
        
        binary_number = ''
        i = 8  
        while i >= 0:
            if 2**i <= number:
                binary_number += '1'
                number -= 2**i
            else:
                binary_number += '0'
            i -= 1

        swap = binary_number[4:] + binary_number[:4]

        return int(swap,2)


def main():
    '''
    Description:
        Main function to prompt the user for a decimal number and display its binary representation.
    '''
    # Prompt the user to enter a non-negative number
    number = input("Enter a non-negative number: ")

    if number.isdigit() and int(number) >= 0:
        print(f"Number after swapping nibble is: {Swap.swap_nibbles(number)}")
    else:
        print("Enter a valid non-negative integer.")


# If the program is run directly from this location, then only run the main function
if __name__ == '__main__':
    main()

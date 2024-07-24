'''


    @Author: Shivraj Yelave
    @Date: 23-02-24
    @Last modified by: Shivraj Yelave
    @Last modified time: 
    @Title: Reverse Number


'''

def reverse(n):
    '''
        Description:
            This funtion is to Reverse a number.

        Parameters:
            n: number entered by user.
        
        Return:
            Reversed number.
    '''
    
    dig = 0  # Initialize variable to hold the current digit
    rev = 0  # Initialize variable to hold the reversed number

    # Loop until n becomes 0
    while n > 0:
        dig = n % 10          # Extract the last digit of n
        rev = 10 * rev + dig  # Append the digit to the reversed number
        print(rev)            # Print the current state of the reversed number
        n = n // 10           # Remove the last digit from n by integer division

    return rev  


# Defining main Function
def main():

    num = input("Enter the number: ")
    print(f"Reverse of {num} is ",reverse(int(num)))

# If the program is run directly from this location then only run main function
if __name__ == '__main__':
    main()
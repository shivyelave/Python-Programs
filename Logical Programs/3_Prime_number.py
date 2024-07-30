'''


    @Author: Shivraj Yelave
    @Date: 23-02-24
    @Last modified by: Shivraj Yelave
    @Last modified time: 
    @Title: Prime Number


'''


def isPrime(n):
    '''
        Description:
            This funtion is to check the entered number is prime or not.

        Parameters:
            n: number entered by user.
        
        Return:
            Entered number is prime or not i.e. True or False .
    '''

    # Check if n is 2, which is the smallest prime number
    if n == 2:
        return True

    # Iterate from 2 to the square root of n+1
    # Any factor of n greater than its square root would have a corresponding factor less than its square root
    for i in range(2, int(n**0.5) + 1):
        # If n is divisible by any number in this range, it's not a prime number
        if n % i == 0:
            return False
    else:
        # If no divisors were found, n is a prime number
        return True 


# Defining main Function
def main():
    number = int(input("Enter the positive Integer: "))

    if isPrime(number):
        print(f"The number {number} is Prime Number.")
    else:
        print(f"The number {number} is not a Prime Number.")

# This ensures that the main() function is called only when the script is run directly.
# If the script is imported as a module in another script, main() will not be executed.
if __name__ == '__main__':
    main()
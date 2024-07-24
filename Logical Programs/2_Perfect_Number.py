'''


    @Author: Shivraj Yelave
    @Date: 23-02-24
    @Last modified by: Shivraj Yelave
    @Last modified time: 
    @Title: Perfect Numbers
    

'''

def check_perfect_number(n):
    '''
        Description:
            This funtion is to check the number.

        Parameters:
            n: Number by user.
        
        Return:
            True or False i.e. number is perfect or not.
    '''

    sum = 0

    for i in range(1,n):
        if n % i ==0:
            sum = sum + i
    return sum == n


# Defining main Function

def main():
    number = int(input("Enter the positive Integer: "))

    if check_perfect_number(number):
        print(f"The number {number} is Perfect Number.")
    else:
        print(f"The number {number} is not a Perfect Number.")

# This ensures that the main() function is called only when the script is run directly.
# If the script is imported as a module in another script, main() will not be executed.
if __name__ == '__main__':
    main()
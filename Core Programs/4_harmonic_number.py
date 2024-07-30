'''


    @Author: Shivraj Yelave
    @Date: 24-02-24
    @Last modified by: Shivraj Yelave
    @Last modified time: 
    @Title: Harmonic number


'''

def harmonic(n):
    
    '''
    Description:
        This recurssive function calculate 1/n.

    Parameters:
        n: number.
        
    Returns:
        funtion with vanlue n-1.
    '''
    
    # Base case
    if n == 1:
        return 1
    # Recursive case
    return 1 / n + harmonic(n - 1)


# Defining main Function
def main():

    num = input("Enter the number: ")
    if (num.isdigit() and 0 < int(num) ) == False:
        print(f"Invalid number.")
    else: 
        print(f"Harmonic number is {harmonic(int(num)):.2f}")

# If the program is run directly from this location then only run main function
if __name__ == '__main__':
    main()

'''


    @Author: Shivraj Yelave
    @Date: 25-02-2024
    @Last modified by: Shivraj Yelave
    @Last modified time: 
    @Title: Square Root Calculation using Newton's Method

    
'''

class Squareroot:
    @staticmethod
    def sqrt(c):
        '''
        Description:
            This function computes the square root of a non-negative number c
            using Newton's method with a specified accuracy.

        Parameters:
            c : the non-negative number for which to compute the square root.

        Returns:
             the square root of the number c.
        '''
        c = int(c)
        epsilon = 1e-15  # Desired accuracy
        t = c  # Initial guess

        # Newton's method iteration
        while abs(t - c / t) > epsilon * t:
            t = (t + c / t) / 2

        return f'{t:.2f}'

def main():

    # Prompt the user to enter a non-negative number
    number = input("Enter a non-negative number: ")

    if number.isdigit() and int(number) > 0:
        # Compute and print the square root
        print("Square root is:", Squareroot.sqrt(number))
    else:
        print("Enter valid positive integer.")

# If the program is run directly from this location, then only run the main function
if __name__ == '__main__':
    main()

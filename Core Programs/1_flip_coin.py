'''


    @Author: Shivraj Yelave
    @Date: 24-02-24
    @Last modified by: Shivraj Yelave
    @Last modified time: 
    @Title: Flip a Coin and count head percentage


'''

import random

def flip_coin(n):

    '''
        Description:
            This funtion is to flip the coin n times.

        Parameters:
            n: Number by user.
        
        Return:
            Percentage of head.
    '''

    head = 0  # Initialize the counter for heads

    for _ in range(n):  # Loop n times
        choices = random.choice(["H", "T"])  # Randomly choose between "H" and "T"
        if choices == "H":  # If the choice is heads ("H")
            head += 1  # Increment the head counter

    return head / n * 100  # Calculate the percentage of heads and return it


# Defining main Function
def main():

    num = input("Enter the number of time coin is fliped: ")
    if num.isdigit():
        print(f"Percent of head occur is {flip_coin(int(num)):.2f} %")
    else: 
        print("Invalid number. Enter valid number. eg: 27.")

# If the program is run directly from this location then only run main function
if __name__ == '__main__':
    main()


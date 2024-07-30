'''


    @Author: Shivraj Yelave
    @Date: 24-02-24
    @Last modified by: Shivraj Yelave
    @Last modified time: 
    @Title: Power of 2


'''

def power_of_2(power):
    '''
        Description:
            This funtion is to generate power of 2.

        Parameters:
            power: Power of 2.
        
        Return:
            2 to the power power(parameter).
    '''

    return 2**power

# Defining main Function
def main():

    power = input("Enter the power of 2(0 to 31): ")
    if (power.isdigit() and 0 <= int(power) < 32) == False:
        print(f"Invalid power. Enter valid number between 0 and 31.")
    else: 
        power = int(power)
        for i in range(power+1):
            print(f"2^{i} = {power_of_2(i)}")

# If the program is run directly from this location then only run main function
if __name__ == '__main__':
    main()

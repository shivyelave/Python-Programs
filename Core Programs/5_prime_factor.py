'''


    @Author: Shivraj Yelave
    @Date: 24-02-24
    @Last modified by: Shivraj Yelave
    @Last modified time: 
    @Title: Prime Factor


'''

def prime_factor(number):

    '''
    Description:
        This function calculate prime factors of number.

    Parameters:
        number : number to find its prime factor.
        
    Returns:
        list of prime factor.
    '''

    factor = []


    while number % 2 ==0:
        factor.append(2)
        number = number // 2

    for i in range(3,int(number**0.5)+1):
        while number % i == 0:
            factor.append(i)
            number = number // i
    if number > 1 :
        factor.append(number)

    return factor

# Defining main Function
def main():

    num = input("Enter the number: ")
    if (num.isdigit() and 0 < int(num) ) == False:
        print(f"Invalid power. Enter valid number.")
    else: 
        num = int(num)
        print(f"Prime factors are ", prime_factor(num))

# If the program is run directly from this location then only run main function
if __name__ == '__main__':
    main()

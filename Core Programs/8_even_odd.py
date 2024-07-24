'''


    @Author: Shivraj Yelave
    @Date: 24-02-24
    @Last modified by: Shivraj Yelave
    @Last modified time: 
    @Title: Even or Odd


'''

def even_odd(number):

    '''
    Description:
        This function check number is even or odd.

    Parameters:
        number : number entered by user.
        
    Returns:
        True if number is even else false.
    '''



    if number % 2 ==0:
        return True
    else: 
        False



# Defining main Function
def main():

    num = input("Enter the number: ")
    if (num.isdigit() and 0 < int(num) ) == False:
        print(f"Invalid number. Enter positve integer")
    else: 
        num = int(num)
        if even_odd(num):
            print(f"Number {num} is even.")
        else:
            print(f"Number {num} is odd.")


# If the program is run directly from this location then only run main function
if __name__ == '__main__':
    main()

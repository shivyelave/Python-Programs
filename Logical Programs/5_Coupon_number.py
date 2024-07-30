'''


    @Author: Shivraj Yelave
    @Date: 23-02-24
    @Last modified by: Shivraj Yelave
    @Last modified time: 
    @Title: Coupen code Generator


'''

#import random function 
import random


def check_coupon(coupon,random_coupons):

    '''
        Description:
            This funtion will match random generated coupon with user coupon.

        Parameters:
            coupon: User's Coupon.
            random_coupons: list of random coupons.
        
        Return:
            True if coupon is Match else false.
    '''
    return True if coupon in random_coupons else False


def generate_random_coupon(length):

    '''
        Description:
            This funtion will generate random coupons.

        Parameters:
            length: number of random coupon to be generated.
        
        Return:
            List of coupons.
    '''

    coupons = []
    i=0
    
    #generate unique random number
    while i < length:
        num = random.randint(1000,9999)
        if num not in coupons:
            coupons.append(num)
            i+=1
    return coupons

# Defining main Function
def main():
    length = int(input("Enter the number of coupons required: "))
    u_coupon = int(input("Enter the your coupons number(4-digit): "))

    coupons = generate_random_coupon(length)

    print("Total generated coupons are",len(coupons))
    print("Lucky coupons who won are:")
    print(coupons)

    if check_coupon(u_coupon,coupons):
        print(f"Your coupon number is in lucky coupon list. You won the lottery")
    else:
        print(f"Sorry your coupon number is not in lucky coupon list. Better luck next time.")

# This ensures that the main() function is called only when the script is run directly.
# If the script is imported as a module in another script, main() will not be executed.
if __name__ == '__main__':
    main()
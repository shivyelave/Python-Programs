'''


    @Author: Shivraj Yelave
    @Date: 23-02-24
    @Last modified by: Shivraj Yelave
    @Last modified time: 
    @Title: Fibonacci Series


'''


def fibonacci(n):
    '''
        Description:
            This funtion is to create the fibonacci series of length n.

        Parameters:
            n: lenth of series i.e. how many number will be there in series.
        
        Return:
            List of finonacci series.
    '''

    #Initialize first and second number
    fib=[0,1]

    #Conditions for length 0, 1 and 2
    if n==0:
        return 0
    elif n==1:
        return [0]
    elif n== 2:
        return [0,1]
    
    #Further series number

    else:
        for i in range(2,n):
            fib.append(fib[i-1]+fib[i-2])
        return fib
    
# Defining main Function
def main():

    num = input("Enter the number: ")
    print("Fibonacci Series is ",fibonacci(int(num)))

# If the program is run directly from this location then only run main function
if __name__ == '__main__':
    main()
'''


    @Author: Shivraj Yelave
    @Date: 23-02-24
    @Last modified by: Shivraj Yelave
    @Last modified time: 24-02-24 10:30
    @Title: Reverse Number


'''

#import time module
import time

def main():
       
    # Prompt the user to start the timer
    start = input("Press enter to start.")
    
    # Record the current time in seconds since the epoch
    curr_time = time.time()
    
    # Prompt the user to stop the timer
    end = input("Press enter again to end.")
    
    # Calculate the elapsed time in seconds
    time_taken = time.time() - curr_time 
    
    # Calculate the elapsed time in minutes
    min = time_taken // 60
    
    # Calculate the remaining seconds after extracting minutes
    sec = time_taken % 60
    
    # Calculate the milliseconds part by extracting the fractional part of seconds and converting to milliseconds
    msec = (sec - int(sec)) * 100

    # Print the elapsed time in the format mm:ss:ms
    print(f"\nTime Taken is {int(min):02d}:{int(sec):02d}:{int(msec):02d}")


    
# This ensures that the main() function is called only when the script is run directly.
# If the script is imported as a module in another script, main() will not be executed.
if __name__ == '__main__':
    main()
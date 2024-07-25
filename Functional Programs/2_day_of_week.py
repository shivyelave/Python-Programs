'''


    @Author: Shivraj Yelave
    @Date: 24-02-24
    @Last modified by: Shivraj Yelave
    @Last modified time: 25-7-2024
    @Title: Day of week


'''
class Day:

    @staticmethod
    def day_of_week(d, m, y):
        '''
        Description:
            This method calculates the day of the week for a given date using
            Zeller's Congruence algorithm.

        Parameters:
            d : int : day of the month
            m : int : month of the year
            y : int : year

        Returns:
            int : the day of the week (0 = Saturday, 1 = Sunday, ..., 6 = Friday)
        '''
        # Convert input strings to integers
        d = int(d)
        m = int(m)
        y = int(y)

        # Adjust the year based on the month
        y1 = y - (14 - m) // 12

        # Calculate the intermediary value x using the adjusted year
        x = y1 + y1 // 4 - y1 // 100 + y1 // 400

        # Adjust the month
        m1 = m + 12 * ((14 - m) // 12) - 2

        # Calculate the day of the week (0 = Saturday, 1 = Sunday, ..., 6 = Friday)
        d1 = (d + x + 31 * m1 // 12) % 7

        # Return the calculated day of the week
        return d1

def main():
    '''
    Description:
        Main function to prompt user for date input and display the calculated
        day of the week.
    '''

    # Prompt the user to enter the date
    date = input("Enter date between 1 and 31: ")

    # Prompt the user to enter the month
    month = input("Enter the month between 1 and 12: ")

    # Prompt the user to enter the year
    year = input("Enter year (e.g., 2024):")

    # Print the calculated day of the week
    days=['Sunday','Modnday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    print("Day of Week is: ", days[Day.day_of_week(date, month, year)])

# If the program is run directly from this location, then only run the main function
if __name__ == '__main__':
    main()

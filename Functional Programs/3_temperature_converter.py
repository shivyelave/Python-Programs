'''

    @Author: Shivraj Yelave
    @Date: 25-02-2024
    @Last modified by: Shivraj Yelave
    @Last modified time: 
    @Title: Temperature Conversion
    

'''

class Convert_temp:

    @staticmethod
    def temperature_conversion(value, unit):
        '''
        Description:
            This function converts temperature between Celsius and Fahrenheit.

        Parameters:
            value :  temperature value entered by user.
            unit : unit of the temperature entered by user, 'C' for Celsius and 'F' for Fahrenheit.

        Returns:
            converted temperature value in the opposite unit.
        '''
        
        if unit == 'C':
            # Convert Celsius to Fahrenheit
            return (value * 9/5) + 32
        else:
            # Convert Fahrenheit to Celsius
            return (value - 32) * 5/9


# Defining main function
def main():
    '''
    Description:
        Main function to prompt user for temperature input and display the converted temperature.
    '''
    
    # Prompt the user to enter the temperature value
    temp_value = float(input("Enter the temperature value: "))
    
    # Prompt the user to enter the unit of the temperature
    temp_unit = input("Enter the unit ('C' for Celsius, 'F' for Fahrenheit): ").upper()

    if temp_unit == 'C' or temp_unit == 'F' :
        # Convert the temperature using the temperature_conversion function
        converted_temp = Convert_temp.temperature_conversion(temp_value, temp_unit)
        
        # Determine the unit of the converted temperature
        converted_unit = 'F' if temp_unit == 'C' else 'C'
        
        # Print the converted temperature
        print(f"Converted Temperature: {converted_temp:.2f}°{converted_unit}")
    
    else:
        print("Enter Valid Input.'C' for Celsius, 'F' for Fahrenheit")


# If the program is run directly from this location, then only run the main function
if __name__ == '__main__':
    main()

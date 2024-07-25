'''


    @Author: Shivraj Yelave
    @Date: 24-02-24
    @Last modified by: Shivraj Yelave
    @Last modified time: 
    @Title: Notes to be returned by Vending Machine


'''

def vending_machine(number, avai_notes=None):
    '''
    Description:
        This function calculates the notes to be returned of 1, 2, 5, 10, 50, 100, 500, and 1000 Rs Notes.

    Parameters:
        number : Money entered by user.
        avai_notes : List of available denominations (default is [1000, 500, 100, 50, 10, 5, 2, 1]).
        
    Returns:
        list : Notes of each denomination.
    '''
    
    if avai_notes is None:
        avai_notes = [1000, 500, 100, 50, 10, 5, 2, 1]
    
    # Base case: if no money is left
    if number == 0:
        return []
    
    # Find the largest note that is less than or equal to the current amount
    for note in avai_notes:
        if number >= note:
            # Take one note of the current denomination and call recursively for the remaining amount
            return [note] + vending_machine(number - note, avai_notes)




# Defining main Function
def main():

    num = input("Enter the number: ")
    if (num.isdigit() and 0 < int(num) ) == False:
        print(f"Invalid number. Enter valid number.")
    else: 
        num = int(num)
        print(f"Number of Notes required are ",len(vending_machine(num)))
        print(f"Notes required are ", vending_machine(num))

# If the program is run directly from this location then only run main function
if __name__ == '__main__':
    main()

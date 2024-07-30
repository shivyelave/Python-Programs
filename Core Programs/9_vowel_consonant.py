'''


    @Author: Shivraj Yelave
    @Date: 24-02-24
    @Last modified by: Shivraj Yelave
    @Last modified time: 
    @Title: Vowel or Consonant


'''

def vowel_consonant(alphabet):

    '''
    Description:
        This function check alphabate is vowel or consonant.

    Parameters:
        alphabet : alphabet entered by user.
        
    Returns:
        True if alphabate is vowle else False.
    '''

    vowel = ['a','e','i','o','u','A','E','I','O','U']

    if alphabet  in vowel :
        return True
    else: 
        False



# Defining main Function
def main():

    alphabet = input("Enter the alphabet: ")
    if (alphabet.isalpha()) == False:
        print(f"Invalid Alphabet. Enter a to z or A to Z.")
    else: 
        if vowel_consonant(alphabet[0]):
            print(f"Alphabet {alphabet[0]} is vowel.")
        else:
            print(f"Alphabet {alphabet[0]} is consonant.")

# If the program is run directly from this location then only run main function
if __name__ == '__main__':
    main()

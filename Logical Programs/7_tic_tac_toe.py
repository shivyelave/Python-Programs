class TikTacToe:
    @staticmethod
    def grid(input):
        '''
        Description:
            This function formats a list of 9 elements into a 3x3 Tic-Tac-Toe grid.

        Parameters:
            input : list : a list of 9 elements to display in the grid.

        Returns:
            str : formatted grid string.
        '''
        return (
            f"{input[0]:^5}|{input[1]:^5}|{input[2]:^5}\n"
            f"{'-' * 17}\n"
            f"{input[3]:^5}|{input[4]:^5}|{input[5]:^5}\n"
            f"{'-' * 17}\n"
            f"{input[6]:^5}|{input[7]:^5}|{input[8]:^5}\n"
        )

    @staticmethod
    def check_and_add_input(input, number, index):
        '''
        Description:
            This function checks if a specified cell is empty and updates it with the given number.

        Parameters:
            input : list : the current board state.
            number : str : the player's mark ('X' or 'O').
            index : int : the position on the board to update.

        Returns:
            str : confirmation message or error message if the place is already taken.
        '''
        index = int(index) - 1  # Adjust for zero-based index
        
        if input[index] == '':  # Check if the cell is empty
            input[index] = number  # Update the cell with the player's mark
            return True  # Return True if the update was successful
        else:
            return False  # Return False if the cell is already taken

    @staticmethod
    def check_win(input):
        '''
        Description:
            This function checks if there is a winning pattern on the Tic-Tac-Toe board.

        Parameters:
            input : list : the current board state.

        Returns:
            str : the winner ('O' or 'X') if there's a winning pattern, otherwise None.
        '''
        # Define winning patterns (rows, columns, diagonals)
        win_patterns = [
            [0, 1, 2],  # Top row
            [3, 4, 5],  # Middle row
            [6, 7, 8],  # Bottom row
            [0, 3, 6],  # Left column
            [1, 4, 7],  # Middle column
            [2, 5, 8],  # Right column
            [0, 4, 8],  # Diagonal from top-left to bottom-right
            [2, 4, 6]   # Diagonal from top-right to bottom-left
        ]

        # Check for winners
        for pattern in win_patterns:
            if input[pattern[0]] == input[pattern[1]] == input[pattern[2]] != '':  # Check if all cells in a pattern are equal and not empty
                return input[pattern[0]]  # Return the winner's mark

        # If no winner
        return None  # Return None if there's no winner

    @staticmethod
    def validate_input(index):
        '''
        Description:
            This function validates if the provided input is a valid number between 1 and 9.

        Parameters:
            index : str : the input to validate.

        Returns:
            bool : True if valid, False otherwise.
        '''
        # Check if the input is a digit and between 1 and 9
        if (index.isdigit() and 0 < int(index) <= 9) == False:
            return False  # Return False if not valid
        else:
            return True  # Return True if valid

def main():
    inp = ['','','','','','','','','']  # Initialize an empty board
    player1 = input("Enter first player name: ")  # Get player 1's name
    player2 = input("Enter second player name: ")  # Get player 2's name

    print(f"{player1} is X\n{player2} is O")  # Assign 'X' to player 1 and 'O' to player 2
    print("Enter number to do X or O in that box")
    # Display the board with positions
    print(f"{'1':^5}|{'2':^5}|{'3':^5}\n"
          f"{'-' * 17}\n"
          f"{'4':^5}|{'5':^5}|{'6':^5}\n"
          f"{'-' * 17}\n"
          f"{'7':^5}|{'8':^5}|{'9':^5}\n")
    turn = True  # Track whose turn it is; True for player 1, False for player 2
    remaning = True  # Track if there are remaining empty cells

    while remaning:
        if turn:  # Player 1's turn
            player_input = input(f"{player1} turn: ")
            if TikTacToe.validate_input(player_input):  # Validate the input
                if TikTacToe.check_and_add_input(inp, 'X', player_input) == False:  # Try to place 'X'
                    print("Place is already taken. Enter another number.")
                else:
                    turn = False  # Switch turn
                    print(TikTacToe.grid(inp))  # Print the updated board
                    if TikTacToe.check_win(inp) == None:  # Check if there's a winner
                        continue  # Continue if no winner
                    else:
                        print(f"{player1} Wins")  # Announce the winner
                        break
            else:
                print("Enter valid number between 1 and 9.")  # Invalid input message
        else:  # Player 2's turn
            player_input = input(f"{player2} turn: ")
            if TikTacToe.validate_input(player_input):  # Validate the input
                if TikTacToe.check_and_add_input(inp, 'O', player_input) == False:  # Try to place 'O'
                    print("Place is already taken. Enter another number.")
                else:
                    turn = True  # Switch turn
                    print(TikTacToe.grid(inp))  # Print the updated board
                    if TikTacToe.check_win(inp) == None:  # Check if there's a winner
                        continue  # Continue if no winner
                    else:
                        print(f"Congratulations! {player2} Wins.")  # Announce the winner
                        break
            else:
                print("Enter valid number between 1 and 9.")  # Invalid input message
        
        remaning = '' in inp  # Check if there are remaining empty cells

if __name__ == '__main__':
    main()

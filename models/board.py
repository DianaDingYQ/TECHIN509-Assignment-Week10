class Board:
    def __init__(self):
        self.grid = [[" " for _ in range(3)] for _ in range(3)]

    def draw_board(self):
        """
        Draw the board of Tic-Tac-Toe game
        """
        for row in range(3):
            print(" | ".join(self.grid[row]))  
            if row < 2: 
                print("-" * 9)

    def update_board(self, row: int, col: int, symbol: str) -> bool:
        """
        Update the game board based on location selected by player

        Args:
            row (int): row index of board
            col (int): column index of board
            symbol (str): symbol used by player
        """
        if self.grid[row][col] == " ":
            self.grid[row][col] = symbol
            return True
        return False

    def check_winner(self) -> str:
        """
        Check the winner of the current board

        Returns:
            str: The winning symbol ('X' or 'O') if there is a winner, else an empty string
        """
        # Check rows
        for row in self.grid:
            if row[0] == row[1] == row[2] and row[0] != " ":
                return row[0]
        # Check columns
        for col in range(3):
            if self.grid[0][col] == self.grid[1][col] == self.grid[2][col] and self.grid[0][col] != " ":
                return self.grid[0][col]
        # Check diagonals
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] and self.grid[0][0] != " ":
            return self.grid[0][0]
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] and self.grid[0][2] != " ":
            return self.grid[0][2]
        return ""

    def is_full(self) -> bool:
        """
        Check if the current board is full or not

        Returns:
            bool: Boolean outcome indicating whether the board is full
        """
        return all(cell != " " for row in self.grid for cell in row)


if __name__ == "__main__":
    while True:
        board = Board()
        current_player = "X"
        moves = []  # 保存每一步的操作记录

        print("Welcome to Tic-Tac-Toe!")
        while not board.is_full():
            board.draw_board()
            print(f"Player {current_player}'s turn.")
            try:
                row = int(input("Enter row (0, 1, 2): "))
                col = int(input("Enter column (0, 1, 2): "))
            except ValueError:
                print("Invalid input. Please enter numbers between 0 and 2.")
                continue

            if 0 <= row < 3 and 0 <= col < 3:
                if board.update_board(row, col, current_player):
                    moves.append((current_player, row, col))  # 记录玩家的操作
                    winner = board.check_winner()
                    if winner:
                        board.draw_board()
                        print(f"Player {winner} wins!")
                        break
                    current_player = "O" if current_player == "X" else "X"
                else:
                    print("Cell is already occupied. Try again.")
            else:
                print("Invalid input. Please enter numbers between 0 and 2.")

        else:
            board.draw_board()
            print("It's a draw!")

        
        with open("game_record.txt", "a") as f:
            f.write("Tic-Tac-Toe Game Record\n")
            f.write("=======================\n")
            for move in moves:
                f.write(f"Player {move[0]} -> Row: {move[1]}, Column: {move[2]}\n")
            if winner:
                f.write(f"\nWinner: {winner}\n\n")
            else:
                f.write("\nResult: Draw\n\n")

        
        replay = input("Do you want to play another game? (yes/no): ").strip().lower()
        if replay != "yes":
            print("Thank you for playing!")
            break

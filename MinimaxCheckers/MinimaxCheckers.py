"""
  Program Title: MiniMaxCheckers
  Author: Michael Roy
  Date: 5/3/2024
  Description: This is a simple user vs ai, checkers game done in python 
  using the minimax algorithm.
"""

import copy
import time
import sys

# Define the size of the checkers board
BOARD_SIZE = 8

# Define player constants
USER = 2
AI = 1

# Initialize scores
user_score = 0
ai_score = 0

# Function to display a typing animation
def typing_animation(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    print("\n")

# Function to wait for user to press Enter
def wait_for_enter():
    input()

# Function to initialize the game board
def initialize_board():
    board = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]
    for row in range(8):
        for col in range(8):
            if (row + col) % 2 != 0:
                if row < 3:
                    board[row][col] = USER
                elif row > 4:
                    board[row][col] = AI
    return board

# Function to display the current state of the game board
def display_board(board):
    print("   ", end="")
    for col in range(BOARD_SIZE):
        print(chr(65 + col), end=" ")
    print()
    for i in range(BOARD_SIZE):
        print(BOARD_SIZE - i, end="  ")
        for j in range(BOARD_SIZE):
            if board[BOARD_SIZE - 1 - i][j] == 0:
                print(".", end=" ")
            elif board[BOARD_SIZE - 1 - i][j] == USER:
                print("O", end=" ")
            else:
                print("X", end=" ")
        print(" " + str(BOARD_SIZE - i))
    print("   ", end="")
    for col in range(BOARD_SIZE):
        print(chr(65 + col), end=" ")
    print()

# Function to check if a move is valid
def is_valid_move(board, player, start_row, start_col, end_row, end_col):
    # Check if the start and end positions are within the board boundaries
    if not (0 <= start_row < BOARD_SIZE and 0 <= start_col < BOARD_SIZE and
            0 <= end_row < BOARD_SIZE and 0 <= end_col < BOARD_SIZE):
        return False
    # Check if the start position contains the player's piece
    if board[start_row][start_col] != player:
        return False
    # Check if the end position is empty
    if board[end_row][end_col] != 0:
        return False
    # Check if the move is diagonal and within one or two squares
    if abs(start_row - end_row) not in [1, 2] or abs(start_col - end_col) not in [1, 2]:
        return False
    # Check if there's an opponent's piece to capture
    if abs(start_row - end_row) == 2:
        mid_row = (start_row + end_row) // 2
        mid_col = (start_col + end_col) // 2
        if board[mid_row][mid_col] == 0 or board[mid_row][mid_col] == player:
            return False
    # Check if the user is moving up (from lower row number to higher row number)
    if player == USER and start_row >= end_row:
        return False
    # Check if the AI is moving down (from higher row number to lower row number)
    if player == AI and start_row <= end_row:
        return False
    return True

# Function to apply a move to the game board
def apply_move(board, start_row, start_col, end_row, end_col):
    # Make a deep copy of the board to avoid modifying the original
    new_board = copy.deepcopy(board)
    # Move the piece from the start position to the end position
    new_board[end_row][end_col] = new_board[start_row][start_col]
    new_board[start_row][start_col] = 0
    # If the move is a capture, remove the opponent's piece from the board
    if abs(start_row - end_row) == 2:
        mid_row = (start_row + end_row) // 2
        mid_col = (start_col + end_col) // 2
        new_board[mid_row][mid_col] = 0
    return new_board

# Function to get all possible moves for a player
def get_possible_moves(board, player):
    moves = []
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == player:
                for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                    for dist in [1, 2]:
                        new_row, new_col = row + dr * dist, col + dc * dist
                        if is_valid_move(board, player, row, col, new_row, new_col):
                            moves.append((row, col, new_row, new_col))
    return moves

# Minimax algorithm with alpha-beta pruning
def minimax(board, depth, maximizing_player, alpha, beta):
    if depth == 0:
        return evaluate(board), None

    player = AI if maximizing_player else USER
    possible_moves = get_possible_moves(board, player)

    # Sort moves based on the magnitude of row distance
    possible_moves.sort(key=lambda move: abs(move[0] - move[2]), reverse=True)

    if maximizing_player:
        max_eval = float('-inf')
        best_move = None
        for move in possible_moves:
            new_board = apply_move(board, *move)
            eval, _ = minimax(new_board, depth - 1, False, alpha, beta)
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = float('inf')
        best_move = None
        for move in possible_moves:
            new_board = apply_move(board, *move)
            eval, _ = minimax(new_board, depth - 1, True, alpha, beta)
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_move

# Evaluation function (simple scoring)
def evaluate(board):
    ai_count = sum(row.count(AI) for row in board)
    user_count = sum(row.count(USER) for row in board)
    return ai_count - user_count

# Main function to run the game
def main():
    global user_score, ai_score
    # Display welcome message and instructions
    welcome_message = "Hello, welcome to Royboy Checkers! This is a simple game of user vs ai, checkers. There are no double jumps, and no crowning of pieces. Capture your opponents pieces to score points. The first team to score 5 points wins. \n\nPRESS ENTER TO PLAY!"
    typing_animation(welcome_message)
    wait_for_enter()
    # Initialize the game board
    board = initialize_board()
    display_board(board)
    # Main game loop
    while True:
        # Display current scores
        print("User Score:", user_score)
        print("AI Score:", ai_score)
        # Check for game over conditions
        if user_score >= 5:
            print("Congratulations! You have won the game!")
            break
        elif ai_score >= 5:
            print("Sorry, you have lost the game. Better luck next time!")
            break
        # Get user's move input
        user_move = input("Enter your move (e.g., A3 B4): ").upper().split()
        # Validate user input format
        if len(user_move) != 2 or len(user_move[0]) != 2 or len(user_move[1]) != 2:
            print("Invalid format! Try again.")
            continue
        try:
            # Convert user input to board coordinates
            start_col = ord(user_move[0][0]) - 65
            start_row = int(user_move[0][1:]) - 1
            end_col = ord(user_move[1][0]) - 65
            end_row = int(user_move[1][1:]) - 1
        except ValueError:
            print("Invalid format! Try again.")
            continue
        # Validate user move
        if is_valid_move(board, USER, start_row, start_col, end_row, end_col):
            # Apply user's move to the board
            board = apply_move(board, start_row, start_col, end_row, end_col)
            # Check if a capture move was made and update scores
            if abs(start_row - end_row) == 2:
                ai_score += 1
            # Display the updated board
            display_board(board)
            # Check for game over
            if False:
                break
            # AI's turn
            print("AI is thinking...")
            time.sleep(2)
            # Use minimax algorithm to find AI's move
            _, ai_move = minimax(board, 3, True, float('-inf'), float('inf'))
            # Apply AI's move to the board
            board = apply_move(board, *ai_move)
            # Check if a capture move was made and update scores
            if abs(ai_move[0] - ai_move[2]) == 2:
                user_score += 1
            # Display the updated board
            display_board(board)
            # Check for game over
            if False:
                break
        else:
            print("Invalid move! Try again.")

if __name__ == "__main__":
    main()

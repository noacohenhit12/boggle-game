import random

BOARD_SIZE = 4


def generate_board():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return [[random.choice(letters) for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]


def print_board(board):
    print("\nBoggle Board:")
    for row in board:
        print(" ".join(row))


def is_valid_word(board, word):
    rows, cols = len(board), len(board[0])
    visited = [[False] * cols for _ in range(rows)]

    def dfs(r, c, index):
        if index == len(word):
            return True

        if r < 0 or r >= rows or c < 0 or c >= cols:
            return False

        if visited[r][c] or board[r][c] != word[index]:
            return False

        visited[r][c] = True

        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        for dr, dc in directions:
            if dfs(r + dr, c + dc, index + 1):
                return True

        visited[r][c] = False
        return False

    for i in range(rows):
        for j in range(cols):
            if dfs(i, j, 0):
                return True

    return False


def main():
    board = generate_board()
    print_board(board)

    while True:
        word = input("\nEnter a word to search (or 'exit'): ").upper()

        if word == "EXIT":
            break

        if is_valid_word(board, word):
            print(f"'{word}' found on the board! ✅")
        else:
            print(f"'{word}' not found ❌")


if __name__ == "__main__":
    main()


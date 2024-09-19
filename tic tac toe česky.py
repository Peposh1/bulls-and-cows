"""
projekt_2.py: Druhý projekt do Engeto Tic Tac Toe
author: Josef Lučan
email: peposh1@seznam.cz
discord: Josef Lučan#98945
"""

# 1. _________________________________________________________________________
# Úkol: Vypisuje uvítací zprávu a pravidla hry.
def print_welcome_message():
    print("Vítejte ve hře Tic Tac Toe")
    print("========================================")
    print("PRAVIDLA HRY:")
    print("Každý hráč může umístit jeden symbol")
    print("(nebo kámen) během svého tahu na 3x3 mřížku.")
    print("VÍTĚZEM se stává ten, kdo umístí tři")
    print("své symboly do:")
    print("* horizontální,")
    print("* vertikální nebo")
    print("* diagonální řady")
    print("========================================")
    print("Začněme hru")


# 2. _________________________________________________________________________
# Úkol: Zobrazuje aktuální stav hrací plochy.
def print_board(board):
    print("--------------------------------------------")
    
    for row in board:
        print("+---+---+---+")
        print("| " + " | ".join(row) + " |")
    
    print("+---+---+---+")
    print("============================================")


# 3. _________________________________________________________________________
# Úkol: Kontroluje, zda hráč s daným symbolem (X nebo O) nevyhrál.
def check_winner(board, mark):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]
    
    return any(all(cell == mark for cell in line) for line in win_conditions)


# 4. _________________________________________________________________________
# Úkol: Kontroluje, zda je hrací plocha plně obsazena (remíza).
def is_board_full(board):
    return all(cell in ["X", "O"] for row in board for cell in row)


# 5. _________________________________________________________________________
# Úkol: Umístí hráčův symbol na zadanou pozici, pokud je pozice platná.
def make_move(board, position, mark):
    row, col = divmod(position - 1, 3)
    
    if board[row][col] not in ["X", "O"]:
        board[row][col] = mark
        return True
    else:
        print("Tato pozice je již obsazena. Vyberte jinou.")
        return False


# 6. _________________________________________________________________________
# Úkol: Získává platný tah od hráče a ověřuje, zda je vstup správný.
def get_valid_move():
    while True:
        move = input("Zadejte číslo tahu (1-9): ")
        if move.isdigit() and 1 <= int(move) <= 9:
            return int(move)
        else:
            print("Neplatný vstup. Zadejte číslo mezi 1 a 9.")


# 7. _________________________________________________________________________
# Úkol: Hlavní funkce, která řídí průběh hry.
def main():
    print_welcome_message()

    board = [[" " for _ in range(3)] for _ in range(3)]
    
    current_player = "X"

    while True:
        print_board(board)
        print(f"Hráč {current_player} | ", end="")
        
        move = get_valid_move()

        if make_move(board, move, current_player):
            if check_winner(board, current_player):
                print_board(board)
                print(f"Gratulujeme, hráč {current_player} VYHRÁL!")
                break
            
            elif is_board_full(board):
                print_board(board)
                print("Hra skončila remízou!")
                break
            
            current_player = "O" if current_player == "X" else "X"


# 8. _________________________________________________________________________
# Úkol: Spustí hlavní funkci programu, když je skript spuštěn.
if __name__ == "__main__":
    main()
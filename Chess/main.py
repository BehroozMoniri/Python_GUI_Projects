import chess
import chess.engine
import pygame
import time
from tkinter import Tk, simpledialog, messagebox

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 800
SQ_SIZE = WIDTH // 8
PIECES = ['r', 'n', 'b', 'q', 'k', 'p', 'R', 'N', 'B', 'Q', 'K', 'P']
IMAGES = {}
LEVELS = ["Very Easy", "Easy", "Medium", "Hard", "Very Hard"]

# Load images
def load_images():
    for piece in PIECES:
        IMAGES[piece] = pygame.transform.scale(pygame.image.load(f'images/pieces/{piece}.png'), (SQ_SIZE, SQ_SIZE))

# Draw board and pieces
def draw_board(screen, board):
    colors = [pygame.Color("white"), pygame.Color("gray")]
    for r in range(8):
        for c in range(8):
            color = colors[(r + c) % 2]
            pygame.draw.rect(screen, color, pygame.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            piece = board.piece_at(chess.square(c, 7-r))
            if piece:
                screen.blit(IMAGES[piece.symbol()], pygame.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))

# Highlight squares
def highlight_squares(screen, board, valid_moves, selected_square):
    s = selected_square
    if s is not None:
        r, c = 7 - s // 8, s % 8
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE), 3)
        for move in valid_moves:
            if move.from_square == s:
                r, c = 7 - move.to_square // 8, move.to_square % 8
                pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE), 3)

def get_move(board, level):
    stockfish_path = "path/to/stockfish"
    engine = chess.engine.SimpleEngine.popen_uci(stockfish_path)
    levels = [0.1, 0.5, 1, 2, 3]
    level = levels[level]
    result = engine.play(board, chess.engine.Limit(time=level))
    engine.quit()
    return result.move

def get_user_input(prompt):
    root = Tk()
    root.withdraw()
    return simpledialog.askstring("Input", prompt)

def show_message(message):
    root = Tk()
    root.withdraw()
    messagebox.showinfo("Info", message)

def main():
    # Get game mode
    game_mode = get_user_input("Enter '1' for single player, '2' for two players: ")
    if game_mode == '1':
        difficulty = int(get_user_input(f"Select difficulty level (0: Very Easy, 1: Easy, 2: Medium, 3: Hard, 4: Very Hard): "))
    
    # Initialize game variables
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Chess")
    clock = pygame.time.Clock()
    board = chess.Board()
    valid_moves = list(board.legal_moves)
    move_log = []
    load_images()
    selected_square = None
    player = 0  # 0: white, 1: black
    running = True
    game_over = False
    
    # Game loop
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            elif e.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos()
                col = location[0] // SQ_SIZE
                row = location[1] // SQ_SIZE
                square = chess.square(col, 7-row)
                
                if selected_square is None:
                    if board.piece_at(square) and board.piece_at(square).color == board.turn:
                        selected_square = square
                else:
                    move = chess.Move(selected_square, square)
                    if move in valid_moves:
                        board.push(move)
                        move_log.append(move)
                        selected_square = None
                        valid_moves = list(board.legal_moves)
                        if board.is_checkmate():
                            show_message("Checkmate! You win!")
                            game_over = True
                        elif board.is_stalemate() or board.is_insufficient_material():
                            show_message("Draw!")
                            game_over = True
                        player = 1 - player
                    else:
                        selected_square = None
        if game_mode == '1' and player == 1 and not game_over:
            move = get_move(board, difficulty)
            board.push(move)
            move_log.append(move)
            valid_moves = list(board.legal_moves)
            if board.is_checkmate():
                show_message("Checkmate! Computer wins!")
                game_over = True
            elif board.is_stalemate() or board.is_insufficient_material():
                show_message("Draw!")
                game_over = True
            player = 1 - player
        
        draw_board(screen, board)
        highlight_squares(screen, board, valid_moves, selected_square)
        pygame.display.flip()
        clock.tick(15)
    
    pygame.quit()

if __name__ == "__main__":
    main()
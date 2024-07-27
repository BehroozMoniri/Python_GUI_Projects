# from PIL import Image, ImageDraw, ImageFont
# import math

# # Constants
# PIECE_SIZE = 100
# PIECE_THICKNESS = 10
# BACKGROUND_COLOR = (0, 0, 0, 0)
# COLOR_BLACK = (0, 0, 0)
# COLOR_WHITE = (255, 255, 255)
# OUTLINE_COLOR = (0, 0, 0)
# FONT_SIZE = 30

# # Create a function to draw an isometric piece
# def draw_isometric_piece(draw, piece_type, color, outline_color):
#     width = HEIGHT = PIECE_SIZE
#     center = (width // 2, HEIGHT // 2)

#     if piece_type == 'p':  # Pawn
#         draw.polygon([
#             (center[0] - 10, center[1] + 20),
#             (center[0] + 10, center[1] + 20),
#             (center[0] + 15, center[1] - 10),
#             (center[0] - 15, center[1] - 10)
#         ], fill=color, outline=outline_color)
#         draw.ellipse([(center[0] - 10, center[1] - 30), (center[0] + 10, center[1] - 10)], fill=color, outline=outline_color)
#     elif piece_type == 'r':  # Rook
#         draw.rectangle([(center[0] - 15, center[1] + 10), (center[0] + 15, center[1] - 10)], fill=color, outline=outline_color)
#         draw.rectangle([(center[0] - 10, center[1] - 30), (center[0] + 10, center[1] - 10)], fill=color, outline=outline_color)
#     elif piece_type == 'n':  # Knight
#         draw.polygon([
#             (center[0] - 15, center[1] + 10),
#             (center[0] + 15, center[1] + 10),
#             (center[0] + 10, center[1] - 10),
#             (center[0] - 10, center[1] - 10)
#         ], fill=color, outline=outline_color)
#         draw.ellipse([(center[0] - 10, center[1] - 20), (center[0] + 10, center[1] - 10)], fill=color, outline=outline_color)
#     elif piece_type == 'b':  # Bishop
#         draw.polygon([
#             (center[0] - 15, center[1] + 10),
#             (center[0] + 15, center[1] + 10),
#             (center[0], center[1] - 20)
#         ], fill=color, outline=outline_color)
#         draw.ellipse([(center[0] - 10, center[1] - 30), (center[0] + 10, center[1] - 10)], fill=color, outline=outline_color)
#     elif piece_type == 'q':  # Queen
#         draw.polygon([
#             (center[0] - 20, center[1] + 10),
#             (center[0] + 20, center[1] + 10),
#             (center[0] + 15, center[1] - 20),
#             (center[0] - 15, center[1] - 20)
#         ], fill=color, outline=outline_color)
#         draw.ellipse([(center[0] - 15, center[1] - 30), (center[0] + 15, center[1] - 10)], fill=color, outline=outline_color)
#     elif piece_type == 'k':  # King
#         draw.rectangle([(center[0] - 15, center[1] + 10), (center[0] + 15, center[1] - 10)], fill=color, outline=outline_color)
#         draw.rectangle([(center[0] - 10, center[1] - 30), (center[0] + 10, center[1] - 10)], fill=color, outline=outline_color)

# # Create a function to generate a piece image
# def generate_piece_image(piece_type, color, filename):
#     image = Image.new('RGBA', (PIECE_SIZE, PIECE_SIZE), BACKGROUND_COLOR)
#     draw = ImageDraw.Draw(image)
#     draw_isometric_piece(draw, piece_type, color, OUTLINE_COLOR)
#     image.save(filename)

# # Generate and save images for each piece
# pieces = ['p', 'r', 'n', 'b', 'q', 'k']
# colors = {'black': COLOR_BLACK, 'white': COLOR_WHITE}

# for piece in pieces:
#     generate_piece_image(piece, colors['black'], f'{piece}.png')
#     generate_piece_image(piece.upper(), colors['white'], f'{piece.upper()}.png')

# print("Intricate isometric chess pieces generated and saved.")
from PIL import Image, ImageDraw, ImageFont

# Constants
PIECE_SIZE = 100
BACKGROUND_COLOR = (0, 0, 0, 0)  # Transparent background
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
OUTLINE_COLOR = (0, 0, 0)

# Draw simple representations of chess pieces
def draw_piece(draw, piece_type, color):
    width, height = PIECE_SIZE, PIECE_SIZE
    center_x, center_y = width // 2, height // 2

    if piece_type == 'p':  # Pawn
        draw.ellipse([(center_x - 10, center_y - 20), (center_x + 10, center_y)], fill=color, outline=OUTLINE_COLOR)
        draw.rectangle([(center_x - 5, center_y), (center_x + 5, center_y + 20)], fill=color, outline=OUTLINE_COLOR)
    elif piece_type == 'r':  # Rook
        draw.rectangle([(center_x - 15, center_y - 20), (center_x + 15, center_y + 20)], fill=color, outline=OUTLINE_COLOR)
        draw.rectangle([(center_x - 15, center_y + 20), (center_x + 15, center_y + 30)], fill=color, outline=OUTLINE_COLOR)
    elif piece_type == 'n':  # Knight
        draw.polygon([(center_x - 15, center_y + 10), (center_x + 15, center_y + 10), (center_x + 10, center_y - 10), (center_x - 10, center_y - 10)], fill=color, outline=OUTLINE_COLOR)
        draw.ellipse([(center_x - 10, center_y - 10), (center_x + 10, center_y)], fill=color, outline=OUTLINE_COLOR)
    elif piece_type == 'b':  # Bishop
        draw.polygon([(center_x - 10, center_y + 10), (center_x + 10, center_y + 10), (center_x, center_y - 10)], fill=color, outline=OUTLINE_COLOR)
        draw.ellipse([(center_x - 10, center_y - 10), (center_x + 10, center_y)], fill=color, outline=OUTLINE_COLOR)
    elif piece_type == 'q':  # Queen
        draw.polygon([(center_x - 15, center_y + 10), (center_x + 15, center_y + 10), (center_x + 10, center_y - 10), (center_x - 10, center_y - 10)], fill=color, outline=OUTLINE_COLOR)
        draw.ellipse([(center_x - 10, center_y - 20), (center_x + 10, center_y - 10)], fill=color, outline=OUTLINE_COLOR)
    elif piece_type == 'k':  # King
        draw.rectangle([(center_x - 10, center_y - 20), (center_x + 10, center_y)], fill=color, outline=OUTLINE_COLOR)
        draw.rectangle([(center_x - 5, center_y), (center_x + 5, center_y + 10)], fill=color, outline=OUTLINE_COLOR)

def generate_piece_image(piece_type, color, filename):
    image = Image.new('RGBA', (PIECE_SIZE, PIECE_SIZE), BACKGROUND_COLOR)
    draw = ImageDraw.Draw(image)
    draw_piece(draw, piece_type, color)
    image.save(filename)

# Generate and save images for each piece
pieces = ['p', 'r', 'n', 'b', 'q', 'k']
colors = {'black': COLOR_BLACK, 'white': COLOR_WHITE}

for piece in pieces:
    #generate_piece_image(piece, colors['black'], f'{piece}.png')
    generate_piece_image(piece.upper(), colors['white'], f'{piece.upper()}.png')

print("Standard chess pieces generated and saved.")


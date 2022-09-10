import pygame
import sys
import numpy as np

pygame.init()

WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
BD_ROWS = 3
BD_COL = 3
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
X_WIDTH = 25
X_SPACE = 55

# rgb: red green blue
RED = (255, 0, 0)
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_CLR = (239, 231, 200)
X_CLR = (66, 66, 66)

game_over=False

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIC TAC TOE')
screen.fill(BG_COLOR)

# console board
board = np.zeros((BD_ROWS, BD_COL))
# print(board)


def xando():
    for row in range(BD_ROWS):
        for col in range(BD_COL):
            if board[row][col] == 1:
                pygame.draw.circle(screen, CIRCLE_CLR, (int(
                    col*200+100), int(row*200+100)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, X_CLR, (col*200+X_SPACE, row*200 +
                                 200-X_SPACE), (col*200+200-X_SPACE, row*200+X_SPACE), X_WIDTH)
                pygame.draw.line(screen, X_CLR, (col*200+X_SPACE, row*200+X_SPACE),
                                 (col*200+200-X_SPACE, row*200+200-X_SPACE), X_WIDTH)


def lines():
    # Horizontal line 1
    pygame.draw.line(screen, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH)
    # Horizontal line 2
    pygame.draw.line(screen, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH)
    # Vertical line 1
    pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH)
    # Vertical line 2
    pygame.draw.line(screen, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)

# marking of squares


def mark_square(row, col, player):
    board[row][col] = player

# checking if squares are available


def available_square(row, col):
    return board[row][col] == 0

# checking if the board is full


def board_full():
    for row in range(BD_ROWS):
        for col in range(BD_COL):
            if board[row][col] == 0:
                return False
    return True


# checking winner
def check_win(player):

    for col in range(BD_COL):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            vertical_line(col, player)
            return True

    for row in range(BD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            horizontal_line(row, player)
            return True

    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        asc_diagonal(player)
        return True

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        dsc_diagonal(player)
        return True

    return False


def vertical_line(col, player):
    posx = col*200+100

    if player == 1:
        color = CIRCLE_CLR
    elif player == 2:
        color = X_CLR

    pygame.draw.line(screen, color, (posx, 15), (posx, HEIGHT-15), 15)


def horizontal_line(row, player):
    posy = row*200+100

    if player == 1:
        color = CIRCLE_CLR
    elif player == 2:
        color = X_CLR

    pygame.draw.line(screen, color, (15, posy), (WIDTH-15, posy), 15)


def asc_diagonal(player):

   if player == 1:
        color = CIRCLE_CLR
   elif player == 2:
        color = X_CLR

   pygame.draw.line(screen, color, (15,HEIGHT-15), (WIDTH-15,15), 15)


def dsc_diagonal(player):
   if player == 1:
        color = CIRCLE_CLR
   elif player == 2:
        color = X_CLR

   pygame.draw.line(screen, color, (15,15), (WIDTH-15,HEIGHT-15), 15)


# restarting the game
def restart():
    screen.fill(BG_COLOR)
    lines()
    for row in range(BD_ROWS):
        for col in range(BD_COL):
            board[row][col]=0

# calling the function lines
lines()
player = 1
# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

            mouse_x = event.pos[0]
            mouse_y = event.pos[1]

            clicked_row = int(mouse_y//200)
            clickes_col = int(mouse_x//200)

            if available_square(clicked_row, clickes_col):
                if player == 1:
                    mark_square(clicked_row, clickes_col, 1)
                    if check_win(player):
                        game_over=True
                    player = 2
                elif player == 2:
                    mark_square(clicked_row, clickes_col, 2)
                    if check_win(player):
                        game_over=True
                    player = 1
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_r:
                restart()
                game_over=False
    
        xando()

        # print(board)

    pygame.display.update()

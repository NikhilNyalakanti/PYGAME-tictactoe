import pygame
from pygame.locals import *
import sys
import time


board=[[None]*4,[None]*4,[None]*4,[None]*4]
XO='x'
winner=None
draw=None
width=400
height=400
line_color=(0,0,0)
white=(255,255,255)
pygame.init()

screen = pygame.display.set_mode((width, height + 100))
pygame.display.set_caption("TIC TAC TOE 4*4 Using PYGAME")
#print(pygame.display.Info())
initaiting_window = pygame.image.load("C:/Users/NIKHIL/Downloads/tictactoe2.png")
initaiting_window = pygame.transform.scale(initaiting_window, ((width, height + 100)))
x_img = pygame.image.load("C:/Users/NIKHIL/Downloads/x2.png")
o_img = pygame.image.load("C:/Users/NIKHIL/Downloads/o2.png")
x_img = pygame.transform.scale(x_img, (50, 50))
o_img = pygame.transform.scale(o_img, (50, 50))

def game_initiating_window():
    screen.blit(initaiting_window, (0, 0))
    pygame.display.update()
    time.sleep(2)
    screen.fill(white)
    pygame.draw.line(screen, line_color, (width / 4, 0), (width / 4, height), 5)
    pygame.draw.line(screen, line_color, (width / 2, 0), (width / 2, height), 5)
    pygame.draw.line(screen, line_color, (width / 4 * 3, 0), (width / 4 * 3, height), 5)
    pygame.draw.line(screen, line_color, (0, height / 4), (width, height / 4), 5)
    pygame.draw.line(screen, line_color, (0, height / 2), (width, height / 2), 5)
    pygame.draw.line(screen, line_color, (0, height / 4 * 3), (width, height / 4 * 3), 5)

    pygame.display.update()
    #time.sleep(10)
    draw_status()

def draw_status():
    global draw,winner
    if winner is None:
        message=XO.upper()+"'s turn"
    else:
        message=winner.upper()+"  Won the game!"
    if draw:
        message="Game Draw!"

    font = pygame.font.Font(None, 30)

    text = font.render(message, 1, (255, 0, 0))

    screen.fill((0, 255, 0), (0, 400, 400, 100))
    text_rect = text.get_rect(center=(width / 2, 450))
    screen.blit(text, text_rect)
    pygame.display.update()
    time.sleep(1)


def check_win():
    global winner,draw,board
    for row in range(0, 4):
        if ((board[row][0] == board[row][1] == board[row][2] == board[row][3]) and (board[row][0] != None)):
            winner = board[row][0]
            pygame.draw.line(screen, (250, 0, 0),
                         (0, (row + 1) * height / 4 - height / 8),
                         (width, (row + 1) * height / 4 - height / 8),
                         4)
            break

    for col in range(0, 4):
        if ((board[0][col] == board[1][col] == board[2][col] == board[3][col]) and (board[0][col] is not None)):
            winner = board[0][col]
            pygame.draw.line(screen, (250, 0, 0), ((col + 1) * width / 4 - width / 8, 0),
                         ((col + 1) * width / 4 - width / 8, height),5)
            break

    if (board[0][0] == board[1][1] == board[2][2] == board[3][3]) and (board[0][0] is not None):
        winner = board[0][0]
        pygame.draw.line(screen, (250, 70, 70), (20,20), (380, 380), 4)

    elif (board[0][3] == board[1][2] == board[2][1] == board[3][0]) and (board[0][3] is not None):
        winner = board[0][3]
        pygame.draw.line(screen, (250, 70, 70), (20,380),(380,20), 4)

    elif (all([all(row) for row in board]) and winner is None):
        draw = True
    draw_status()

def drawXO(row,col):
    global XO
    if(row==1):
        posy=25
    if(row==2):
        posy=height/4+20
    if(row==3):
        posy=height/2+20
    if (row == 4):
        posy=height/4*3+20
    if(col==1):
        posx=20
    if(col==2):
        posx=width/4+20
    if(col==3):
        posx=width/2+20
    if (col == 4):
        posx=width/4*3+20
    board[row-1][col-1]=XO
    if(XO=='x'):
        screen.blit(x_img,(posx,posy))
        XO='o'
    else:
        screen.blit(o_img,(posx,posy))
        XO='x'
    pygame.display.update()



def user_click():
    x,y=pygame.mouse.get_pos()
    if x<width/4:
        col=1
    if (x<width/2 and x>width/4):
        col=2
    if (x<width/4*3 and x>width/2):
        col=3
    if (x<width and x>width/4*3):
        col=4
    if x>width:
        col=None
    if y<height/4:
        row=1
    if (y<height/2 and y>height/4):
        row=2
    if (y<height/4*3 and y>height/2):
        row=3
    if (y<height and y>height/4*3):
        row=4
    if y>height:
        row=None
    print("x=",x," y=",y)
    print("row=",row," col=",col )
    if(row and col and (board[row-1][col-1] is None)):
        global XO
        drawXO(row,col)
        check_win()
def reset_game():
    global board,XO,draw,winner
    board=[[None]*4,[None]*4,[None]*4,[None]*4]
    X0='x'
    winner=None
    draw=False
    time.sleep(3)
    game_initiating_window()



game_initiating_window()
while(True):
    for event in pygame.event.get():
        #print(event.type)
        if event.type== QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==MOUSEBUTTONDOWN:
            user_click()
            if(winner or draw):
                reset_game()

    pygame.display.update()

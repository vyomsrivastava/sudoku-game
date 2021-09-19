# importing the pygame
import pygame
# importing request library (its a library used in python to get calls and post calls)
import requests
# setting up the width and backgorund color of the window

WIDTH = 550
background_color = (38, 38, 38)
orignal_grid_element = (52, 31, 151)

#adding api in our sudoku game
response = requests.get("https://sugoku.herokuapp.com/board?difficulty=easy")
grid = response.json()['board']
grid_original = [[grid[x][y] for y in range(len(grid[0]))] for x in range(len(grid))]

#initializing pygame
def main():
    pygame.init 
    win = pygame.display.set_mode((WIDTH, WIDTH)) # creating the window
    pygame.display.set_caption("Sudoku") #giving caption
    win.fill(background_color) # filling the window with background color
    myfont = pygame.font.SysFont('Comic Sans MS', 35)# filling the window with background color

    # creating grid
    for i in range(0,10):
        if(i%3 == 0):
                #drwaing the block line (vertical)
                pygame.draw.line(win, (255, 255, 255), (50 + 50*i, 50), (50 + 50*i ,500 ), 4 )
                #(vertical)
                pygame.draw.line(win, (255, 255, 255), (50, 50 + 50*i), (500, 50 + 50*i), 4 )
        #drwaing vertical line
        pygame.draw.line(win, (166, 166, 166), (50 + 50*i, 50), (50 + 50*i ,500 ), 2 )
        #drwaing horizental line
        pygame.draw.line(win, (166, 166, 166), (50, 50 + 50*i), (500, 50 + 50*i), 2 )
    pygame.display.update()

    for i in range(0, len(grid[0])):
        for j in range(0, len(grid[0])):
            if(0<grid[i][j]<10):
                value = myfont.render(str(grid[i][j]), True, original_grid_element_color)
                win.blit(value, ((j+1)*50 + 15, (i+1)*50 ))
    pygame.display.update()

#adding the function that if we press the quit key then pygame window will close.
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

main()

import pygame
import random

pygame.init()


class Draw_info:

    BLACK =  0,0,0
    WHITE =  255, 255, 255, 255
    GREEN = 0,255, 0, 255
    RED = 255, 0, 0
    GREY = 128, 128, 128
    BG_COLOUR = WHITE
    SIDE_PADDING = 100 #50 PX on right, 50 px on left
    TOP_PADDING = 150


    def __init__(self, width, height, lst):
        self.widht = width
        self.height = height

        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Visualiser")

        self.set_list(lst)


    def set_list(self, lst):
        self.lst = lst
        self.max_val = max(lst)
        self.min_val = min(lst)

        self.bar_width = round((self.width - self.SIDE_PADDING )/ len(lst)) #determine how thick the bar charts will be
        self.bar_height = round((self.height - self.TOP_PADDING) /(self.max_val - self.min_val)) #max - min will tell me no. of values in the range.
        self.start_x =  self.SIDE_PADDING // 2  #where you will start drawing. Top left corner of screen in pygame is 0,0


    #generate starting list

def generate_starting_list(n, min_val, max_val):

        """generate random list of numbers t sort"""

        lst = []
        for i in range(n):
            value = random.randint(min_val, max_val)
            lst.append(value)
        return lst




def main():

    run = True
    clock = pygame.time.Clock() #determine how fast game will run

    #initialising the window and the random list
    n= 50
    min_val= 10
    max_val = 100

    lst = generate_starting_list(n, min_val, max_val)
    draw_info = Draw_info(800, 800)

    while run:
        clock.tick(60) #60 is max no of times this loop can run per second

        pygame.display.update() ##update the screen

        for event in pygame.event.get(): #will return a list of events that have occured since the last clock tick

            if event == pygame.QUIT:
                run == False

    pygame.quit()


if __name__ == '__main__':
    main()

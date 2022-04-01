
import pygame
import random

pygame.init()


class Draw_info:

    BLACK =  0,0,0
    WHITE =  255, 255, 255
    GREEN = 0,255, 0, 255
    BG_COLOUR = WHITE
    SIDE_PADDING = 100 #50 PX on right, 50 px on left
    TOP_PADDING = 150

    RED = 13, 98, 195
    DARK_RED = 199, 37, 67
    BORDEAUX = 178, 29, 80
    DARK_MAGENTA = 157, 23, 100
    PURPLE = 168, 37, 127
    MAGENTA = 181, 44, 153



    GRADIENTS = [ RED, DARK_RED,
                 BORDEAUX, DARK_MAGENTA,
                 PURPLE, MAGENTA ]


    def __init__(self, width, height, lst):
        self.width = width
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



def draw(draw_info):

    """A function that draws the screen"""

    #first fill the entire screen with a colour to "draw over" anything that has
    #been drawn previously
    draw_info.window.fill(draw_info.BG_COLOUR)
    draw_list(draw_info)
    pygame.display.update()


def draw_list(draw_info):

    """A function that draws the list on the screen"""

    #need to determin the height of the element and the width of the element and then draw a rectangle representing it

    lst = draw_info.lst
    for i, val in enumerate(lst):
        x = draw_info.start_x + i*draw_info.bar_width  #bar width

        #val- draw_info.min_val  tells us how much larger we are than the minimum
        y = draw_info.height - (val- draw_info.min_val )* draw_info.bar_height #determine the height of the rectangle.

        #there are 6 colours in the gradients list. For each bar in the lst we are going to draw, we will assign a colour from the gradient list to that bar
        # when we have iterated throguh the gradient list once, we shall start reassiging gradients from the very beginning of the gradients list.
        colour = draw_info.GRADIENTS[i % 6]
        pygame.draw.rect(draw_info.window, colour, (x, y, draw_info.bar_width, draw_info.height))




def heap_sort(lst, n, i):

    """A function that implements the heap sort algorithm"""


    largest = i
    l = 2*i + 1 #eft child
    r = 2 * i + 2 #right child


    #see if left child of root exists and is greater than parent:
    if l < n and lst[i] < lst[l]:
        largest = l


    #see if right child of root exists and is greater than parent:
    if r < n and lst[i] < lst[r]:
        largest = r

    #change parent if needed
    if largest != i:
        lst[i], lst[largest], = lst[largest], lst[i] #swap the two nodes

        #recursively call this function to heapify the parent node:
        heap_sort(lst, n, largest)


#main function to sort a given array

def heapSort(lst):
    n = len(lst)

    #build a max heap
    # Since last parent will be at ((n//2)-1) we can start at that location.

    for i in range(n //2-1, -1, -1):
        heap_sort(lst, n, i)

    #one by one extract elements
    for i in range(n-1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i] #swap
        heap_sort(lst, i, 0)





def main():

    run = True
    clock = pygame.time.Clock() #determine how fast game will run

    #initialising the window and the random list
    n= 50
    min_val= 10
    max_val = 100

    lst = generate_starting_list(n, min_val, max_val)
    draw_info = Draw_info(800, 800, lst)

    while run:
        clock.tick(60) #60 is max no of times this loop can run per second

        pygame.display.update() ##update the screen

        draw(draw_info)

        for event in pygame.event.get(): #will return a list of events that have occured since the last clock tick

            if event.type == pygame.QUIT:
                run = False

    pygame.quit()





if __name__ == '__main__':
    main()



#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

from main import draw_info, draw_list

def heap_sort(array, n, i):

    """A function that creates a heap"""

    largest = i
    l = 2*i + 1 #eft child
    r = 2 * i + 2 #right child


    #see if left child of root exists and is greater than parent:
    if l < n and array[i] < array[l]:
        largest = l


    #see if right child of root exists and is greater than parent:
    if r < n and array[i] < array[r]:
        largest = r

    #change parent if needed
    if largest != i:
        array[i], array[largest], = array[largest], array[i] #swap the two nodes

        #recursively call this function to heapify the parent node:
        heap_sort(array, n, largest)


#main function to sort a given array

def heapSort(array):
    
    """Function that sorts the array"""

    n = len(array)

    #build a max heap
    # Since last parent will be at ((n//2)-1) we can start at that location.

    for i in range(n //2-1, -1, -1):
        heap_sort(array, n, i)

    #one by one extract elements
    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i] #swap
        heap_sort(array, i, 0)




def bubble_sort(draw_info, ascending = True):
    
    """A function that implements the bubble sorting algorithm,
    defaults to ascending order"""
    
    lst = draw_info.lst
    for i in range(len(lst)-1):
        for j in range(len(lst) -1 -i):
            num1 = lst[j]
            num2 = lst[j + 1]
            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                lst[j], lst[j+1] = lst[j+1], lst[j]
                #draw list
                draw_list(draw_info)
                yield True #call this function every time you want a swap to occur
                #creates a generator. Yield will pause but store the current state of the function
    return lst

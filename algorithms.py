
def heap_sort(array, n, i):

    """A function that implements the heap sort algorithm"""


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
    n = len(array)

    #build a max heap
    # Since last parent will be at ((n//2)-1) we can start at that location.

    for i in range(n //2-1, -1, -1):
        heap_sort(array, n, i)

    #one by one extract elements
    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i] #swap
        heap_sort(array, i, 0)

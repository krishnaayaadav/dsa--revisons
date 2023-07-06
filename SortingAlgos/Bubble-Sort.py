

ids = (13, 46, 24, 52, 20, 9)


# bubble sort pushes maximum to the last
max = 13
current_elm = 46
 

 
def bubbleSort(arr):
    n = len(arr)
    # print(arr)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n-1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
    return arr
 
 
# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]
 
# print(bubbleSort(arr))


def BubbleSort(arr):
    temp = arr
    arr = list(arr)
    arr_len = len(arr)

    for i in range(arr_len):

        for j in range(1, arr_len-1): # 
            
            prev = arr[j-1] # previous element
            next = arr[j] # next element

            # print(f'previous: {prev} next: {next}')

            if(prev>next):
                print(f'previous: {prev} next: {next}')
                arr[j-1], arr[j] = arr[j], arr[j-1]
                print(f'previous: {prev} next: {next} \n')

                # print(prev)

            
    return f'\n {temp} \n sorted {arr}'

            # if()


roll = [12,34,34,45,23,1,23,45,56,77,46,4,132,13,32,2,4,556,7,89,98,65,777]

# print(not(12 < 5)) # 12 < 5:false >> True

# print('sorted' , BubbleSort(ids))


def bubble_sorts(arr):
    size = len(arr)

    for i in range(0, size-1):

        for j in range(0, size-i-1):
            print(j, end=' ')

            if(arr[j] > arr[j+i]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print()
    
    return arr

print(bubble_sorts(list(ids)))
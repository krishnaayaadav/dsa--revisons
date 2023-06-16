

def binary_search(arr, key):

    st = 0
    end = len(arr)-1
    mid = st + (end - st)//2

    while st<= end:
        item = arr[mid]
        
        # if key and arr[mid] is equal
        if (key == item):
            return mid
        
        # if key > arr[mid] is greater
        elif(key>item):
            st = mid + 1
        
        # if key > arr[mid] is less than
        else: 
            end = mid-1
        
        # update mid
        mid = st + (end - st)//2

    return -1

# arr = tuple(range(1,145))
arr = [12,23,34,45,56]
key = 57
result = binary_search(arr, key)


print(result)




""" 
 find mid
 compare mid with given
 if equals than return
 if not than decide portion and do the same steps

"""


def binary_search(arr, key): # 1 2 3 4 5 6 7 8 9 10
    
    st  = 0 
    end = len(arr)-1
    mid =  st + (end-st) # st + end // 2 

    while st<= end:
        mid_val = arr[mid]

        if(mid_val == key):
            return mid
        
        elif(mid_val<key):
            st = mid + 1
        else:
            end = mid -1
        
        mid = st + (end - st)

    return -1

stu_ids = list(range(1,101)) # range(1,101) 1 2 3 4 100

key = 405
# print(stu_ids)
# index = binary_search(arr=stu_ids, key=key)

def linear_search(arr, key):

    for i in range(0, len(arr)):
        elm = arr[i]

        if(elm == key):
            return i
    return -1

result = linear_search(stu_ids, 45)


# print(f'{key} is avaible at index: {index}')

print(result)


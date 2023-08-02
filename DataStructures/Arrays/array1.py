
from array import array

stu_ids = array('i', [1,2,3,4,5,6,7,8,9,10,45,89,65,87,54,98,2222,65,54,98,12,13,10])

# largest elm # smallest elm second largest and smallest

# find duplicate and remove duplicate with _
nums = list(range(1, 10)) + list(range(1, 10)) + list(range(1, 10))
# rolls = array('i', [n for n in nums ])

print()
def remove_duplicates(arr, arr_len):
    arr = sorted(arr)
    i = 0
    tempArr = []

    while i < arr_len:
        elm = arr[i]
        tempArr.append(elm)
        count = arr.count(elm)
        if(count > 1): # 2
            i += count # 0 + 2: 2
        else:
            i += 1
    n = arr_len - len(tempArr)
    underscores = ["_" for _ in range(0,n)]

    tempArr.extend(underscores)
    return tempArr
        

# result = remove_duplicates(arr=nums, arr_len=len(nums))

# print(result)

def removeDuplicates( nums: list[int]) -> int:

        i       = 0
        tempArr = []
        arr_len = len(nums)
        nums = sorted(nums)

        while i < arr_len:
            elm = nums[i]
            count = nums.count(elm)

            tempArr.append(elm)

            if(count > 1):
                i += count
            else:
                i +=  1
        
        n = arr_len - len(tempArr)

        # under_scores = [ for n in range(0, n)]

        # tempArr.extend(under_scores)
        return len(tempArr), tempArr

# nums = [1,1,2]

# results  = remove_duplicates(nums, len(nums))
results  = removeDuplicates(nums)

print(results)
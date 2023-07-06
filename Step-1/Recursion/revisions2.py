#  1 to n cmp
# n to 1  cmp
# find some n  cmp
# find average of 1 to N cmp 
# find smallest element of array using recursion  cmp 
# find greatest element                           cmp
# find duplicate elements of arra using recursion cmp

# reverse of number n = 123
# check weahter number is  palindrom  not


# without using backtracking
nums = set()
def display_1_to_N(n, i, nums):
    # n = 10,
    # i = 1 1+1: 2 

    if (i>n): # 1 >10: false 2>10L false 11>10
        return 
    
    print(i, end=' ')  # 1 2 

    # calling same function by passing n and i+1
    display_1_to_N(n=10, i=i+1, nums=nums)
    return nums.add(i)


# result = display_1_to_N(n=10, i=1, nums=nums)

# print(nums)

def displayN_to_1(n:int):

    if (n<= 0): # 0<= 0:true
        return
    
    displayN_to_1(n-1)
    print(n)
    # return n 

# displayN_to_1(10)

# find sum of number using recursion

# n = 5 : sum: 1 + 2 + 3 + 4 + 5

def find_sum_of_N(N:int, total_sum):

    if (N <= 0): # n = 0
        return 0
    # 
    total_sum = N +   find_sum_of_N(N-1, total_sum) 

    return total_sum
    
# sumss = find_sum_of_N(10, 0)
# print(sumss)

def find_some_without_using_any_parameters(N): # 5

    if (N <= 0):
        return 0
    
    return N +  find_some_without_using_any_parameters(N-1)


# print(find_some_without_using_any_parameters(10))

def find_average_of_N(N):

    if (N<= 0):
        return 0
    
    if N == 10:
        res = (N + find_average_of_N(N-1)) / 10
    res = N + find_average_of_N(N-1)
    
    return res

# print(find_average_of_N(10) / 10)


from array import array

"""
  Approach to find smallest element of array of unsorted array
          For Unsorted Array
          1.will iterate each element
          2. We assume that first is the smallest one
          3. we comparare smallest elm if current while performing iteration
          4. if current is less than smallest then update the value of smallest
          keep repeating these step until we reach the last elements

"""

employee_salary = array('i', [11000, 12000, 340000,100,100,200, 2000, 565,565,  45000, 78000, 54000, 8000, 80000,7000])

# find smallest elements of array using recursion
def find_smallest_elm_in_arr(arr:array, arr_len:int): # 5 -1: 4  3 2 1 0

    if arr_len <= 0: # 1
        return 0
    
    #          arr[0]
    index = find_smallest_elm_in_arr(arr, arr_len-1)
    smallest = arr[index]

    if (arr[arr_len]< smallest): # arr[1] < arr[0]: 
        index = arr_len # updating the smallest index here

    return index

# index =  find_smallest_elm_in_arr(arr=employee_salary, arr_len=len(employee_salary) - 1 )
# print(employee_salary[index])

def find_largest_of_arr(arr:array, arr_len:int):

    if(arr_len <= 0): # 9 8 7 6 5 4 3 2 1 0
        return arr[0]
    
    elm = find_largest_of_arr(arr, arr_len-1)

    if(arr[arr_len] > elm):
        elm = arr[arr_len]
    
    return elm

# largest = find_largest_of_arr(employee_salary, arr_len=len(employee_salary) -1 )

# print(largest)

# find duplicate elements from array

"""
   Approach: 1. We will iterate through each elements
             2. And we will count the occurenece of the element if occurence is greater than 1 it duplicate

"""
dup_elm  = set()


def find_duplicate_of_arr(arr:array, arr_len:int,dup_elm=None):

    if(arr_len < 0):
        return dup_elm
    #          getting dup elm here
    dup_elm = find_duplicate_of_arr(arr, arr_len-1, dup_elm)
    if(arr.count(arr[arr_len]) > 1):
        dup_elm.add(arr[arr_len])

    return dup_elm
    

# result = find_duplicate_of_arr(arr=employee_salary, arr_len=len(employee_salary) -1, dup_elm=dup_elm)

# print(result)

# find reverse of number using recursion
#  n = 123 321  123//10 12 12//10: 1//10: 1
def reverse_of_num(n, rev=0):

    if(n == 0):
        return rev
    
    rev = rev *10 + n%10
    return reverse_of_num(n//10, rev)

# result = reverse_of_num(123)

# print(result)


def is_palindrom(n, tempN, rev=0):

    if (tempN == 0):
        return True if(rev == n) else False
    
    rem = tempN % 10
    rev = rev *10 + rem
    return is_palindrom(n ,tempN//10, rev)

# print(is_palindrom(121, 121))
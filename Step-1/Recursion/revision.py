
# # 1 -  ? 
import sys

# def display(n):

#     if(n < 1):
#         return 
#     # reciving we perform some thing into
#     num = display(n-1)

#     print(n)

#     return n

# # (display(5))


# def find_sum_of_n(total_sum, N):

#     if(N == 0):
#         return N
#     #            1           +  0 = 1
#     total_sum = N + find_sum_of_n(total_sum, N-1)

#     return total_sum

# # print(find_sum_of_n(0 , 5))

sys.setrecursionlimit(10**6)


# def sum_of_series(N):

#     if( N <= 0):
#         return 0
    
#     return N**3 + sum_of_series(N-1)

# # print(sum_of_series(50000))

# def sumOfSeries(N):
        
#         if(N <= 0):
#             return 0
        
#         return N**3 + sumOfSeries(N-1)
# series = sum_of_series(50000)
# print(series, series == 1562562500625000000)

 
# n = 5 + 4 + 3+ 2+ 1

# without using loop 

def sum_of_1_n(total_sum, n):

    if n<= 0: # n = 0 
        return n
    
    total_sum = n +  sum_of_1_n(total_sum, n-1)
    # 0       = 1 + 0: 1
    # return 1
 
    return total_sum

result = sum_of_1_n(0,5)
print(result)

def sum_of_N(n):

    if n <= 0:
        return 0
    
    return n + sum_of_N(n-1)

result2 = sum_of_N(5)


print(result2)


def sumOfSeries(N):
        if(N <= 0):
            return 0
        return N**3 + sumOfSeries(N-1)
sums = sumOfSeries(50000)

print( sums == 1562562500625000000, f'\n {1562562500625000000} \n {sums}' )

# without using any loop
# factorial 5 =  5*4*3*2*1 = 120

def find_factorial_ofN(n):
    if(n<= 0):
        return 0
    
    if (n== 1):
        return n
    
    # return  0*  0
    return n * find_factorial_ofN(n-1)

# fact = find_factorial_ofN(0)

# print(fact)

rolls = [5,4,3,2,1]

def arr_reverse(arr, counter, n):
    arr_len = len(arr) - 1

    if counter >  arr_len // 2:
        return arr
    # swapping here
    arr[n], arr[arr_len -n] = arr[arr_len - n], arr[n]
     
     # calling the same function and return it returned value
    return arr_reverse(arr, counter+1, n-1)

arr2 = arr_reverse(rolls, 1, len(rolls) -1)

print(arr2)
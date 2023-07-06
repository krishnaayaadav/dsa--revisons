
# find some numbers using recursion


def sum_of_n(N):

    if(N == 1):
        return 1
    
    # calling here same function with n-1
    temp = sum_of_n(N-1)

    return temp + N
   
    

print(sum_of_n(5))
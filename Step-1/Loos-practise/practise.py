# Example 1: Print the first 10 natural numbers using for loop.

# Natuaral Number: means all positve numbers excluding 0

def first_n_natural_num(num): # num= 10
    natual_nums = []
    i = 1

    while i<=num:
        # print(i, end=' ')
        natual_nums.append(i)

        i+= 1
    print(f'first {num} natural number are: {natual_nums}')
    return natual_nums

# first_n_natural_num(40)

# Example 2: Python program to print all the even numbers within the given range.

def all_even_in_range(range_st, range_end):

    even_nums = []
    step_size = 1

    if range_st%2 == 0: #
        step_size = 2   # for optimization to reduce no of iterations


    for num in range(range_st, range_end, step_size):
        if(num %2 == 0):
            even_nums.append(num)
        
    print(f'\n Even number with range of: {range_st} to {range_end}: \n {even_nums}')
    return even_nums

# all_even_in_range(range_st=11, range_end=21)


# Example 3: Python program to calculate the sum of all numbers from 1 to a given number.


def calculate_sum_of_nums_1_to_N(N):

    sum  = 0

    for num in range(1, N+1):
        sum += num
    
    print(sum)
    return sum

# calculate_sum_of_nums_1_to_N(5)


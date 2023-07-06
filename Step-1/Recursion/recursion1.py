

def print_msg():

    print('\n Hello')
    print_msg()

# print_msg()

counter = 1 #main function <<1 <<2 <<3 <<1 <<2 <<3 << 4 <<5 <<6

def print_hello():
    
    global counter

    if(counter > 5): # 1>5: false, 2>5: false, 3>5: false 4>5:false, 5>5:false 6>5: true
        return
    else:
        print('hello') # hello hello hello hello hello
        counter += 1   # 2+1: 3+1: 4+1: 5+1: 6
        print_hello()  # calling the same function

# print_hello()

# print 1 to 10

def greet(n):
    # greet(4)
    # greet(3)
    # n = 3-1: 2
    # greet(2)
    #  n = 2 -1: 1 = 0
    # greet(0)

    if (n < 1): # 4 < 1:false 3<1: false 2<1: false 1<1: false 0 < 1:true

        return # here will return here

    print(n)    # 4 3 2 1

    # calling the same function
    greet(n-1)  # calling the same function

# greet(4)

# we have to print 1 to N 
# n = 4: 1 2 3 4

counter = 1 # 
def print_till_n(n): # 10-1: 9-1: 8-1: 7-1: 6-1: 5
 
    global counter # 1 2 3 4 5 6 11

    if(counter >n): # 1>10: false 2>9: 3>8: false: 4>8: false: 5>6: false 6>5:true 10>10:false 11>10:true
        return
    
    else:
        print(counter)     # 1 2 3 4 5 10
        counter += 1       # 1+1: 2+1: 3+1: 4+1: 5+1: 6: 10+1: 11
        print_till_n(n)  # calling the same function with n-1

# print_till_n(10)

# using recursion  n = 5 Output: 5 4 3 2 1
def printN_to_1(n): # 5 4  3 2 1 0

    if(n<1): # 5 < 1: false 4<1: false 3<1: false 2<1:false 1<1: false 0 < 1: true

        return  # return back from here
    else:
        print(n)  # 5 4 3 2 1

        # we calling the same function
        printN_to_1(n-1)   # 5-1: 4-1: 3-1: 2-1: 1-1: 0 

# printN_to_1(5)


# print(5)
    

# numbers from 1 to N without using any global variable

def printNum(i,n): 
    # i = 1+1: 2+1: 3+1: 4+1: 5+1: 6
    # n = 5

    # base condition
    if(i>n):         # i>n: 1>5: false: 2>5: false: 3>5: false 4>5: false: 5>5: false
        #  6>5:true
        # it will return back
        return
    else:

        print(i)    # 1 2 3 4 5

        # calling the same function by passing i+1, n
        printNum(i+1, n)

# printNum(1,5)

def diplayN_to_1(i, n):
    # i = 0  1 2 3 4+1: 5+1: 6
    # n = 5

    if(i>=n): # 0>5: false 1>5: 2>5: false: 3>5:false 4>5: false: 5>5: false

        return
    else: # 5 4 3 2 1 0
        print(n-i) # 5-0: 5 5-1: 4 5-2: 5-3: 5-4: 1

        # calling the same function 0+1: 1+1: 2
        diplayN_to_1(i+1, n)
    
diplayN_to_1(0, 5)
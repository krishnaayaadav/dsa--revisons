def nums(i, n):
    # i = 5 4  3 2 1 0
    # n = 5

    if(i<1):  # 5<0: false 4<0: false 3<0: false: 2<0: false 1<0: false 0<0

        return
    
    # otherwise
    # we calling the same func i-1, n
    nums(i-1, n) # << line is executed done
    print(i)     # << next line  done
                 # done

# nums(5, 5)

"""
   1
   2
   3

"""

# i = 5-1: 4-1: 3-1: 2-1: 1-1: 0

# nums(5,5) >> nums(4,5)<<  nums(3,5) << nums(2,5)  nums(1,5)<<  nums(0,5)

# n = 4 Ouptu: 1 2 3 4

def nums(i, n): # 1 

    if(i>n):
        return
    
    nums(i+1, n)
    print(i)

# nums(1,5)

# Always remember two thing what is expected ouput
# if you coming from top to bottom 5-1 so will have execute last statement fisrt everytime
# if you are coming from bottom to top 1-5 so will apply some(addition) there

def greets(n):

    if(n == 0):
        return 
    
    print('Hello')
    greets(n-1)
    print('World')

# greets(5)
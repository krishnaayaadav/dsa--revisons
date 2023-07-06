
"""

  * * * * *  >> rows
  * * * * *
  * * * * *
  * * * * *
  * * * * *
          ||
          columns  

          
 Approach:  to make any pattern: 
  1. is first count the number of rows and columns
  2. find relationship with rows and columns
      like i first row how many columns are ther
           then in second row how many columns and so on.
 
 
"""
n = 6

for i in range(1, n):
    for j in range(1,n):
        print('* ', end=' ')
    print()


"""

   *                 rows = 5
   *   *
   *   *   *
   *   *   *  *
   *   *   *  *   *  columns = 5


"""
print()
for i in range(1,n): # 1
    for j in range(1,n): # 1 1 2
        if(j<= i):
            print('* ', end=' ')
        
    print()

"""
   1              row=1 row = 2:  1 2 
   1  2 
   1  2  3
   1  2  3   4 
   1  2  3   4  5

"""

print()
for i in range(1,n):
    for j in range(1,n):
        if(j<=i):
            print(j, end=' ')
    print()


"""
   1    row = 1 1 , row =2: 2 
   2  2 
   3  3  3
   4  4  4  4 
   5  5  5  5  5

"""
print()
for i in range(1, n):
    for j in range(1,n):
        if(j<= i):

            print(i, end=' ')
    print()


"""
   1  2  3  4  5
   1  2  3  4
   1  2  3
   1  2 
   1

"""

print()
for i in range(1,6):
    for j in range(1, 7-i):
        print(j, end=' ')
    print()

"""
                    *
                *   *   *
            *   *   *   *    *
        *   *   *   *   *    *    *
    *   *   *   *   *   *    *    *   *
    

"""
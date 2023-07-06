
#  Problem Statement: Given an integer N, write a program to count the number of digits in N.


def find_digits_of_N(num):

    counter = 0

    temp = num

    while temp != 0:

        temp = temp // 10
        counter += 1
    digits = len(str(num))

    print(f'total number of digits in: {num} is: {counter} \n {digits}')

    #  another approach will be 
    
    return counter

# find_digits_of_N(23300100100)


def pos_neg(a, b, negative):
  response = False
  

  if(a < 0 and b >= 1 and negative == False):
    print('1')
    response = True
  
  elif(a>= 1 and b < 0 and negative == False):
    print('2')

    response = True
    
  elif(negative):
    if( a < 0 and b <0):
        print('3')
      
        response = True
   
    
 
    
  return response
    
# print(pos_neg(1,-1, True))
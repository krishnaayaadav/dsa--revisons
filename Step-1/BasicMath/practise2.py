

def check_divisible(*numbers, by:int):

    temp = list(set(numbers))
    hcf = 1

    l = len(temp)


    while by<= temp[0]:

        for i in range(0, l): # 18, 24 48
            num = temp[i]
            

            if(num % by != 0): # 18%2: 0, 24%2: 48: 0
                by += 1
                break

            else:
                temp[i] = num// by # updating the value
            
            if i == l-1:
                hcf =  hcf * by
                by += 1

    return hcf


# print(check_divisible(18, 24, 48, by=2))

def total_divisors(*num):

    toal = []
    temp = num
    p    = 2
    l = temp

    while p <= num[-1]:

        for i in range(0, l):
            num = temp[i]
            if( num % p == 0):
                temp[i] = temp[i] // p
            pass


def evenlyDivides (N):
        temp = N # 12
        
        counter = 0
        
        while temp != 0: # 23 != 0:true
            
            # finding here remainder
            lastN = temp % 10      # temp%10: 3
            
            if(N % lastN == 0): # checking that weahter temp % lastN == 0
                counter += 1
            
            temp = temp// 10 # updating temp N 
        
        return counter

# print(evenlyDivides(22074))




def sums(n):

    temp  = n
    total_sum = 0
    is_same = "No"

    while temp != 0:

        rem = temp% 10
        total_sum = total_sum + rem**3

        temp = temp // 10

    if total_sum == n:
        is_same = "Yes"
    
    return  is_same

# print(sums(371))

print(0%10, 0**3)

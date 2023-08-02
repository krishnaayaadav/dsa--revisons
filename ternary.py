
greatest = 123 if(123 >234) else 234


result = True if(123 == 321) else False
print(result)

num = -123
num = int(str(num).split('-')[1])
print('-123'.split('-'), num)

num =   int('-'+str(122334))
print(num)

print(1534236469 >> 32 )
print(2147483647 >> 32 )

def is_32_bin(num):
    try:
        bin_string = bin(num)
    except:
        return False
    
    if(len(bin(num)[2:]) <= 32):
        return True
    else:
        return False

print(is_32_bin(2**32))

print(1534236469 >> 30)

arr = list(range(1,1101))

counter = 0 #

while True:

    try:
        arr[counter] # if element exist
    except:
        break # if not than break loop

    else:
    
        counter += 1

print(counter, len(arr))

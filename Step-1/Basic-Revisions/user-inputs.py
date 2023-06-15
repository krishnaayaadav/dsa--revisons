# take inputs from user 

def input_handler(): # string input
    name = input('Enter your name: ')
    print(f'your name is: {name}')

# input_handler()

# take number input 

def number_input():
    age = None
        
    try:
        age = int(input('Enter your age: ')) # default type of input is string
    except:
        print('Please Enter Valid Age')
    else:
        print(f'Your age is : {age}')
    return age
    
    
# number_input()





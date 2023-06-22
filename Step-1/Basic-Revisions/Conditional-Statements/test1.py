
def input_hander(input_type=str):
    # input_type means which type of input we are looking for from user
    user_input = None


    
    if input_type == dict:
        input_type = str

    
    try:
        user_input = input_type(input('Enter here:  '))
        # temp_input  = user_inputs.split(' ')
        # user_input = [{i: temp_input[i]} for i in range(0,len(temp_input)) if temp_input[i] != '' ]
        # print(user_inputs)


    except OSError as e:
        print('Error while taking input from user as : ',e)

    else:
        return user_input


# Q4. Write a program to check whether a person is eligible for voting or not. (accept age from user)

def check_eligible_for_vote(age):
    is_eligible = False

    if(age>= 18):
        is_eligible = True

    return is_eligible        


# name = input_hander()
# print(name)

age = input_hander(input_type=int)

# result = check_eligible_for_vote(age=age)
# print(result)



# Q5. Write a program to check whether a number entered by user is even or odd.

def is_even(num):
    if(num%2 == 0):
        return True
    else:
        return False

print(f'{age} is even:  ', is_even(age))


# Q6. Write a program to check whether a number is divisible by 7 or not.

# Q7. Write a program to display "Hello" if a number entered by user is a multiple of five ,


def display_last_digit_of_num(num:int):

    # approach 1 using % modulus operator

    last_digit = num%10
    # Using string here
    last_digit2 = int(str(num)[-1])

    return last_digit, last_digit2
 
def is_divisible_of_n(num, divi):

    if divi not in [7, 3]:
        is_divisible = False

        if(num%divi == 0):
            is_divisible = True
        
        return is_divisible
    elif divi == 3:
        last_digit = display_last_digit_of_num(num)[0]

        if(last_digit%3 == 0):

            print(f'yes {last_digit} is divisible of 3 ')

    else:
        if(num % divi == 0):
            print('Hello')

print(is_divisible_of_n(age, 3))


                                      
# Q9. Write a program to display the last digit of a number.
# (hint : any number % 10 will return the last digit)


print(display_last_digit_of_num(12023-1))


# Q10. Write a program to check whether the last digit of a number( entered by user ) is divisible of 3 of not


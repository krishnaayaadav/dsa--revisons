

# variables are constainers which are use to store value to it so that we can use them further.

name = 'krishna'  # string
print(name) # output will be krishna

num = 123       # number 
print(num)  # 123

marks = 98.8   # marks
print(marks)  # 98.8

# 
is_passed  = True # booleans
print(is_passed)  # True

is_fail  = bool(0)
print(is_fail)


# let say we want to store  names of 5 students
# 1st Approach
stu1 = 'student1_name'
stu2 = 'student2_name'
stu3 = 'student3_name'
stu4 = 'student4_name'
stu5 = 'student5_name'

# Optimised Approach

# this  is tuple
stu_names = ('student1_name',
              'student2_name', 'studentn3ame', 'student4_name', 'student51_name', )

# tuples are use to store multiple items in single varible of any data-type
# Note: Tuples are immutable by nature so we can't change the values/items of the tuple after creations

# tuples are adviced to use in read operations only 



roll = 12
roll2 = 24
average = (roll + roll2)/2
print(average) # average meas sum of all elements divide by number of elements

name = 'krishna '
sir_name = 'yadav'

print(f'full name: {name} + {sir_name}: {name + sir_name} ') # two string concetenations

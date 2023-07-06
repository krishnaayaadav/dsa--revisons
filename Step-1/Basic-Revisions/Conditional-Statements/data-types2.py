"""
 Part 2 of data-types:
    Now we some special things in python such as list, tuple ,sets and dictionaries

    List: is use to store multiple items in single varible in ordered format.
         So list is  collection of elements which is store in some particular order maintian by indexing
         and list can store any kind of data items and value of list can update, deleted due muttable nature.
         To create list we square brackets stu_name = ['name1', 'name2', ]

    Tuples: are also use to store multiple items in a single variables of any data-type 
           But tuples are immuttable by nature means after inilization of the tuple we can't change the value of the tuple or their items
           because tuple does not support item updatation, deletion, addtion as well
           So we use tuple where we want to perform read operation than we use it, 
             tuples are faster than list in speed because they take less space or memory

            to create tuple we parentheses ()
            ids = (1,2,3,4,5,6,7)

   Dictionaries are use to store data in key-value pair So by using the key we can access their value update delete or perform any other operations that we want to perform.

   We use curly braces to create dictionaries.

   Sets: is also use to store collection of items in single variable in ordered way means
         means it does not have any particular order like indexing kind it store data in random order
         Note: set does not store duplicate values it sets muttable means we can change their elements after creation of sets.

         we curly braces to create sets 
         student_ids = {12,323,34,45,223,34,423,34,45}

  Arrays: are use to mutliple items in signle variable of same data-type only in order ways
          to use arrays in Python we array  or numpy module implement arrays in python


"""

# list
stu_name  = ['ankita', 'krishna', 'aman', 'karan', 'nisha'] # storing stu-names here
# store stu ids

stu_ids  = [12,34,5,4,34,45,56,34] #
expense_list = ['Tution fee', 400, 'collage fee', 1000, 'grocery',340]

# add new expense

expense_list.extend(['Asia Tour', 1000])
print(expense_list)

expense_list.append('Vocation Tour')
expense_list.remove('grocery')
expense_list.pop() # remove last elements default
expense_list.pop(2) # remove elm at index 2


# update
expense_list[3] = 'new Update expense data elements'
print(expense_list)


# Tuples here
ids = (12,45,32,34, 34,23)



occurrence = ids.count(34)
print(occurrence)
print(ids[::]) # print starting till end

for i in range(len(ids)):
   elm = ids[i]
   print(elm)



second_elm = ids[1]

print(second_elm) #

ids[1]


student_names = ('krishna', 'ankita', 'rohan')

temp_names = list(student_names)
temp_names[-1] = 'Rohan Roy'

print(tuple(temp_names), student_names)


# print using while loops 

l =  len(ids)-1

while l>=0:
   print(ids[l])
   l -=1 


# dictionaries 
student_details = {
   "name": "Ankita Singh",
   "email": 'ankita123@gmail.com',
   "age": 23,
   "address": "New Delhi, India",
   "name": 'Ankita' # updating value
}


# access value use key

print(student_details.keys())
print(student_details.values())

for key, val in student_details.items():
   print(key, val)

name = student_details['name']
print(name)
student_details['name'] = 'Ankita Sharma'


name = student_details['name']
print(name)

student_details.pop('name') # pop method will delete the specified key


# sets 

registeration_ids = {12,33,45,45,34,45,56,23,34,45,34,34}

print(registeration_ids)

registeration_ids.add(111)
registeration_ids.remove(34)
print(registeration_ids)


# Arrays

import array

# array creation
student_rolls = array.array('i', [12,23,45,45,56,56,3,12,34,45,54])

print(student_rolls)

# 

sum = 0
for elm in student_rolls:
   print(elm)
   sum += elm

print(sum)

def find_sum_of_arr(my_arr:array):
   sum  = 0
   for i in range(len(my_arr)):
      elm = my_arr[i]
      # sum += elm
      print(elm)
   
   return sum,array


print(find_sum_of_arr(student_rolls))

print(student_rolls[2])

print(len(student_rolls))

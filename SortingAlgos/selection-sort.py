
"""In selection sort we select the minimum number and than swap it"""

# first find minimium number
# swap that number with starting index with its actual position

# stuIds = (13, 45, 24, 23,1,43,34,45,45,34,2,23,34,56,57,52,  34, 20, 9)

stuIds = list(range(12, 34)) + list(range(1, 34))

# find minimium

class SelectionSort:

    def __init__(self, sequence):
        self.sequence = sequence

    def find_minimum(self):     
        sequence = list(self.sequence) # [ 13, 45, 24,9, 52, 20 ]

        st  = 0
        i   = st
        end = st
        small = sequence[st]
        # len here
        seq_len = len(sequence)

        # while loop
        const = seq_len - 1

        while i< seq_len:

            # current elm
            num = sequence[i]
            if(num < small):
                end = i
                sequence[st], sequence[end] = sequence[end], sequence[st] # swapping here
            i +=  1

            if not(i<seq_len): # 0 1 2 3 4 5:false 6:true
                st  = const - (const -(st+1))
                i   = 0
                end = st
                if st == 6:
                    break
                small = sequence[st]
        
        return f'\n {self.sequence} \n {tuple(sequence)} sorted one'

    def selection_sort(self):
        """Selection sort is implemented:
           find minimum element  and swap it.
        """
        # sequence here
        sequence = list(self.sequence)

        # length
        seq_len = len(sequence)

        for i in range(seq_len): # N times
            smallest = sequence[i] # i = 0 : 13 >> 9
            # print(smallest)

            for j in range(i+1, seq_len): # N-1
                nums = sequence[j]

                if nums < smallest: # checking weather nums is less than smallest or not
                    smallest = nums # j = 6: 13
                    sequence[i], sequence[j] = sequence[j], sequence[i]  # swapping the elements here
            
        return f'sorted \n {sequence } \n  \n unsorted hai\n {self.sequence} '

s = SelectionSort(sequence=stuIds)
# print(s.find_minimum())

print(s.selection_sort())

# if not 6<6:
#     print('is not less')

"""
   plans 8 days.
   3 days for  building portfolios crud react js, blog website, authentication. authentication, docker ngnix servers
   5 days for earning. 
"""
def swapping():
        

    # swapp the numbers
    num = 12
    num2 = 23
    print(num, num2)


    temp = num
    # num = 12 : num = 23 : num 23
    # num = 23
    # num2 = 23: num2 = temp
    # temp = 12 , num2 = 12
    # num = 23, num2 = 12
    num = num2
    num2 = temp

    print(num, num2)


    # 12 + 23 = 35
    # without using third variable

    marks1 = 10
    marks2 = 20
    print(marks2, marks1)


    marks1 = marks1 + marks2 # 10 + 20 = 30
    marks2 = marks1 - marks2 # 30 -20  = 10

    marks1 = marks1-marks2   # 30 - 10

    print(marks2, marks1)
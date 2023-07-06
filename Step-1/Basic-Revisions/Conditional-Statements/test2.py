"""
Q1. WAP to accept percentage from the user and display the grade according to the following criteria:

         Marks                                    Grade
         &gt; 90                                         A
         &gt; 80 and &lt;= 90                       B
         &gt;= 60 and &lt;= 80                       C
         below 60                                  D

"""

def display_percentage(percentage):  # 90

    if(percentage>90): # 
        print(f'Your Grade is: A')

    elif(percentage>80 and percentage<=90):
        print(f'Your Grade is: B')
    
    elif(percentage >= 60 and percentage<80):
        print(f'Your Grade is: C')

    else:
        print(f'Your Grade is: D')

# display_percentage(90)


"""
   

Q2. WAP to accept the cost price of a bike and display the road tax to be paid according to the following criteria :
&nbsp;&nbsp; &nbsp;
        Cost price (in Rs)                                       Tax
        &gt; 100000                                                  15 %
        &gt; 50000 and &lt;= 100000                          10%
        &lt;= 50000                                                  5%

"""

def display_road_tax(bike_price:int):
    tax = 0

    if(bike_price > 100000):
        tax = (bike_price*15) /100
    
    elif(bike_price <= 100000 and bike_price > 50000  ):
        tax = (bike_price *10 )/100

    elif(bike_price <= 50000):
        tax = (bike_price *5)/100
    
    print(f'Tax Price for bike of {bike_price} is: {tax}')

    return tax

# print(display_road_tax(50001))

"""
 

Q4. Write a program to accept a number from 1 to 7 and display the name of the day like 1 for Sunday , 2 for Monday and so on.

"""

def display_day(num): # num = 1
   # indexing 0
    days = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
    day_num = list(range(1,8)) # [1, 2, 3, 4, 5, 6, 7]

    if(num in day_num): # 1 in 
        print(f'\n Given number is: {num} and day is: {days[num-1]}')
    else:
        print('\n Given number is invalid')
    

# display_day(712)

"""
    
    Q5. WAP to accept a number from 1 to 12 and display name of the month and days in that month like 1 for January and number of days 31 and so on ?

"""
    
def display_month(num:int):

    month_num = list(range(1,13))

    months = ('January', 'Feb', 'March', 'April', 'May', 'June', 'July', 'August', 'September',  'October', 'Nov', 'Dec' )

    if(num in month_num):
        print(f'month at: {num} is: {months[num-1]}')
    else:
        print('\n Given number is invalid')

# display_month(100)

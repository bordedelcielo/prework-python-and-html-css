#Python prework homework

# Question 1
# Print username
# My solution:
def hello_name(user_name):
    print('hello_' + user_name + '!')

hello_name('USERNAME')

# Working through it in class 10/11
def hello_name(user_name):
    print('hello ' + user_name + '!')

hello_name('Christopher')

# Question 2
# Print odd numbers
# My solution:
odd_numbers = list(range(1,101,2))
print(odd_numbers)

#Working through it in class 10/11
# Print all odd numbers between 1 and 100
def add100():
    print([value for value in range(1,100,2)])

add100()
# Print first 100 odd numbers
def first_100():
    numbers = list(range(0,201,2))
    for number in numbers:
        if number % 2 != 0:
            print(number)

#first_100()

# Question 3
# My solution:
def max_num_in_list(a_list):
    print(max(a_list))

list_b = list_b = [25, 47, 35, 22]
max_num_in_list(list_b)

# Working through it in class 10/11
def max_num(a_list):
    max_value = max(a_list)
    return max_value

print(max_num([2,3,5,8,9]))
test = max_num([2,3,5,8,9])

#Question 4
#My solution:
"""Return true or false whether a given year is a leap year."""
def is_leap_year(a_year):
    if (a_year%4) == 0 and ((a_year%100) != 0 or (a_year%400) == 0):
        return True
    else: 
        return False

year_b = 1900
year_c = 1955
year_d = 1956
year_e = 2000
print(is_leap_year(year_b))
print(is_leap_year(year_c))
print(is_leap_year(year_d))
print(is_leap_year(year_e))

# Working through it in class
def is_leap_year(a_year):
    """
        Return true or false whether a given year is a leap year.
    """

    if a_year % 4 == 0 and (a_year % 400 == 0 or a_year % 100 != 0):
        print(True)
    else:
        print(False)

# Question 5
# I followed Kevin B.'s solution.
"""determine whether all numbers in the given list are consecutive."""

def is_consecutive(a_list): 
    end=len(a_list)
    if end < 2:
        print(False)
    
    for index in range(0, end -1):
        if a_list[index] + 1 == a_list[index + 1]:
            continue
        else:
            return False
    return True

list_b = [1,2,3,4,5,6,7,8,9]
list_c = [0,1,4,5,6,7,8,9]
list_d = [2]
is_consecutive(list_b)
is_consecutive(list_c)

print(is_consecutive(list_b))
print(is_consecutive(list_c))

# Working through it in class 10/11

def is_consecutive(a_list):
    """Figure out if all numbers in the given list are consecutive."""
    return sorted(a_list) == list(range(min(a_list),max(a_list)+1))

print(is_consecutive([1,2,3,4,5,7]))
print(is_consecutive([1,2,3,4,5,6]))

# Another in-class solution
def is_consecutive2(a_list):
    i = 0 # an increment counter
    status = True # a flag that tells us currently set to true
    while i < len(a_list) - 1:
        if a_list[i] + 1 == a_list[i+1]:
            i+=1 # increment i
        else:
            status = False
            break
    print(status)

is_consecutive2([3,4,5,6])
is_consecutive2([1,5,2,3,])
is_consecutive2([2,4,5])
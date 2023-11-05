"""
Please upload your answers to the 5 pre-work coding questions here.
upload them as a .py file, a .ipynb file, or as a repo containing a .py or a .ipynb 
The questions, if you need them:

Coding Questions

Complete the Coding Questions below in one .py file
Create an account at https://github.com/

Upload this file to github.com and submit the Git repository to the google classroom assignment.

Watch this video walkthrough(Git/Github/Google Clasrrom)

You will be turning in this assignment to your Google classroom. Please save your 5 functions to one .py file and demark the question numbers and the question in a comment above its respective function.

Question 1
Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.

    def hello_name(user_name):
        .....
               
Question 2
Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

    def first_odds():
        .....
               
Question 3
Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

    def max_num_in_list(a_list):
        .....
               
Question 4
Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

    def is_leap_year(a_year):
        .....
               
Question 5
Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

    def is_consecutive(a_list):
        .....
"""

def hello_name(username):
    print(username)
    pass

def print_odds():
    index = 1
    max = 100
    while index < 100:
        print(index)
        index += 2
    pass

def max_num_in_list(a_list):
    return len(a_list)

def is_leap_year(a_year):
    if a_year % 100 == 0 and a_year % 400 == 0:
        return True
    elif a_year % 100 == 0:
        return False
    elif a_year % 4 == 0:
        return True
    else:
        return False

def is_consecutive(a_list):
    is_consecutive = True
    for i in range(len(a_list)):
        if a_list[i] != a_list[-1]:
            if a_list[i] + 1 != a_list[i + 1]:
                is_consecutive = False
    return is_consecutive

print("hello_name")
hello_name("Junior")
print("")
print("print_odds")
print_odds() 
print("")
print("max_num_in_list")
b_list = (1,2,3,4,5)
print(max_num_in_list(b_list))
print("")
print("is_leap_year")
print(is_leap_year(1987))
print("")
print("is_consecutive")
b_list = (1,3,4,5)
print(is_consecutive(b_list))
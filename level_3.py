"""Write a Python function to find all the Strong numbers in a given list of numbers.
Write another function to find and return the factorial of a number. Use it to solve the problem."""

"""Example:
A number is considered to be a Strong number if sum of the factorial of its digits is equal to the number itself.
145 is a Strong number as 1! + 4! + 5! = 145.

Sample Input	                        Expected Output
num_list = [145,375,0,100,2]	        [145, 2]
"""

#PF-Exer-26

def factorial(number):
    #remove pass and write your logic to find and return the factorial of given number
    fact = 1
    if number == 0:
        return 1
    elif number>0:
        for i in range(number,0,-1):
            fact *= i
        return fact
        


def find_strong_numbers(num_list):
    #remove pass and write your logic to find and return the list of strong numbers from the given list
    
    strong_num_list = []
    for ele in num_list:
        if ele == 0:
            continue
        numm = 0
        temp = ele
        while ele != 0:
            las_num = ele%10
            numm += factorial(las_num)
            ele //=10
        if numm == temp:
            strong_num_list.append(temp)
        else:
            continue
    return strong_num_list
        
        
            
            
        


num_list=[145,375,100,2,0]
strong_num_list=find_strong_numbers(num_list)
print(strong_num_list)
# For this game we randomly generate a bunch of different math questions
# The user has to answer the correct value

import random # will allow us to randomly generate operants
import time #

OPERATORS = ["+", "-", "*"] # python operators
MIN_OPERAND = 2
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

def generate_propblem():
    left =  random.randint(MIN_OPERAND, MAX_OPERAND) # choose a random integer from MIN_OPERAND and MAX_OPERAND
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS) # this function choice picks an element from a list

    expr = str(left) + " " + operator + " " + str(right) # this will give us the expresion 
    answer = eval(expr) # the function eval evaluates a string as if it was a python expression
    return expr, answer

# 2) Now we ask the user a number (the answer) and setup the timer 

wrong = 0
input("Press enter to start!")
print("----------------------------------")

start_time = time.time() # this will give us a time in seconds 

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_propblem()
    while True: # loop so it keeps asking until the user gives the right answer 
        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()        
total_time = round(end_time - start_time, 2) # so we can have the total time from start to end (duh lol); round( ,2) limits for 2 digits

print("----------------------------------")
print("Nice work! :) You finished in:", total_time, "seconds! :D")

# FizzBuzz Algorithm 

# Define a function
# If input is divisble by 3, return string "Fizz"
# If input is divisible by 5, return string "Buzz"
# If input is divisible by both 3 and 5, return "FizzBuzz"
# If input is any other number, print out that number 

# Try 1:
def fizz_buzz(input):
    if input % 3 == 0 and not input % 5 == 0:
         return "Fizz"
    elif input % 5 == 0 and not input % 3 == 0:
        return "Buzz"
    elif input % 3 == 0 and input % 5 == 0:
        return "FizzBuzz"
    else:
        return input 
    
print(fizz_buzz(7))

# Cleaner Code:
def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):       #First condition for numbers like 15/ brackets 
        return "FizzBuzz"
    if input % 3 == 0:                      #elif not required if first condition false, second is true
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input                            #else not required, Python assumes 

print(fizz_buzz(7))


# Iterate over 1-10 and list out all the even numbers without using the step argument of the range function 
# Print out one message at the end for all the even numbers found

count = 0
for number in range(1, 10):
    if number % 2 == 0:
        print(number)
        count += 1
print(f"We have {count} even numbers")

         


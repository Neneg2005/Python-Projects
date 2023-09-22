print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? $"))
number_of_people = int(input("How many people is the bill split between? "))
percent_tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))


tip_percent = percent_tip / 100
total_tip = tip_percent * total_bill 
calculated_bill = total_tip + total_bill
each_person = calculated_bill / number_of_people
rounded_bill = "{:.2f}".format(each_person)
print(f"Each person should pay: ${rounded_bill}")

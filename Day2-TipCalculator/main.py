# print("Hello"[0]) #Get the first char in a string
# print("Hello"[-1]) #Get the last char in a string

# print(123_456_789) #Format long numbers

# print(3.1415) #Print decimal numbers (floats)

# print(True and False) #Print booleans

# print(type(False) == bool) #Get and compare types

# print(int("123")) #Cast string to integer int(), float(), string(), bool()

# print(6 / 3) #Division of 2 ints will return float
# print(6 // 3) #Double division operator will make division return int (this will wipe the decimal part of the number)

# print(2 ** 3) #Exponentiation

#Order of operations will follow PEMDAS
#() -> ** -> * -> / -> + -> - 
#BUT * and / are on the same priority level, will exec first one from left to right, same with + and -

# bmi = 84 / 1.65 ** 2 #Will output number with many decimals
# print(round(bmi, 2)) #Round decimals to N number of decimals

# score = 0 #Initialize score variable
# score += 2 #Increase score by 2
# score -= 1 #Reduce score by 1
# print("Your score is " + str(score)) #Print the score with str concatenation
# print(f"Your score is = {score}") #Print score with formatted strings, parsing is done behind the scene

print("Day 2: Tip calculator")
total_bill = float(input("What was the total bill?: $"))
tip_rate = int(input("How much tip would you like to give? 10, 12, or 15?: ")) / 100
number_of_people = int(input("How many people will split the bill?: "))
per_person_amount = total_bill * (1 + tip_rate) / number_of_people
print(f"Each person should pay: {round(per_person_amount, 2)}")

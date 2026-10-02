# 2.Number Analyzer
# Ask the user to enter an integer.
# Your program must determine:
# a.Whether the number is positive, negative, or zero.
# b.Whether it is even or odd.
# c.Whether it is divisible by 3.
# d.Whether it is divisible by 5.
# e.Whether it is divisible by both 3 and 5.
# Display the results clearly using f-strings.
# Hint: Use %, if-elif-else, and.

number = int(input("Enter an integer: "))

if number > 0:
	sign = "positive"
elif number < 0:
	sign = "negative"
else:
	sign = "zero"

if number % 2 == 0:
	parity = "even"
else:
	parity = "odd"

divisible_by_3 = number % 3 == 0
divisible_by_5 = number % 5 == 0
divisible_by_both = divisible_by_3 and divisible_by_5

print(f"{number} is {sign}.")
print(f"{number} is {parity}.")
print(f"Divisible by 3: {divisible_by_3}")
print(f"Divisible by 5: {divisible_by_5}")
print(f"Divisible by both 3 and 5: {divisible_by_both}")



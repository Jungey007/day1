# 3.Electricity Bill Calculator
# Create a program that asks the user for the number of electricity units consumed.
# Calculate the bill according to:
# Units	Rate
# First 20 units	Rs. 5/unit
# Next 30 units	Rs. 7/unit
# Next 50 units	Rs. 10/unit
# Above 100 units	Rs. 12/unit

# Use if-elif-else to calculate the bill.
# Also display:
# Units consumed
# Total bill
# using f-strings.

units = float(input("Enter the number of electricity units consumed: "))

if units < 0:
	print("Units consumed cannot be negative.")
elif units <= 20:
	bill = units * 5
elif units <= 50:
	bill = 20 * 5 + (units - 20) * 7
elif units <= 100:
	bill = 20 * 5 + 30 * 7 + (units - 50) * 10
else:
	bill = 20 * 5 + 30 * 7 + 50 * 10 + (units - 100) * 12

if units >= 0:
	print(f"Units consumed: {units:g}")
	print(f"Total bill: Rs. {bill:.2f}")


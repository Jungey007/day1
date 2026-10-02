# 4.ATM Withdrawal Validation
# Create a simple ATM withdrawal program.
# Ask the user for:
# Account balance
# Withdrawal amount
# PIN
# The transaction should be successful only when:
# PIN is correct
# Withdrawal amount is greater than 0
# Withdrawal amount is less than or equal to the balance
# Use and to combine the conditions.
# If the withdrawal is successful, calculate and display the remaining balance.
# Handle different cases such as:
# Invalid PIN
# Invalid withdrawal amount
# Insufficient balance
# Withdrawal successful

balance = float(input("Enter account balance: "))
withdrawal = float(input("Enter withdrawal amount: "))
pin = input("Enter PIN: ")
correct_pin = "1234"

if pin == correct_pin and withdrawal > 0 and withdrawal <= balance:
	balance -= withdrawal
	print(f"Withdrawal successful. Remaining balance: {balance:.2f}")
elif pin != correct_pin:
	print("Invalid PIN")
elif withdrawal <= 0:
	print("Invalid withdrawal amount")
else:
	print("Insufficient balance")


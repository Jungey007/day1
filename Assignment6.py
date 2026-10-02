# 6.Shopping Discount Calculator
# Create a shopping program that asks for:
# Customer name
# Product price
# Quantity
# Membership status (yes/no)
# Calculate:
# Subtotal = price × quantity
# Apply discounts:
# Subtotal ≥ Rs. 10,000 → 15%
# Subtotal ≥ Rs. 5,000 → 10%
# Subtotal ≥ Rs. 2,000 → 5%
# Otherwise → No discount
# If the customer is a member and subtotal is at least Rs. 5,000, give an additional 5% discount.
# Display:
# Customer name
# Subtotal
# Discount
# Final amount
# Use f-strings.

customer_name = input("Enter customer name: ")
price = float(input("Enter product price (Rs.): "))
quantity = int(input("Enter quantity: "))
membership = input("Are you a member? (yes/no): ").strip().lower()

subtotal = price * quantity

if subtotal >= 10000:
	discount_rate = 0.15
elif subtotal >= 5000:
	discount_rate = 0.10
elif subtotal >= 2000:
	discount_rate = 0.05
else:
	discount_rate = 0

if membership == "yes" and subtotal >= 5000:
	discount_rate += 0.05

discount = subtotal * discount_rate
final_amount = subtotal - discount

print(f"Customer name: {customer_name}")
print(f"Subtotal: Rs. {subtotal:.2f}")
print(f"Discount: Rs. {discount:.2f}")
print(f"Final amount: Rs. {final_amount:.2f}")


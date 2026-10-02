# 5.Login and Access Level
# Create a login system with the following users:
# Username: admin
# Password: admin123
# Role: Administrator
# Username: student12
# Password: study123
# Role: Student
# Ask the user for username and password.
# If the login is correct:
# Display the user's role.
# If the role is Administrator, display Full system access.
# If the role is Teacher, display Teacher access.
# If the login is incorrect, display Invalid username or password.
# Use nested conditions.

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":
	if password == "admin123":
		role = "Administrator"
		print("Role:", role)
		if role == "Administrator":
			print("Full system access")
		elif role == "Teacher":
			print("Teacher access")
	else:
		print("Invalid username or password")
elif username == "student12":
	if password == "study123":
		role = "Student"
		print("Role:", role)
		if role == "Administrator":
			print("Full system access")
		elif role == "Teacher":
			print("Teacher access")
	else:
		print("Invalid username or password")
else:
	print("Invalid username or password")


# Functional based programming

# Without functions
a = 10
b = 12

# math operations
print(a+b)
print(a-b)
print(a*b)
print(a/b)


a = 14
b = 15
# math operations
print(a+b)
print(a-b)
print(a*b)
print(a/b)

# With Functions

a = 300
b = 200
def math_ops():
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)

# Call the function
math_ops()

# Example 2
a = 689
b = 258
math_ops()


# Functions With Parameters --> a and b are parameters
def math_ops(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)

math_ops(600,800)
math_ops(20,10)


# Positional Functionality
def login(username,password):
    if username == "swapna" and password == "1234":
        print("Login successful!")
    else:
        print("Login failed.")



# call login
login("swapna","1234")
login("pavani","1234")
login("1235","4567")


# Default Arguement Based
def emp_info(emp_name="swapna",emp_email="swapna@gmail.com",emp_location="Hyderabad"):
    print(f"Hi {emp_name}, Your Email is {emp_email} and location is {emp_location}")
emp_info()
emp_info("user2","user2@gmail.com")
emp_info("Avaneesh","ava@gmail.com","Malaysia")







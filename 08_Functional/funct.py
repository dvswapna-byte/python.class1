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


# with keyword arguement

def emp_info(emp_name="swapna",emp_email="swapna@gmail.com",emp_location="Hyderabad",emp_country="India"):
    print(f"Hi {emp_name}, Your Email is {emp_email} and location is {emp_location} in {emp_country}")
emp_info(emp_name="swapna",emp_email="swapna@gmail.com",emp_location="Hyderabad",emp_country="India")

# Arbitary Positional (*arge)
def add_two_nums(a,b):
    print(a+b)

def add_unknown(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    print(f"Sum is: {sum}")

add_unknown()
add_unknown(1)
add_unknown(1,2,3)
add_unknown(10,20,56)

#Arbitary Keyword Arguement (**kwargs)
def profile(**info):
    print(info)

profile()
profile(name="swapna")
profile(name="swapna",id=236,city="Hyderabad")

# Transactions
def cred_transactions(**transactions):
    print(transactions)
    total = 0
    for i in transactions:
        total = total + transactions[i]
        print(f"You have done {len(transactions)} transactions and total valueof all transactions is {total}")

cred_transactions(jan=1000,feb=15000,mar=500)

# using arg and kwarg
def cred_transactions_new(*transactions,**account):
    print(transactions)
    print(account)
    total = 0
    for i in transactions:
        total = total + 1
    print(f"Hi {account['name']} You have done {total} amount of transactios in {account['account_id']}")
cred_transactions_new(1000,2000,3000,name="swapna",account_id=325892156)


        




    








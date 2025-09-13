# conditional statements (if, elif, else)
#if condition:
if 5 > 2:
    print("Valid condition")
else:
    print("Invalid condition")


 # Voting app
age = 12

if age >= 18:
    print("You Can Vote ")
else:
    print("You Cannot Vote") 

# input function
value = input("Enter some value: ")
print("You entered: ", value)
print(type(value))  # by default input function takes input as string 

# dynamic voting
age = int(input("Enter your age: "))  # converting string to integer
if age >= 18:
    print("You Can Vote ")
else:
    print("You Cannot Vote")

# Ternary operator
age = int(input("Enter your age: "))  # converting string to integer
status = "You Can Vote" if age >= 18 else "You Cannot Vote"
print(status)

#elif ladder
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 50:
    print("Grade D")
else:
    print("Fail")

# switch case - match case (python 3.10+)
day = int(input("Enter your choice (1-7): "))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day")

# elif ladder style
age = 25
if age == 0 or age == 1 or age == 2 or age == 3 or age == 4 or age == 5:
    category = "Toddler"
elif age == 6 or age == 7 or age == 8 or age == 9 or age == 10 or age == 11 or age == 12:
    category = "Kid"
elif age == 13 or age == 14 or age == 15 or age == 16 or age == 17 or age == 18 or age == 19:
    category = "Teen"
else:
    category = "Adult"
print("You are in the", category, "category")

# match case style
age = 25
match age:
    case 0 | 1 | 2 | 3 | 4 | 5:
        category = "Toddler"
    case 6 | 7 | 8 | 9 | 10 | 11 | 12:
        category = "Kid"
    case 13 | 14 | 15 | 16 | 17 | 18 | 19:
        category = "Teen"
    case _:
        category = "Adult"
print("You are in the", category, "category")


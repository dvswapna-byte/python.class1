# while loop
count = 1
while count <= 5:
    print(count)
    count += 1  # incrementing the counter to avoid infinite loop
print("Loop ended.")

# simulate real worls we use while loop
atm_correct_pin = 1234
user_given_pin = 0
while user_given_pin != atm_correct_pin:
    user_given_pin = int(input("Enter your ATM PIN: "))
print("PIN accepted. Access granted.")
print ("You can withdraw money now.")

#infinite loop
# while True:
count = 1
while True:
    print(count)
    count += 1
    if count > 5:
        break  # exit the loop when count exceeds 5

# for loop
text = "Python is a general purpose programming language"
for i in text:
    print(i)

#num = 10
#for charecter in num:
    #print(charecter)  # TypeError: 'int' object is not iterable

print(dir)
num = 10
print(dir(num))  # lists all the valid attributes and functionalities of int class
print(type(num))  # <class 'int'>

list_nums = [10, 20, 30, 40, 50]
print(type(list_nums))  # <class 'list'>
print(num)


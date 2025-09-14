# range
range(5)  # 0,1,2,3,4
range(1,6)  # 1,2,3,4,5
range(1,10,2)  # 1,3,5,7,9
range(10,1,-1)  # 10,9,8,7,6,5,4,3,2
range(10,1)  # empty
range(2,10,1)  # 2,3,4,5,6,7,8,9
range(2,10,3)  # 2,5,8

for num in range(1,6):
    print(num)

# to do the step reverse use -1
for num in range(10,1,-1):
    print(num)

for num in range (10,1,-2):
    print(num)

#loops with condition
print("Printing even numbers from 1 to 20")
num = 2
while num <= 20:
    print(num)
    num = num + 2

print("Printing even numbers from 1 to 20")
num = 1
while num <= 20:
    if num % 2 == 0:
        print(num)
    num = num + 1

#list of courses
course_list = ["python", "java", "c++", "html", "css", "javascript"]
for course in course_list:
    print(course)

# nested loops
for i in range(1, 4):  # outer loop
    for j in range(1,4):
        print(f"{i}*{j} = {i*j}")
    print("----------")

i = 1
while i < 4:
    j = 1
    while j < 4:
        print(f"{i}*{j} = {i*j}")
        j += 1
    print("----------")
    i += 1
# break and continue
for num in range(5):
    if num == 3:
        print(num)

for num in range(5):
    if num == 3:
        break
    print(num)
for num in range(5):
    if num == 3:
        continue
    print(num)


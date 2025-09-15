# List in python

# Empty list
my_list = []
print("Empty list:", my_list)
print("Type of my_list:", type(my_list))
print(my_list)

# Store data in list
my_list = [1, 2, 3, 4, 5]
print("List with data:", my_list)

string_list = ["Python", "Djaonjo", "JavaScript"]
print("List of strings:", string_list)

mixed_list = [1, "Hello", 3.4, True]
print("Mixed list:", mixed_list)

num_list = list[10, 20, 30, 40, 50]
print("List using list() constructor:", num_list)
print("Type of num_list:", type(num_list))
print(num_list)

# Accessing elements in list
print("First element of my_list:", my_list[0])
print("Last element of my_list:", my_list[-1])
print("Second last element of my_list:", my_list[-2])
print("Elements from index 1 to 3:", my_list[1:4])
print("Elements from start to index 3:", my_list[:4])

# Slicing
num_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(num_list[:]) # All elements
print(num_list[1:]) # From index 1 to end
print(num_list[:3]) # From start to index 2
print(num_list[1:4]) # From index 1 to index 3
print(num_list[::2]) # Every second element
print(num_list[1::2]) # Every second element from index 1
print(num_list[::-1]) # Reversed list
print(num_list[::-2]) # Every second element in reversed list

# Memory allocation
num1 = 10
num2 = 10
print("Memory address of num1:", id(num1))
print("Memory address of num2:", id(num2))
# Both point to same memory location as integers are immutable
my_list1 = [1, 2, 3]
my_list2 = [1, 2, 3]
print("Memory address of my_list1:", id(my_list1))
print("Memory address of my_list2:", id(my_list2))
# Both point to different memory locations as lists are mutable
print(id(my_list1[0]))
print(id(my_list2[0]))
# Both point to same memory location as integers are immutable

# Accessing errors
# print(my_list[10]) # IndexError: list index out of range
# print(my_list[-10]) # IndexError: list index out of range
# print(my_list[1:10]) # No error, returns elements from index 1 to end

# Using range() to create a list
range_list = list(range(1, 11))
print("List created using range():", range_list)

# Perform conditional logics
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day = input("Enter a day: ")
if day in days:
    print("Exists")
else:
    print("Does not exist")

# List methods
list = [10]
print(dir(list))

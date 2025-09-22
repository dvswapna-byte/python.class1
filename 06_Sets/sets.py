# sets
empty_set = {}
print(type(empty_set))
print(empty_set)

# empty set should be created using class
empty_set = set()
print(type(empty_set))
print(empty_set)

# numbers sets
num_set = {10,20,30,40,50}
print(type(num_set)) # unordered
print(num_set)


# Duplicates eliminated
num_set = {10,20,30,40,50,10,20}
print(type(num_set))
print(num_set) #unique

# No index
num_set = {10,20,30,40,50}
#print(num_set[0])

# String and mixed
text_set = {"ab","good","morning"}
print(text_set)

mixed_set = {10,20,30,40,50,"ab","good","morning"}
print(mixed_set)

# Accessing
num_set = {10,20,30,40,50}
for num in num_set:
    print(num)

# convert to access using index
list_nums = list(num_set)
print(list_nums[0])





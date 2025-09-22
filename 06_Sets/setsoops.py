# Set operations
# add : adds an element to the set

s1 = {10,20,30,40,50}
print(s1)
s1.add(60)
print(s1)

# update: Adds multiple elements
s1 = {10,20,30,40,50}
print(s1)
s1.update([60,70,80,90])
print(s1)

# remove: removes element
s1 = {10,20,30,40,50}
print(s1)
s1.remove(30)
print(s1)


# Discard: remove element, if not found no error
s1 = {10,20,30,40,50}
print(s1)
s1.discard(30)
print(s1)
s1.discard(92)
print(s1)

# clear(): removes all the elements, empties set
s1 = {10,20,30,40,50}
print(s1)
s1.clear()
print(s1)

#pop : removes an random element
s1 = {10,20,30,40,50}
print(s1)
s1.pop()
print(s1)
print("======)")

#NOTE: SETS ARE MUTABLE

# Copy: creates a backup/shallow copy
s1 = {10,20,30,40,50}
print(s1)
s1.copy()
print(s1)

# set specific operations
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
# Union: combines the elements from both sets
print(s1.union(s2))

print(s1 | s2)

# intersection: extracts common elements
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.intersection(s2))
print(s1 & s2)


# intersection_update: extract only common elements and updates
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.intersection_update(s2))
print(s1)
print(s2)
print(s1.intersection_update(s2))

# Difference : removes the elements which also occur in other set
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.difference(s2))

# Difference_update
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.difference_update(s2))
print("======")
print(s1 - s2)
print(s2 - s1)

# Symetric difference
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}

print("=====")
print(s1^s2)

print(s1.symmetric_difference(s2))
print(s1.symmetric_difference_update(s2))
print(s2^s1)

# issubset(): subset of other set
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
s3 = {50,40,10}
print(s2.issubset(s1))
print(s3.issubset(s1))

# issuperset
s1 = {10,20,30,40,50}
s2 = {40,50}
s3 = {50,40,10}
print(s2.issuperset(s1))
print(s3.issuperset(s1))
print(s1.issuperset(s2))

# isdisjointset: checks if 2 sets have no common elements
s1 = {10,20,30,40,50}
s2 = {40,50}
s3 = {50,40,10}
print(s1.isdisjoint(s2))

# All 17 operations performed
#frozenset is immutable
fz_set = frozenset({10,20,30,40,50})
print(type(fz_set))
print(dir(fz_set))











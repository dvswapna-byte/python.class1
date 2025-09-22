# dictionaries
# empty dict
empty_dict = {}
print(type(empty_dict))
print(empty_dict)

#dict_nums
dict_nums = {1:10,2:20,3:30}
print(dict_nums)

fruits_dict = {"a":"apple","b":"banana"}
print(fruits_dict)

fruits_dict.update({"c":"cherry"})
print(fruits_dict)

fruits_dict.update({"a":"avacado"})
print(fruits_dict)


#pop(): removes item with specified key
# pop item():n removes last item

fruits_dict = {"a":"apple","b":"banana"}
print(fruits_dict)
fruits_dict.popitem()
print(fruits_dict)

# clear: removes all items
#empties the dictionary
fruits_dict = {"a":"apple","b":"banana"}
print(fruits_dict)
fruits_dict.clear()
print(fruits_dict)

#get(): used to get the values for key
fruits_dict = {"a":"apple","b":"banana"}
print(fruits_dict)
print(fruits_dict.get("b"))
print(fruits_dict)
print(fruits_dict.get("c"))


#keys: returns all the keys
fruits_dict = {"a":"apple","b":"banana"}
print(fruits_dict)
print(fruits_dict.keys())

only_keys = fruits_dict.keys()
for key in only_keys:
    print(key)

for key in fruits_dict:
    print(key)

#values: returns all values
fruits_dict = {"a":"apple","b":"banana"}
print(fruits_dict)
print(fruits_dict.values())

only_values = fruits_dict.values()
for value in only_values:
    print(value)

# items(): returns keys and values both
fruits_dict = {"a":"apple","b":"banana"}
print(fruits_dict)
print(fruits_dict.items())
keys_values = fruits_dict.items()
for item in keys_values:
    print(item)

# copy: create shallow copy
fruits_dict = {"a":"apple","b":"banana"}
print(fruits_dict)
bk_fruits_dict = fruits_dict.copy()
print(bk_fruits_dict)

bk_fruits_dict.update({"c":"cherry"})
print(bk_fruits_dict)

# soft copy using = 
fruits_dict = {"a":"apple","b":"banana"}
print(fruits_dict)
bk_fruits_dict = fruits_dict
print(bk_fruits_dict)
bk_fruits_dict.update({"c":"cherry"})
print(bk_fruits_dict)
print(fruits_dict)


# setdefault: returns value of a key if not present sets it
# if the key is present will not update
fruits_dict = {"a":"apple","b":"banana"}
print(fruits_dict)
print(fruits_dict.setdefault("b","blackberry"))
print(fruits_dict)


fruits_dict = {"a":"apple","b":"banana"}
print(fruits_dict)
print(fruits_dict.setdefault("c","cherries"))
print(fruits_dict)

















# strings
# string is a sequence of characters
a = "hello"
b = 'world'
c = '''hello world'''
d = """hello world"""
print(a)
print(b)
print(c)
print(d)
print(type(a))
print(type(b))
print(type(c))
print(type(d))

#note: triple quotes are used for multi-line strings and docstrings
#multi-line string
e = '''this is a very 
multi-line string'''
print(e)

#if you want to use single quote in a string, use double quotes to enclose the string
f = "it's a beautiful day"
print(f)
#if you want to use double quote in a string, use single quotes to enclose the string
g = 'he said "hello" to me'
print(g)

# if you want to use both single and double quotes in a string, use escape character (\)
h = 'it\'s a beautiful day'
i = "he said \"hello\" to me"
print(h)
print(i)

#string concatenation
j = a + " " + b
print(j)

#indexing in strings
#positive indexing
text = "hello world"
print(text[0]) #h
print(text[1]) #e
print(text[2]) #l
#negative indexing
print(text[-1]) #d
print(text[-2]) #l
print(text[-3]) #r

#string accessing
text = "hello world"
print("using loop")
for charecter in text:
    print(charecter)
print("using indexing")
for i in range(len(text)):
    print(text[i])

text = "Python"
print(len(text)) #6
print("Length of the string is:", len(text))

#example using list
list_data = ["dell", "hp", "lenovo", "asus"]
print("Length of the list is:", len(list_data)) #4
print("Brands count is:", len(list_data))

#string slicing
#string[]
#string[Start:End:Step]
text = "hello world"
print(text[0:5]) #hello
print(text[6:11]) #world
print(text[:5]) #hello
print(text[6:]) #world
print(text[:]) #hello world
print(text[::2]) #hlowrd
print(text[1:10:2]) #el ol
print(text[::-1]) #dlrow olleh
print(text[-1:-6:-1]) #dlrow

#string methods
text = "hello world"
print(text.upper()) #HELLO WORLD
print(text.lower()) #hello world
print(text.capitalize()) #Hello world
print(text.title()) #Hello World
print(text.count('o')) #2
print(text.find('o')) #4 (index of first occurrence)
print(text.find('z')) #-1 (not found)
print(text.replace('world', 'Python')) #hello Python
print(text.split(' ')) #['hello', 'world']
print(text.strip()) #hello world (removes leading and trailing spaces)
print(text.startswith('h')) #True
print(text.endswith('d')) #True
print(text.isalpha()) #False (contains space)
print(text.isdigit()) #False
print(text.isspace()) #False
print(text.index('o')) #4 (index of first occurrence, raises error if not found)



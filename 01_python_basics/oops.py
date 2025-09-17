# Append()
# adds a elemnt to the end of the list
#extend
#takes an iterable and adds each element to the list individually

# reverse
#reverses thebelements in the list
# Sort: sort the elements of the list
# reverse using slice technique
# sort the elements in ascending or descending order, implace operation
list_nums = [20, 10, 30, 50, 40]
print(list_nums)
print(list_nums.sort(reverse=True))
print(list_nums)

# sort with text
list_courses = ["c", "Python","Java","Cloud"]
print(list_courses)
print(list_courses.sort())
print(list_courses)

#mixed data
#list_mix = [20, 10. "C","Python",30, 50, 40]
#print(list_mix)
#print(list_mix.sort())
#print(list_mix)

#copy: creates a shallow copt
#soft copy

#infinate loops
#i=10
#while i>=1:
 #   print(i)
  #  i+=1

#loop, else
a=int(input("Enter the lower limit: ")) 
b=int(input("enter a upper limit: "))
even=0
odd=0
for i in range (a,b+1):
    if i/2==0:
        even+=i
    else:
        odd+=i
else:
    print("Loop terminated succssfully: ")
    print("the sum of all the even numbers in the given series is", even)
    print("the sum of all the odd numbers in the given series is ", odd)


    

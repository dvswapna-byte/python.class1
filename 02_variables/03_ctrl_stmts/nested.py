# nested conditional statements
age = int(input("Enter your age: "))
has_id = input("Do you have an ID? (yes/no): ").strip().lower()
if age >= 18:
    if has_id == 'yes':
        print("You are allowed to enter the club.")
    else:
        print("You need an ID to enter the club.")
else:
    print("You are not allowed to enter the club.")
    
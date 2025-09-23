# Student/Product/Employee Management System
# System setup Using Tuples
SYSTEM_INFO = ("Edify Student Management Portal","v1","2025")

ADMIN_INFO =("admin@edify.com","9808080","Room 201")

# Display System info at startup
print("="*50)
print(f"    Welcome To {SYSTEM_INFO}")
print("-"*50)
print(f"    Developed by Students at {SYSTEM_INFO}")
print("="*50)

# Student info is Dictionary
students = {}


# Build menu system
while True:
    print("Choose an Option Below:  ")
    print("1 - Add Student")
    print("2 - Modify Student")
    print("3 - Delete Student")
    print("4 - List Student")
    print("5 - Exit System")

    choice = input("Enter Your Choice(1-5): ")

    if choice == "1":
        print("Adding Student Logic")
        student_id = input("Enter ID:   ")
        if student_id in students:
            print("ID Already Exists")
        else:
            name = input("Enter Name:   ").title()
            scores = []
            while True:
                score_input = input("Enter Score or Type Done:  ")
                if score_input == "done":
                    break
                if score_input.isdigit():
                    score = int(score_input)
                    if 0<= score <=100:
                        scores.append(score)
                    else:
                        print("Scores should be in range (0-100)")
                else:
                    print("Scores can be Numbers only")
            skills = set()
            while True:
                skill_input = input("Enter Skill or Type Done:  ")
                if skill_input == "done":
                    break
                skills.add(skill_input.title())
            
            # save student details
            students[student_id] = {
                "name": name,
                "scores": scores,
                "skills": skills
            }
            print("Student Added")

        # for confirmation
        print(students)



    
    elif choice =="2":
        print("Modifying Student Logic")
        student_id = input("Enter ID:   ")
        if student_id in students:
            new_name = input("Enter Name:   ").title()
            students[student_id]["name"] = new_name
            print("Student updated successfully")
        else:
            print("ID Doesn't exist")
            print(students)


    elif choice == "3":
        print("Deleting Student Logic")
        student_id = input("Enter ID to delete:   ")
        if student_id in students:
            remove = students.pop(student_id)
            print(remove)
        else:
            print("ID doesn't exist")


    elif choice == "4":
        print("Listing Student Logic")
        if not students:
            print("No Students Available")
        else:
            print("Students Details")
            for sid, data in students.items():
                print(f"ID: {sid}")
                print(f"  Name: {data['name']}")
                print(f"  Scores: {data['scores']}")
                print(f"  Skills: {', '.join(data['skills']) if data['skills'] else 'None'}")
                print("-" * 50)

        # calculating Average score, high score, count of skills
        
        count = len(skills)
        print(f"Total number of skills:", count)

        all_scores = [score for data in students.values() for score in data['scores']]
        if all_scores:
            high_score = max(all_scores)
            print(f"Highest Score:", high_score)
        else:
            print("No scores available to calculate highest score.")

        average = sum(scores)/len(scores)
        print("Average of Scores is:", average)
        

    elif choice == "5":
        print("Exiting System")
    else:
        print("Invalid Option, Select only (1-5)")






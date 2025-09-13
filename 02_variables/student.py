# Student Management System
student_id = 101
student_name = "Alice"
student_age = 20

# Scores
quiz_score = 85
assignment_score = 90
exam_score = 88

# Attendance
student_attendance = 60

# Calculations
total_score = quiz_score + assignment_score + exam_score
average_score = total_score / 3
student_passed = average_score >= 75
attendance_percentage = (student_attendance / 75) * 100

#Attendance increment
student_attendance += 1

# Award eligibility
award_eligible = average_score >= 90 and attendance_percentage >= 90
# Print student details
print("="*50)
print("======== Student Details ========")
print("="*50)
print(f"ID: {student_id}")
print(f"Name: {student_name}")
print(f"Age: {student_age}")
print(f"Quiz Score: {quiz_score}")
print(f"Assignment Score: {assignment_score}")
print(f"Exam Score: {exam_score}")
print(f"Total Score: {total_score}")
print(f"Average Score: {average_score:.2f}")
print(f"Passed: {'Yes' if student_passed else 'No'}")
print(f"Student Current Attendance: {student_attendance}")
print(f"Attendance Percentage: {attendance_percentage:.2f}%")
print(f"Award Eligible: {'Yes' if award_eligible else 'No'}")
print("="*50)

# Increment attendance by 1
student_attendance += 1
attendance_percentage = (student_attendance / 75) * 100
print(f"Updated Attendance: {student_attendance}")
print(f"Updated Attendance Percentage: {attendance_percentage:.2f}%")

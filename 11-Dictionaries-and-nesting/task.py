student_scores = {"Harry": 88, "Ron": 78, "Hermione": 95, "Draco": 75, "Neville": 60}

# Grading Program
# You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names of the students and the values are their exam scores.

# Write a program that converts their scores to grades.

# By the end of your program, you should have a new dictionary called student_grades that should contain student names as keys and their assessed grades for values.

# This is the scoring criteria:
# - Scores 91 - 100: Grade = "Outstanding"
# - Scores 81 - 90: Grade = "Exceeds Expectations"
# - Scores 71 - 80: Grade = "Acceptable"
# - Scores 70 or lower: Grade = "Fail"

student_grades = {}

for score_key in student_scores:
    if student_scores[score_key] >= 91:
        student_grades[score_key] = "Outstanding"
    elif student_scores[score_key] >= 81 and student_scores[score_key] <= 90:
        student_grades[score_key] = "Exceeds Expectations"
    elif student_scores[score_key] >= 71 and student_scores[score_key] <= 80:
        student_grades[score_key] = "Acceptable"
    else:
        student_grades[score_key] = "Fail"

print(student_grades)

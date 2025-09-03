"""
- Create a variable grade holding an integer between 0 - 100
- Code if, elif, else statements to print the letter grade of the number grade variable

Grades:
A = 90 - 100
B = 80 - 89
C = 70-79
D = 60 - 69
F = 0 - 59

Example:
if grade = 87 then print('B')
"""
grade = int(input("Enter your grade : "))
if 90 < grade < 100:
    print("Grade is A")
elif 80 < grade < 90:
    print("Grade is B")
elif 70 < grade < 80:
    print("Grade is C")
elif 60 < grade < 70:
    print("Grade is D")
else:
    print("Grade is F")
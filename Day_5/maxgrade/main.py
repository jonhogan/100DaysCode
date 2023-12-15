grades = [78, 65, 89, 86, 55, 91, 64, 89]

maxGrade = float('-inf')

for grade in grades:
    if grade > maxGrade:
        maxGrade = grade

print(f'The highest grade is: {maxGrade}')
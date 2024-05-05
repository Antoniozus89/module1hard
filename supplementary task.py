grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]

students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

surnames = sorted(students)

grade_list1 = []

for i in grades:
    aver = round(sum(i) / len(grades),2)
    grade_list1.append(aver)
print(grade_list1)

dict(zip(surnames, grade_list1))
print(dict(zip(surnames, grade_list1)))

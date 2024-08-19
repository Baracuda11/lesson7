grades = [5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2, ], [4, 4, 3], [5, 5, 5, 4, 5]
student = ("Aaron", "Bilbo", "Steve", "Johnne", "Khendrik")
student = sorted(student)
keys = (sum(grades[0]) / len(grades[0]),
        sum(grades[1]) / len(grades[1]),
        sum(grades[2]) / len(grades[2]),
        sum(grades[3]) / len(grades[3]),
        sum(grades[4]) / len(grades[4]))
klass = {student[0]: keys[0], student[1]: keys[1], student[2]: keys[2], student[3]: keys[3], student[4]: keys[4]}
print(klass)
a = input("Выберите последнего ученика из списка:")

print(a, keys[0] and keys[1] and keys[2] and keys[3] and keys[4])
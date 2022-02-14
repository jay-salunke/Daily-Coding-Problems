count = 0
list = []
n = int(input())
k = int(input())

while n > 0:
    a = int(input())
    list.append(a)
    n -= 1

for student_marks in list:
    if student_marks > 0 and student_marks >= list[k-1]:
        count += 1

print(count)

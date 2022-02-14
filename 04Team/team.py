list = []
count = 0
problems = int(input())
while problems > 0:
    x, y, z = (input().split())
    list.append([int(x), int(y), int(z)])
    if list[0].count(1) >= 2:
        count += 1
    list.clear()
    problems -= 1

print(count)

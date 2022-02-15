n = int(input())
x = 0
statements = []
while n > 0:
    statement = input()
    statement = statement.replace("X", "")
    statements.append(statement)
    n -= 1

for s in statements:
    if s == "++":
        x += 1
    else:
        x -= 1

print(x)

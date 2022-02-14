words = []
test_cases = int(input())

while test_cases > 0:
    word = input()
    words.append(word)
    test_cases -= 1

for word in words:
    if len(word) > 10:
        length = len(word[1:len(word)-1])
        print(word[0]+str(length)+word[-1])
    else:
        print(word)

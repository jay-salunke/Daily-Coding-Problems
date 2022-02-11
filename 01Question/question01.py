'''
Run-length encoding is a fast and simple method of encoding strings.
The basic idea is to represent repeated successive characters as a single count and character.
For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding.
You can assume the string to be encoded have no digits and consists solely of alphabetic characters.
 You can assume the string to be decoded is valid.

'''


def check_pos(position):
    return True if position == len(string)-1 else False


string = "AAAABBBCCDAA"
encoded_string = ""
position = 1
count = 1
list = []
current_letter = string[0]
while True:
    if current_letter == string[position]:
        count += 1
        if check_pos(position):
            list.append(str(count)+current_letter)
            break
        position += 1
    else:
        list.append(str(count)+current_letter)
        current_letter = string[position]
        if check_pos(position):
            list.append(str(count)+current_letter)
            break
        count = 1
        position += 1
encoded_string = encoded_string.join(list)
print(encoded_string)

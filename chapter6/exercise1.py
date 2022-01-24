index = 0
string = input("Type a string: ")
while index < len(string):
    letter = string[index-1]
    print(letter)
    index = index - 1

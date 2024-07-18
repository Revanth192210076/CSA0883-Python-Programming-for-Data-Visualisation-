def character(s, char):
    for i in range(len(s)):
        if s[i] == char:
            return i
    return -1  

input= "Hello, World!"
char = 'o'

index = character(input,char)

if index != -1:
    print(f"The character '{char}' is present at index {index}.")
else:
    print(f"The character '{char}' is not present in the string.")

string_1 = input() 
length = len(string_1) 
distance = 0 
for index in range (0, length): 
    if index == 0: 
        a = abs(ord(string_1[index]) - ord('a')) 
        b = 26 - abs(ord(string_1[index ]) - ord('a')) 
    else: 
        a = abs(ord(string_1[index]) - ord(string_1[index - 1])) 
        b = 26 - abs(ord(string_1[index ]) - ord(string_1[index -1])) 
    distance += min (a, b) 
print(distance) 

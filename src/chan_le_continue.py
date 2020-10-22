"""
@created: Nguyen Anh Tien
@Desc: odd, even, continue
    print: tat cac so le tu 1 toi number
"""

number = int(input("Enter: "))

for index in range(number):
    if index % 2 != 0:
        print(index, end=" ")

print()

for index in range(number):
    if index % 2 == 0:
        continue
    print(index, end=" ")
    

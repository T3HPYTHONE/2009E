"""
@created: Nguyen Anh Tien
@Desc: prime number: n1, n2
"""

number = int(input("Enter a number: "))
flag = True

"""
number = 2
"""
#tim n1
for index in range(number - 1, 1, -1):
    for factor in range(2, index):
        if index % factor == 0:
            flag = False
            break
    if flag == True:
        print("n1: ", index)
        break
    flag = True

#tim n2
flag = True
counter = number + 1
while True:
    for factor in range(2, counter):
        if counter % factor == 0:
            flag = False
    if flag == True:
        print("n2: ", counter)
        break
    flag = True
    counter += 1

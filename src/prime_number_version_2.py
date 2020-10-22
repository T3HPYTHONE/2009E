"""
@created: Nguyen Anh Tien
@Desc: prime number
"""

number = int(input("Enter a number: "))
flag = True

for index in range(2, number):
    if number % index == 0:
        flag = False

if flag == True:
    print(f"{number} la so nguyen to")
else:
    print(f"{number} khong phai la so nguyen to")

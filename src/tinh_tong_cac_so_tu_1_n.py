"""
@created: Nguyen Anh Tien
@Desc: tinh tong cac so tu 1 toi n
"""

number = int(input("Enter a number: "))

total = 0
for index in range(1, number + 1):
    total += index

print(f"Total: {total}")

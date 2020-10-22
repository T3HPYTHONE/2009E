# -*- coding: utf-8 -*-

"""
Step 1:
    xac dinh cac so la so le
Step 2:
    tim cac so lon nhat
"""

a = int(input("Nhập a =:"))
b = int(input("Nhập b =:"))
c = int(input("Nhập c =:"))

if a % 2 == 0:
    a  = 0
    
if b % 2 == 0:
    b = 0
    
if c % 2 == 0:
    c = 0

if a != 0 or b != 0 or c != 0:
    if (a == 0) and (b != 0 and c != 0):
        max_number = max(b, c)
    elif (a != 0) and (b == 0) and (c != 0):
        max_number = max(a, c)
    elif (a != 0) and (b != 0) and (c == 0):
        max_number = max(a, b)
    elif (a != 0) and (b != 0) and (c != 0):
        max_number = max(a, b, c)
    elif (a != 0) and (b == 0) and (c == 0):
        max_number = a
    elif (a == 0) and (b == 0) and (c != 0):
        max_number = c
    elif (b != 0) and (c == 0) and (a == 0):
        max_number = b
    print("So le lon nhat la:", max_number)
else:
    print("Khong co so le nao")

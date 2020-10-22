import math

def is_prime(a_number):
    for index in range(2, int(math.sqrt(a_number)) + 1):
        if a_number % index == 0:
            return False
    return True

if __name__ == '__main__':
    n = int(input("Enter: "))
    total = 0
    for a_number in range(2, n + 1):
        if is_prime(a_number):
            print(a_number, end=" ")
            total += a_number
    print()
    print("Result: ", total)
    

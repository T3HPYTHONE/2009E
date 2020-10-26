#
import string

if __name__ == '__main__':
    input_str = input()
    embosser = string.ascii_lowercase
    pointer = 0
    total = 0
    for index in range(len(input_str)):
        position = embosser.index(input_str[index])
        rotate = abs(position - pointer)
        if rotate > 13:
            #clockwise not shortest
            #should counterclockwise
            rotate = 25 - rotate + 1
        pointer = position
        total += rotate
    print(total)

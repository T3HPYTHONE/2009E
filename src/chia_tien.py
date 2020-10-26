"""
"""

if __name__ == '__main__':
    input_money = 45005
    counter = 0
    while input_money > 0:
        mod = input_money % 10
        input_money = input_money // 10
        if mod != 0:
            if counter == 0:
                print("{} VND".format(mod))
            elif counter == 1:
                print("{} muoi VND".format(mod))
            elif counter == 2:
                print("{} tram VND".format(mod))
            elif counter == 3:
                print("{} nghin VND".format(mod))
            elif counter == 4:
                print("{} chuc nghin VND".format(mod))
            elif counter == 5:
                print("{} tram nghin VND".format(mod))
            elif counter == 6:
                print("{} trieu VND".format(mod))
        counter += 1

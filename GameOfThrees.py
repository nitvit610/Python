num = int(input("Please input a number: ") )

while True:
    if num % 3 == 0:     
        if num == 0:
            break
        else:
            print(int(num), "/ 3 =", int(num / 3) )
            num /= 3

    elif num % 3 == 1:
        print(int(num), "- 1 =", int(num) - 1)
        num -= 1
        

    else:
        print(int(num), "+ 1 =", int(num) + 1)
        num += 1

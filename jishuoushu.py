number = input("请你输入一个数，判断这个数的奇偶性: ")
number = int(number)
if number % 2 == 0:
    print("\n这个数" + str(number) + " 是偶数.")
else:
    print("\n这个数 " + str(number) + " 是奇数.")

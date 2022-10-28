import random
PC = random.randint(1, 100)  # PC可以修改为任意名字
while True:
    ME = int(input("请输入100以内的整数"))  # ME可以修改为任意名字
    if ME > PC:
        print("大了")
    elif ME < PC:
        print("小了")
    else:
        print("答对了")
        break

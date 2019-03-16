#导入random随机包
import random

if __name__ == '__main__':

    #randint 随机获取一个数
    val = random.randint(1,2);

    print(val)

    #randchoice 在一个指定的数据源中随机获取一个数
    num = "abcde"
    val = random.choice(num)
    print(val)

    #randrende  三个参数 第一个参数是起始值，第二个参数是结束值 ， 第三个参数是步长 （可写可不写）
    v = random.randrange(1,10,2)
    print(v)

    #shuffle 把列表中的值打乱
    num = [1,2,3,4,5,6]

    print("before {0}".format(num))

    v = random.shuffle(num)

    print("after {0}".format(num))

    #uniform函数 在写范围中 取小数
    v = random.uniform(3,4)
    print(v)


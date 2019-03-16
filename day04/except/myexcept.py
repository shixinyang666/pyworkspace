if __name__ == '__main__':
    class MyException(Exception) :
        def myfun(self):
            print("自定义异常")
    #ZeroDivisionError异常 是当被除数不正确是 抓取异常使程序继续运行
    try:
        print(5/0)
    except ZeroDivisionError :
        print("ZeroDivisionError")

    #Exception全部异常
    try:
        print(5/0)
    except Exception :
        print("Exception")

    #手动抛出异常     当处理异常时将不影响程序运行
    try:
        raise Exception
    except Exception:
        print("Exception")

    print("good")

    #当处理异常有多个时，应把子异常类放在上面 否则将执行不到
    try:
        print(5/0)
    except ZeroDivisionError :
        print("ZeroDivisionError")
    except Exception :
        print("Exception")

    #自定义异常
    try:
        raise ZeroDivisionError
    except MyException as m:
        #调用自定义异常类中的函数
        m.myfun()
    except Exception :
        print("Exception")
if __name__ == '__main__':
    # ##
    # 字符串切片
    # 普通字符串切片 语法:mstr[0:3] 数字可以省略 冒号不可省略
    # mstr[::2]字符串切片
    # ///

    mstr = "goog goog study,day day up"

    #简单打印字符串
    print(mstr)

    #字符串切片
    print(mstr[0:3])

    #字符串切片
    print(mstr[:])

    ###
    # 字符串大小写转换及首字母大写
    # 字符串全部变成大写 upper()
    # 字符串全部变成小写 lower()
    # 字符串首字母大写() title()
    # ///
    nstr = " Hello Python "
    bstr = " abcdef ";
    #字符串全部大写
    print(nstr.upper())

    #字符串全部小写
    print(nstr.lower())

    #字符串首字符变成大写
    print(bstr.title())
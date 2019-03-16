if __name__ == '__main__':
    #center方法
    mstr = "abcd"
    mcenter = mstr.center(10,"-")
    print(mcenter)

    #splitlines按行进行切割
    mstr2 = "abbcdaf\n dsfadavdsaewfas\ndsafsdavadsf \n"
    mline = mstr2.splitlines()
    print(mline)

    #partition方法 指定元素进行切割成元组 如果找到该元素 只切割一次
    mstr3 = "hiohiohihihi"
    mp =  mstr3.partition("o")
    print(mp)

    #去除左边空格
    mstr4 = "  abc  "
    mlstrip = mstr4.lstrip()
    print(mlstrip)

    #去除右边空格
    mstr5 = "  abc  "
    mrstrip = mstr5.lstrip()
    print(mrstrip)

    #join拼接字符串
    a = "abc"
    b = "def"
    c = a.join(b)
    print(c+"---------------------------")

    print(6^7)
if __name__ == '__main__':

    ##
    # print输出 print
    #
    # #///

    #定义变量
    username = "zhangsan"
    upassword = "123456"
    usex = "man"

    #默认print输出
    print(username,upassword,usex)

    #print输出不换行 用end()表示
    print(username, upassword, usex,end = "")

    #print参数之间去掉分隔符 用sep参数实现
    print(username,upassword,usex,sep="")

    #print参数之间用-代替
    print(username,upassword,usex,sep="-")

    #print格式化输出
    print("我的用户名是:{0}".format(username))


if __name__ == '__main__':
    #打开文件 访问方式只读
    myfile1 = open(r"C:\Users\SXY\PycharmProjects\pyworkspace\day04\file\hello.c","r")
    # 打开文件 访问方式只写
    myfile2 = open(r"C:\Users\SXY\PycharmProjects\pyworkspace\day04\file\hello.c","w")

    #测试文件是否可写
    mybool = myfile2.writable()
    print(mybool)

    #向文件写入文件
    mwrite = myfile2.write("hello")
    print(mwrite)

    #向文件写入多行内容
    mlist = ["\n123\n","456\n","789\n"]
    myfile2.writelines(mlist)

    #关流
    myfile2.close()

    #判断该文件是否可读
    mybool2 = myfile1.readable()
    print(mybool2)

    #向文件读取全部内容
    mread = myfile1.read()
    print(mread)

    #设置文件指针 每当文件读取过后指针将在最后一位 如在读取将读取不到任何内容
    myfile1.seek(0)

    #从文件中的读取一行
    myreadline = myfile1.readline()
    print(myreadline)

    # 设置文件指针 每当文件读取过后指针将在最后一位 如在读取将读取不到任何内容
    myfile1.seek(0)

    #从文件中读取多行 读取多行是 返回值是以列表的方式返回
    myreadlines = myfile1.readlines()
    print(myreadlines)

    #返回当前指针位置
    mytell = myfile1.tell()
    print(mytell)



    #open方法使用with语句
    with open(r"C:\Users\SXY\PycharmProjects\pyworkspace\day04\file\hello.c","r") as f :
        f.seek(0)
        while True :
            mf =  f.read()

            if mf == "" :
                break
            else:
                print(mf, end="")

        f.seek(0)

        mlist = list(f)

        for i in mlist :
            print(i,end="-")


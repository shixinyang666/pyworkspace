if __name__ == '__main__':
    ###
    #列表增删
    # ///

    #创建列表的两种方式
    mstr = list()
    mnum = []

    #添加元素的两种方式
        #append添加到结尾
    mstr.append("张三")
        #insert添加 可通过下标来添加
    mstr.insert(0,"李四")
        #输出
    print(mstr)

    #删除元素的两种方法
        #pop删除
    mstr.pop()
        #输出
    print(mstr)
        #remove删除 可指定元素
    mstr.remove("李四")
        #输出
    print(mstr)

    #删除列表 清空列表
    mlist = [1,2,3,4,5,6,7,8,9,10]
        #clear清空列表
    mlist.clear()
        #输出
    print(mlist)
        #del删除列表 也可以指定下标进行删除
    del mlist



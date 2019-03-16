import random
if __name__ == '__main__':
    ###
    #通过id()可以判断一个list是不是重新创建的
    # 根据id()的返回值是否相同来判断是否一致
    # ///

    #创建一个列表
    mnum = [1,2,3,4,5,6,7,8,9,10]
    #获取mnum列表进行切片 负数下标实现切片操作
    nnum = mnum[-2:-5:-1]

    #打印id的值
    print("mnum -->",id(mnum))
    print("nnum -->",id(nnum))

    #创建列表
    onum = [v for v in range(1,11)]
    print(onum)

    #创建列表第一种方法
    mnum1 = [v for v in mnum]
    print(mnum1)
    #创建列表第二种方法
    mnum2 = [v for v in mnum if v % 2 ==0]
    print(mnum2)
    #创建列表第三种方法
    mstr = [["a","b"],["c","d"],["e","f"]]
    mstr1 = [[n,m] for n,m in mstr ]
    print(mstr1)
    #随机生成整数
    mnum3 = [random.randint(1,10) for i in range(1,10)]
    print(mnum3)
    #复制
    mnum4 = mnum[:]
    print(mnum4)
#函数模块
import  day04.operation.p1 as p
if __name__ == '__main__':
    #定义字典存入功能名称
    mdict = {
                1:"输入用户姓名及性别，然后给出下列的提示",
                2:"随机生成两个分别包含10和15个整数的列表，并计算输出两个列表的并集",
                3:"注意一个用户信息，包含EMAIL号，判断信息是否合法，如果合法则输出相关信息",
                4:"从键盘输入一行字符串，判断是否是回文数"
             }
    #定义字典存入功能函数
    mfun = {
                1:p.checkSex,
                2:p.randomNum,
                3:p.email,
                4:p.huistr
            }

    #选择界面
    while True :
        print()
        for k in mdict.keys():
            print("{0}:{1}".format(k, mdict[k]))
        #输入功能编号
        mnum = int(input("请选择要实现的功能:"))

        if 1 == mnum :
            mname = input("请输入姓名:")
            msex = input("请输入性别:")
            mfun[1](mname,msex)
        elif(2 == mnum):
            mfun[2]()
        elif(3 == mnum):
            meamim = input("请输入邮箱:")
            mfun[3](meamim)
        elif(4 == mnum):
            mstr = input("请输入字符串:")
            mfun[4](mstr)
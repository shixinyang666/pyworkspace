#函数模块
import day04.demo01 as dd

if __name__ == '__main__':
    #定义字典 并存入标题
    mtitle = {
                1:"输入某年某月某日，判断这一天是这一年的第几天",
                2:"输入两个人的出生月份，来计算两个人的缘分",
                3:"随机生成一个序列，再次生成一个整数，查看这个整数有没有在序列中",
                4:"随机生成一个序列，10个元素，并对序列进行升序排序",
                5:"退出"
            }
    #定义字典 存入函数
    mfun = {
                1:dd.myyear,
                2:dd.mymonth,
                3:dd.randomnum,
                4:dd.listsort
            }

    #选择功能
    while True :
        #循环打印标题
        for k in mtitle.keys() :
            print("{0}.{1}".format(k,mtitle[k]))

        #抓取异常 避免未输入功能编号而程序崩溃
        try:
            # 输入功能编号
            mnum = int(input("请输入功能编号:"))

            # 判断功能编号并调用
            if mnum == 1:
                myyear = input("请输入年月日 格式-yyyymmdd:")
                mfun[1](myyear)
            elif (mnum == 2):
                mmonth1 = int(input("请输入第一个人的出生月份:"))
                mmonth2 = int(input("请输入第二个人的出生月份:"))
                mfun[2](mmonth1, mmonth2)
            elif (mnum == 3):
                mfun[3]()
            elif (mnum == 4):
                mfun[4]()
            elif (mnum == 5):
                print("退出程序!!!")
                break
        except Exception :
            print("请输入功能编号!!!")



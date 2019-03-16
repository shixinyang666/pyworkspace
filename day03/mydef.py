#定义函数
def fun01() :
    print("以调用函数fun01")
#接收单个参数
def fun02(v) :
    print("传过来的值:{v}".format(v=v))
#函数返回值
def fun03() :
    return 666

#函数炫耀传递两个参数
def fun04(name,password) :
    print("name={name},password={password}".format(name=name,password=password))

#函数参数默认值可以用传递默认值的参数
def fun05(name,pwd="123") :
    print("name={name},password={password}".format(name=name,password=pwd))

#函数中把实参变成可选择的
def fun06(name,pwd,sex="") :
    if sex == "" :
        print("name={name},password={password}".format(name=name,password=pwd))
    else:
        print("name={name},password={password},sex={sex}".format(name=name, password=pwd,sex=sex))

#返回一个字典
def fun07(name,pwd,sex="") :
    if sex == "":
        user = {"username":name,"password":pwd}
    else:
        user = {"username": name, "password": pwd,"sex":sex}

    return user


#接收列表
def fun08(user) :
    print(user)

#在形参前加上一个* 好所有的值封装到这个元组中
def fun09(*num) :
    print(type(num))
    for i in num :
        print(i)

#在形参前加上两个* 所有的值封装到这个字典里
def fun10 (**mydict) :
    print(type(mydict))
    for k in mydict.items():
        print(k)
#程序入口
if __name__ == '__main__':
    #调用函数
    fun01()

    #传递一个实参
    fun02(666)

    #接受返回值
    print(fun03())

    #传递关键字实参给函数
    fun04(name="zhangsan",password="123")

    #传递关键字实参，函数是有默认值的可以不用传递实参
    fun05(name="lisi")

    #把实参变成可选的，不是所有调用函数的都有sex所有把sex放到最后
    # 假如放到前面的话会编译异常
    fun06("wangwu","456")
    fun06("tianqi","789","man")

    #调用函数返回一个字典
    user = fun07("zhangsan","000","man")
    print(user)

    #传递列表
    fun08(user)

    #传递元组
    fun09(1,2,3,4,5,6)

    #传递键值
    fun10(k=10,v=20)
#冒泡排序的函数实现
def babo_reserve(var):
    for i in range(len(var)-1):
        for k in range(len(var)-1-i):
            if var[k] > var[k+1]:
                var[k],var[k+1] = var[k+1],var[k]
    return var
#调用实验：
def get_num():
    ls = []
    a = input("请输入列表中的元素：")
    while a != "":
        ls.append(a)
        a = input("请输入列表中的元素：")
    return ls
ls = get_num()
print(babo_reserve(ls))

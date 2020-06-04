#杨辉三角前n行打印的函数实现：
#方法1：
def Yanghui(n):
    result = [] #结果是一个大列表
    row = [1] #第一行
    result.append(row)
    for i in range(1,n+1):
        next_row = [1]
        for k in range(len(row)-1):     #上一行的长度减去1次
            next_row.append(row[k]+row[k+1])
        next_row.append(1)
        result.append(next_row)
        row = next_row
    for j in result:
        print(j,end="\n")
Yanghui(10)
    

#从用户输入获取一个二维列表的函数实现：
def get_list2():
    result=[]
    while True:
        mid_carry = input("元素1，元素2，元素3，......，元素n，用空格分隔，按回车结束：")
        if mid_carry == "":
            break
        mid_carry = mid_carry.split(" ")
        result.append(mid_carry.copy())
    return result
print(get_list2())
            
                
                
                

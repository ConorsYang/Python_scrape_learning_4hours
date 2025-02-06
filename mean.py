total = 0
count = 0
result = 0
print("这是一个求平均值的program")
data_input = input("请输入您想输入的数字：")
while data_input != "q":
    total += float(data_input)
    count += 1
    data_input = input("请输入您想输入的数字：")
if count == 0:
    result = 0
else:
    result = total / count
print("您所求的平均值为："+str(result))



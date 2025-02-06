#user_BMI
# user_weight = float(input("您的体重是(kg)："))
# user_height = float(input("您的身高是(m)："))
# user_BMI = user_weight / user_height ** 2
# print("您的BMI是:"+str(user_BMI))

def calculate_BMI(weight, height):
    BMI = weight / height ** 2
    if BMI <=18.5:
        category = "偏瘦"
    elif BMI <= 25.5:
        category = "正常"
    else:
        category = "肥胖"
    print(f"您的BMI为：{category}")
    return BMI

print(calculate_BMI(90,1.74))

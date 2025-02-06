# 定义一个学生类
# 要求：
# 1. 属性包括学生姓名、学号，以及语数英三科成绩
# 2. 能够设置某学生某科目的成绩
# 3. 能够打印出该学生的所有科目成绩

class Student:
    # def __init__(self, name, id, grade_Chinese, grade_math, grade_English):
    def __init__(self, name, id):
        self.name = name
        self.id = id
        # 有初始值就可以不用定义，后续可以直接修改
        # 一个字典搞定对应关系
        self.grades = {"语文": 0, "数学": 0, "英语": 0}
        # self.grade_Chinese = grade_Chinese
        # self.grade_math = grade_math
        # self.grade_English = grade_English

    # def modify_grage_Chinese(self, grade):
    #     self.grade_Chinese = grade
    #
    # def modify_grage_math(self, grade):
    #     self.grade_math = grade
    #
    # def modify_grage_English(self, grade):
    #     self.grade_English = grade
    # 指定科目，指定成绩，一个函数搞定
    def set_grage(self, course, grade):
        if course in self.grades.keys():
            self.grades[course] = grade

    def print_grades(self):
        print(f"学生{self.name} 学号{self.id}的所有成绩为：")
        for course in self.grades:
            print(f"{course}的成绩为：{self.grades[course]}分")


chen = Student("小陈", "100618")
zeng = Student("小曾", "100622")
zeng.set_grage("语文", 67)
zeng.set_grage("数学", 88)
zeng.print_grades()
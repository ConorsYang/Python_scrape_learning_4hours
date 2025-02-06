with open(".\\test.txt", "r", encoding="utf-8") as f:
    print(f.readline())
    print(f.readline())
    print(f.read(3))

    print(1)

with open(".\\test1.txt", "w", encoding="utf-8") as file:
    file.write("我欲乘风归去，\n又恐琼楼玉宇，\n高处不胜寒。")

with open(".\\test1.txt", "a", encoding="utf-8") as file:
    file.write("\n起舞弄清影，\n何似在人间。")


# 作者：于会飞
# 日期：2021.4.9
# 主题：复习巩固基础知识

# 字符串
message = "test word"
print(message) 

message = '单引号的字符串，可以兼容"包含双引号"的字符串！' 
print(message)  

name = "test firST wORd !"
print(name.title()) 
print(name.upper())
print(name.lower())

# 变量
first_name = "tina"
last_name ="yu"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()} !")

# 空白：空格、制表符、换行符
print("Languages: python java c c++")
print("Languages:\tpython\tjava\tc\tc++")
print("languages:\npython\njava\nc\nc++")
print("languages:\n\tpython\n\tjava\n\tc\n\tc++")#先换行再缩进
print("languages:\t\npython\t\njava\t\nc\t\nc++")#先缩进再换行

# 去除空白
delete_space = ' python '
print(delete_space)
print(delete_space.rstrip())
print(delete_space.lstrip())
print(delete_space.strip())
delete_space=delete_space.rstrip()
print(delete_space)

# 习题一
person_name = " eric "
massage = f'Hello {person_name.title().strip()}, \n\tdabai ask you:"would you like to learn some Python today ?"'
print(massage)

# 运算
num1 = 0.2 + 0.1
num2 = 1+2.0
num3 = 3.0 **2
num4 = 140_000_000_000
num5, num6, num7 = 1, 0.5, -3.77
print(num1, num2, num3, num4, num5, num6, num7                            )

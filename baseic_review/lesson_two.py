# 作者：Tina Yu
# 时间：2021.4.10
# 主题：基础巩固复习第二课

# List
bycycles = ['trek','cannondale', 'redline', 'specialized']
print(bycycles)
print(bycycles[1].title())
print(bycycles[-2].title())

bycycles[1] = 'bycycle'
print(bycycles)

bycycles.append('bycycle1')
print(bycycles)

bycycles.insert(2, 'bycycle2')
print(bycycles)

del bycycles[1]
print(bycycles)

pop_test = bycycles.pop(2)
print(bycycles)
print(pop_test)

bycycles.remove('specialized')
print(bycycles)


friends = ['Viki', 'jiuling', 'jianghuan', 'huahua']
print(f"Hi {friends[0]}, you are my best friend!")


# for循环
lessons = ['lesson1', 'lesson2', 'lesson3']
for lesson in lessons:
	print(f"\n\n\t这是课节名称：{lesson} !\n")
print("========================循环已结束====================")
 

#排序
fruits = ['ass', 'kdi', 'bde', 'adde']
print(sorted(fruits))
print(fruits)
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
fruits.reverse()
print(fruits)
print(len(fruits))
print("*********************************************************")

# range
nums = []
for num in range(1,10):
	square=num**2
	nums.append(square)
	print(nums)
print(f"==================这是最终的nums：{nums}======================")
print(f"最大值为：{max(nums)}")
print(f"最小值为：{min(nums)}")
print(f"总和为：{sum(nums)}")

squares = [num**2 for num in range(1,5)]
print(f"列表解析的结果：{squares}")


# 切片
players = ['p1', 'p2', 'p3', 'p4']
print(players[1:4])
print(players[:3])
print(players[1:])
print(players[-3:-1])
copy_player = players[:]
print(copy_player)
players.append("p6")
copy_player.append("p5")
print(players)
print(copy_player)
print(f"The first three items are: {players[:3]}")
print(f"Three items from the middle of the list are: {players[1:4]}")
print(f"The last three items in the list are: {players[-3:]}")


# 元祖
print("\n\n\n====================开始复习元祖=================\n")
test_tuples = ("火锅", "烤肉", "炒菜", "烧烤")
print("以下品类可供参考：")
for test_tuple in test_tuples:
	print(test_tuple)


	def test_lent():
		a = len(str(9999999999999999999999))
		print(a)
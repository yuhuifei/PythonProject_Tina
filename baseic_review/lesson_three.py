# 作者：Tina Yu
# 时间：2021.4.10
# 主题：基础知识巩固复习

# 字典
alien_0 = {'color':"green", 'points':5}
print(alien_0['color'])
print(alien_0['points'])
alien_0['x_point'] = 0
alien_0['y_point'] = 25
print(alien_0)
alien_0['color'] = 'yello'
print(alien_0)

alien_0 = {'x_position' : 0, 'y_position' : 25, 'speed' : 'fast'}
print(f"Original position: {alien_0['x_position']}")
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")


#遍历字典
user_0 = {
	'user_name': 'Tina Yu',
    'first_name': 'Tina',
    'last_name': 'Yu'
}
for key, value in user_0.items():
	print(f"\nKey: {key}")
	print(f"value: {value}")

favorite_languages = {
	'zhang': 'python',
	'li': 'c',
	'zhao': 'java',
	'qian': 'python'
}
for name in favorite_languages.keys():
	print(name.title())



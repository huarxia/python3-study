# 请写一个程序打印出 0~100 所有的奇数。
i = 0
maxNum = 100
# 定義一個字符串保存所有的奇數
oddStr = ''
while i <= maxNum:
	if i % 2 != 0:
		oddStr += str(i)
		oddStr += ' '
	i += 1
print(oddStr)

# 公元年数可被4整除（但不可被100整除）为闰年,但是正百的年数必须是可以被400整除的才是闰年。其他都是平年 

year = input('請輸入一個公元年數: ')
isLeapYear = False

while not year.isdigit():
	year = input('您輸入不是一個公元年數,請重新輸入: ')
# 轉換為int類型
year = int(year)
if (year % 100 == 0 and year % 400 == 0):
	isLeapYear = True
elif (year % 4 == 0 and year % 100 != 0):
	isLeapYear = True
else:
	isLeapYear = False
# 轉換為str
year = str(year)
if isLeapYear:
	print(year + '年,是閏年~~')
else:
	print(year + '年,不是閏年~~')

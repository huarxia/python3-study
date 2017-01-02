# @file:      變量計算一年多少秒
# @author:    花夏(liubiao@itosx.com)
# @version:   V0.0.1
# @date:      2016-12-31 16:28:36

daysPerYear = 365
hoursPerDay = 24
minutesPerHour = 60
secondsPerMinutes = 60
result = daysPerYear * hoursPerDay * minutesPerHour * secondsPerMinutes
result = str(result)
print('一年有：' + result + '秒')

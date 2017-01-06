# 有红、黄、蓝三种颜色的球
# 其中红球 3 个，黄球 3 个，绿球 6 个
# 先将这 12 个球混合放在一个盒子中，从中任意摸出 8 个球，编程计算摸出球的各种颜色搭配。

# 首先摸出8個球中綠色至少2個，因為紅黃球總共是6個
# 所以綠球的範圍是 range(2, 7)
# 紅球的範圍是 range(0, 4)
# 黃球的範圍是 range(0, 4)

print('--------* 三色球問題 *--------')

sumNum = 8
for green in range(2, 7):
    for red in range(0, min(4, sumNum - green + 1)):
        # min(4, sumNum - green + 1) 這裡取 sumNum - green + 1
        # 是因為sumNum - green這個數是可以range取到的
        if sumNum - green - red <= 3:
            print('綠球:', green, '紅球:', red, '黃球:', sumNum - green - red)

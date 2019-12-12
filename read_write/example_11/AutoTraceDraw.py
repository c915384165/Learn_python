#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import turtle as t
# 初始化
t.title("自动轨迹绘制")
t.setup(800, 600, 0, 0)
t.pencolor("red")
t.pensize(5)

# 数据读取


def read_data(file_name):
    datals = []
    f = open(file_name)
    for line in f:
        line = line.replace("\n", "")
        datals.append(list(map(eval, line.split(","))))
    f.close
    return datals


# 接口：
# 0:前进；1: 方向<0> left, <1> right; 2: angle value; 3&4&5: RGB color;6: type of  line or circle
# 自动绘制


def draw_line(datals):
    for i in range(len(datals)):
        # 当为1时候画图，否则pass，相当于注释
        if datals[i][7]:
            # 绘直线
            if datals[i][6] == 0:
                t.pencolor(datals[i][3], datals[i][4], datals[i][5])
                t.fd(datals[i][0])
                if datals[i][1]:
                    t.right(datals[i][2])
                else:
                    t.left(datals[i][2])
            # wait for
            # 添加了绘曲线的部分
            elif datals[i][6] == 1:
                t.pencolor(datals[i][3], datals[i][4], datals[i][5])
                if datals[i][1]:
                    t.circle(datals[i][0], datals[i][2])
                else:
                    t.circle(datals[i][0], datals[i][2]*(-1))
            else:
                pass
        else:
            pass




def main():
    datals = read_data('data.txt')
    draw_line(datals)


main()

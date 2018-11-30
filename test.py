# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 22:49:34 2018

@author: lenovo
"""

global NUM
NUM = 0


class MCNode:
    def __init__(self, m=3, c=3, b=1, num=0):  # 初始化
        self.m = m
        self.c = c
        self.b = b
        self.num = num

    def __eq__(self, other):  # 判断是否相等 重构==
        if (self.m == other.m and self.c == other.c and self.b == other.b):
            return True
        else:
            return False

    def isGoal(self):  # 是否为目标状态
        if (self.m == 0 and self.c == 0 and self.b == 0):
            return True
        else:
            return False

    def stateIsLegal(self):  # 是否合法
        if self.m < 0 or self.c < 0 or self.m > 3 or self.c > 3:
            return False
        if self.m < self.c and self.m > 0:
            return False
        if (3 - self.m) < (3 - self.c) and (3 - self.m) > 0:
            return False
        if self.m == 3 and self.c == 3 and self.b == 0:
            return False
        if self.m == 0 and self.c == 0 and self.b == 1:
            return False
        if self.m == 3 and self.c == 0 and self.b == 1:
            return False
        if self.m == 0 and self.c == 3 and self.b == 0:
            return False
        else:
            return True

    def visited(self, opend):  # 是否可以找到
        for o in opend:
            # if (self.m==MCNode(o).m and self.c==MCNode(o).c and self.b==MCNode(o).b):
            if (self == o):
                return True
        return False

m1 =  MCNode(3,3,1,0)
opend = []
opend.append(m1)
m1.visited(opend)
# opend = []
# closed =[]
# opend.append(m1)
# m1.procedding(opend,closed)

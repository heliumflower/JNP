# -*- coding: utf8 -*-
import xlrd
import random

pc=0.8
pm=0.2
delta_k=3
delta_h=1

# for i in range(1, 10):
#     p=table.cell(i,0).value
#     print q
# for i in range(1, 10):row
#     q = table.cell(i, 1).value/1000*table.cell(i, 2).valuerow
#     print q

zdmfa = []
#读取数据zdmfa
data = xlrd.open_workbook('data.xlsx')
table = data.sheet_by_name(u'坡道数据')
z = []
for row in range(1,11):
    p = table.cell(row, 0).value
    q = table.cell(row, 1).value / 1000 * table.cell(row, 2).value
    z.append([p,q])

for i in range(0,9):
    zdmfa.append(z)
# zdmfa=[
#     [[10, 1],[5, 2],[9, 1],[9, 2],[12, 3],[13, 2],[7, 1],[5, 1],[14, 3],[11, 4]],
#     [[10, 1],[5, 2],[9, 1],[9, 2],[12, 3],[13, 2],[7, 1],[5, 1],[14, 3],[11, 4]],
#     [[10, 1],[5, 2],[9, 1],[9, 2],[12, 3],[13, 2],[7, 1],[5, 1],[14, 3],[11, 4]],
#     [[10, 1],[5, 2],[9, 1],[9, 2],[12, 3],[13, 2],[7, 1],[5, 1],[14, 3],[11, 4]],
#     [[10, 1],[5, 2],[9, 1],[9, 2],[12, 3],[13, 2],[7, 1],[5, 1],[14, 3],[11, 4]],
#     [[10, 1],[5, 2],[9, 1],[9, 2],[12, 3],[13, 2],[7, 1],[5, 1],[14, 3],[11, 4]],
#     [[10, 1],[5, 2],[9, 1],[9, 2],[12, 3],[13, 2],[7, 1],[5, 1],[14, 3],[11, 4]],
#     [[10, 1],[5, 2],[9, 1],[9, 2],[12, 3],[13, 2],[7, 1],[5, 1],[14, 3],[11, 4]],
#     [[10, 1],[5, 2],[9, 1],[9, 2],[12, 3],[13, 2],[7, 1],[5, 1],[14, 3],[11, 4]],
#     [[10, 1],[5, 2],[9, 1],[9, 2],[12, 3],[13, 2],[7, 1],[5, 1],[14, 3],[11, 4]]
# ]
#
# 交叉
random.shuffle(zdmfa)
sum=len(zdmfa)
n=int(sum*pc/2)
number=len(zdmfa[0])
for i in range(0,n):
    for j in range(0,number):
         a=random.random()
         b1=0.5+a
         b2=0.5-a
         zdmfa[2*i][j][0]=b1*zdmfa[2*i][j][0] +b2*zdmfa[2*i+1][j][0]
         zdmfa[2*i][j][1]=b1*zdmfa[2*i][j][1] +b2*zdmfa[2*i+1][j][1]
         # zdmfa[2*i+1][j][0]=b1*zdmfa[2*i][j][0] +b2*zdmfa[2*i+1][j][0]
         # zdmfa[2*i+1][j][1]=b1*zdmfa[2*i][j][1] +b2*zdmfa[2*i+1][j][1]
#print zdmfa


# 变异
array=range(0,sum)
random.shuffle(array)
n1=len(array)
n2=int(sum*pm)
for i in range(0,n2):
    for j in range(min(array[0], array[1]),max(array[0], array[1])):
        a1=random.randint(-delta_k, delta_k)
        a2=random.randint(-delta_h, delta_h)
        zdmfa[i][j][0] = a1+zdmfa[i][j][0]
        zdmfa[i][j][1] = a2+zdmfa[i][j][1]
print zdmfa

# for i in range(0,len(zdmfa)):
#     print zdmfa[i]
#     print '\n'

print zdmfa

#
#
# # zdmfa.append([])
# # zdmfa[2].append([666,888])
# # zdmfa[2].append([123,06])
#
#
#
#
#
#
#
#
#
#

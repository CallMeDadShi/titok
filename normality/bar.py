# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

#条形图绘制


likes=[0, 0, 0, 0, 0, 1, 1, 1, 3, 3, 6, 82, 1935, 8197, 8198, 8294, 8294, 8458, 8458, 9073, 12930, 15572, 15572, 18099, 23697, 23805, 24131, 24657, 24657, 25775, 27454, 28047, 28047, 32569, 38920, 45075, 45075, 49617, 51673, 66354, 68241, 70271, 70271, 70621, 76903, 80670, 80670, 83996, 83996, 110010, 110011, 110548, 114015, 115506, 120167, 150706, 150708, 172963, 186723, 190336, 190336, 199726, 221970, 222880, 222880, 267660, 282896, 282899, 284761, 284761, 331484, 345166, 345168, 379099, 413130, 420233, 420234, 440003, 448500, 448500, 547829, 547829, 612469, 612472, 639917, 719088, 1176491, 1176491, 1228956, 1228956, 1257544, 1379461, 1446799, 1446799, 1744101, 1771246, 2915208, 5924576, 16046526]
shares=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 113, 321, 381, 473, 610, 965, 1650, 1650, 1751, 1751, 1766, 1799, 1799, 2014, 2014, 2149, 2337, 2453, 2507, 2507, 3300, 3300, 4589, 4589, 4610, 4966, 5618, 5857, 6208, 6492, 6764, 7131, 9212, 9212, 10035, 10531, 10531, 11844, 13971, 13971, 14377, 14505, 15867, 17539, 17539, 17731, 17731, 19644, 19703, 20420, 20527, 20685, 22521, 22521, 26503, 26503, 27131, 28134, 28134, 32127, 32127, 32829, 36764, 36764, 39509, 41687, 52113, 52113, 53315, 53315, 55393, 58633, 58633, 69390, 69390, 72730, 90642, 91855, 94909, 94909, 96181, 96181, 170415, 171702, 171702, 196496, 206130]
comments=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 18, 61, 121, 121, 251, 272, 272, 297, 297, 347, 347, 384, 430, 433, 433, 433, 546, 615, 626, 684, 726, 726, 880, 940, 963, 996, 1120, 1210, 1210, 1240, 1240, 1354, 1354, 1429, 1429, 1493, 1517, 1640, 1728, 1728, 1837, 1897, 1897, 2026, 2128, 2252, 2252, 2329, 2329, 2412, 3274, 3323, 3323, 3349, 3407, 4333, 4659, 5762, 5762, 6026, 6423, 6423, 6471, 6485, 7595, 10298, 10310, 10310, 10657, 10657, 11540, 11540, 13216, 13216, 20806, 22019, 22019, 24221, 27484, 27484, 36514, 47475, 51530, 59507, 59507, 89852, 180565, 662917]


a=['<1w','1w~10w','10w~50w','50w~100w','100w+']#1w,1w~10w.10w~50w,50w~100w,100w+
likes_group = [0,0,0,0,0]
comment_group=[0,0,0,0]
shares_group=[0,0,0,0,0]

for i in likes:
    if i<=10000:
        likes_group[0]+=1
    elif i>10000and i<=100000:
        likes_group[1]+=1
    elif i>100000and i<=500000:
        likes_group[2]+=1
    elif i>500000and i<=1000000:
        likes_group[3]+=1
    else:
        likes_group[4]+=1

for i in shares:
    if i<=10000:
        shares_group[0]+=1
    elif i>10000and i<=100000:
        shares_group[1]+=1
    elif i>100000and i<=500000:
        shares_group[2]+=1
    elif i>500000and i<=1000000:
        shares_group[3]+=1
    else:
        shares_group[4]+=1

c=['<500','500~5k','5k~5w',"5w+"]
for i in comments:
    if i<=500:
        comment_group[0]+=1
    elif i>500and i<=5000:
        comment_group[1]+=1
    elif i>5000and i<=50000:
        comment_group[2]+=1
    else:
        comment_group[3]+=1

# plt.bar(a, likes_group, label='likes', color='#db639b')

#plt.bar(a, shares_group, label='shares')
#
plt.bar(c, comment_group, label='comments',color='#e16531')
# params

# x: 条形图x轴
# y：条形图的高度
# width：条形图的宽度 默认是0.8
# bottom：条形底部的y坐标值 默认是0
# align：center / edge 条形图是否以x轴坐标为中心点或者是以x轴坐标为边缘

plt.legend()

plt.xlabel('number')
plt.ylabel('value')


plt.show()
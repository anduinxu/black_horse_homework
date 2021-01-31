import numpy as np
import pandas as pd


grades=pd.DataFrame([[68,65,30],[95,76,98],[98,65,88],[90,88,77],[80,90,90]],index=['张飞','关羽','刘备','典韦','许诸'],columns=['语文','数学','英语'])
# grades=pd.read_excel('成绩.xlsx')
# print(grades)
print('average of yuwen is',grades['语文'].mean())
print('average of english is',grades['英语'].mean())
print('average of math is',grades['数学'].mean())

print('average of yuwen is',grades['语文'].min())
print('average of english is',grades['英语'].min())
print('average of math is',grades['数学'].min())

print('average of yuwen is',grades['语文'].max())
print('average of english is',grades['英语'].max())
print('average of math is',grades['数学'].max())

print('average of yuwen is',grades['语文'].var())
print('average of english is',grades['英语'].var())
print('average of math is',grades['数学'].var())

print('average of yuwen is',grades['语文'].std())
print('average of english is',grades['英语'].std())
print('average of math is',grades['数学'].std())

grades['total_grades']=grades.apply(lambda x:x.sum(),axis=1)
print(grades.sort_values('total_grades',ascending=False))
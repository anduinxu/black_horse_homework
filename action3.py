import numpy as np
import pandas as pd


with open('car_complain.csv','r',encoding='utf-8') as file:
    complains=pd.read_csv(file)
    # print(complains['problem'])
    problem_list=[]
    for i in complains['problem']:
        problem_list.append(i.split(','))
    complains['problem2']=problem_list
    print(complains['problem2'])
    print(complains.groupby('brand').count())
    print(complains.groupby('car_model').count())
    print(complains.groupby(['brand','car_model']).count())

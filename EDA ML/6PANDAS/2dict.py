from pydoc import describe

import pandas as pd
import numpy as np
# dic={'id':[101,102,103,104,105],'Stud_Name':['Python','Java','DSA','C','R'],'Mark_1':[99,45,33,66,78],'Mark_2':[77,88,78,98,90],'Mark_3':[98,97,94,93,99]}
# a=pd.DataFrame(dic)
# print(a.describe(include='0'))
lst=[[101,'Vilas','PK',22,'Python','knr'],
     [102,'Thejus','PK',20,'Python','ekm'],
     [103,'Sreerag','PK',19,'Javascript','knr'],
     [104,'Sanay','S',22,'ACC','knr'],
     [105,'Ashwin','A',20,'DS','wyd'],
     [106,'Kelly','A',19,'java','Mlp'],
     [107,'Surya','P',14,'c','Mlp'],
     ]
df=pd.DataFrame(lst)
df.columns=['ID','FName','LName','Age','Prof','Loc']
# print(df.describe(include='object'))
# print(df.describe(include='all'))
df['salary']=[9000,8555,7444,3333,8888,5333,5454]
df['Gender']=['M','M','M','M','M','F','M']
df1=df.drop(['Prof'],axis=1)
print(df1)


import pandas as pd
import numpy as np
# a=pd.Series([2,3,4])
# print(a)
# a=pd.Series((1,3,2,4,5))
# print(a)
# print('*'*100)
# b=pd.Series({'Name':'Vilas','Age':22,})
# print(b)

# convert 1 to 50
# a=pd.Series(np.arange(1,51))
# print(a)
# #head() ---------> Returns first 5 datas  as default else that number
# print(a.head(10))
# #tail() ---------->Returns last 5 datas as default else that number
# print(a.tail(10))

# create a dic and conver it to series id fname lname age proffesion
# a=pd.Series({'Id':1,'Fname':'Vilas','Lname':'PK','Age':22,'Prof':'Python'},index=['Id','Fname','Age'])
# print(a)

# create 2 series and do add sub mul div
a=pd.Series([1,3,2])
b=pd.Series([6,8,3])
add=np.add(a,b)
print(add)
sub=np.subtract(a,b)
print(sub)
mul=np.multiply(a,b)
print(mul)
div=np.divide(a,b)
print(div)
#shape returns dimensions like (x,y,z)
# a=pd.Series([1,3,5,2,6,4,7,8,])
# print(a.shape,a.ndim)

#Join  ----------> Used to join 2 series  WE USE CONCAT(()) or a._APPEND(b) TO IGNORE INDEX NUMBER IGNORE INDEX=TRUE
# a=pd.Series([1,3,2,4])
# b=pd.Series([4,2,4,9])
# c=pd.concat((a,b),ignore_index=True)
# print(c)


#2D NESTED LIST
#ID FNAME LNAME AGE PROF LOC
# lst=[[101,'Vilas','PK',22,'Python','knr'],
#      [102,'Thejus','PK',20,'Python','ekm'],
#      [103,'Sreerag','PK',19,'Javascript','knr'],
#      [104,'Sanay','S',22,'ACC','knr'],
#      [105,'Ashwin','A',20,'DS','wyd'],
#      [106,'Kelly','A',19,'java','Mlp'],
#      [107,'Surya','P',14,'c','Mlp'],
#      ]
# df=pd.DataFrame(lst)
# df.columns=['ID','FName','LName','Age','Prof','Loc']
# print(df)
# print(df.shape)
# print(df.dtypes)
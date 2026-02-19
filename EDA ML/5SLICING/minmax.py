import  numpy as np
#MAX and MIN
# a=np.array([1,2,4,3,55,66,44])
# b=np.array([[1,4,2,33],[5,66,33,77],[66,4,33,99]])
# c=np.max(b,axis=1)
# print(c)

#ARGMAX ----> GIVES INDEX OF LARGEST NUMBER
# AND TRAVESE IN MUMERICAL ORDER INDEX

# a=np.array([[2,3,1],[5,6,3],[67,45,33]])
# b=np.argmax(a)
# c=np.argmin(a)
# print(a)
# print(b)
# print(c)

#FLOOR --------------> REMOVES THE DECIMAL PART
# a=np.array([[2.2,3.4,5.6,5.4,],[2.2,3.4,5.4,9.0],[3.4,9.9,6.7,7.6],[6.7,8.6,6.8,9.8]])
# print(np.floor(a))

#CEIL ------> MAPS TO HIGHEST INTEGER VALUE
# print(np.ceil(a))

#ROUND ------>ROUNDS TO NEXT INTEGER BASED ON FRACTIONAL PART IF ODD.5 ---MAPS TO NEXT ELSE EVEN.5 STAYS IN EVEN
# print(np.round(a))

a=np.array([2,4,5,3,1])
b=np.array([2,4,3,5,6])
c=np.concatenate((a,b))
print(c)
# we can target the data as x,y
from sklearn.datasets import load_wine
x,y=load_wine(return_X_y=True)
print(x)# x data 
print(y)# y data
#another type target the value using the parameter data and the target
from sklearn.datasets import load_linnerud
data=load_linnerud()
print(data.data,data.target)

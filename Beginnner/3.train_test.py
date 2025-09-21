from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

x,y=load_breast_cancer(return_X_y=True)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)#0.2 is 20% for testing
print(x_train)
datalen=len(x_train)
print(datalen)


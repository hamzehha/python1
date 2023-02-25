import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import  accuracy_score

df= pd.read_csv("diabetes.csv")
df.loc[df['BloodPressure'] == 0, 'BloodPressure'] =72
train, test = train_test_split(df,test_size=0.2)
#X_train ,Y_train
#X_test ,Y_test
train = pd.DataFrame(train)
X_tran = train.drop(columns=["Outcome"],axis=1)
Y_tran = train["Outcome"]
train = pd.DataFrame(train)
model= LogisticRegression(max_iter = 1000)
model.fit(X_tran,Y_tran)
#####
test = pd.DataFrame(test)
X_test = test.drop(columns=["Outcome"],axis=1)
Y_test = test["Outcome"]

pred = model.predict(X_test.iloc[:5])
#print(pred)
#print(Y_test[:5])
#print(df.shape)
print(accuracy_score(Y_test,pred))
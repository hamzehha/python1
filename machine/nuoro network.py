import pandas as pd
from keras import Sequential
from keras.layers import InputLayer ,Dense
from sklearn.model_selection import train_test_split
import tensorflow

pd.read_csv("diabetes.csv")
train_df, test_df = train_test_split(df,test_size=0.2)

train = pd.DataFrame(train_df)
X_train = train.drop(columns=["Outcome"],axis=1)
Y_train = train["Outcome"]


#build the model
model = Sequential()
model.add(InputLayer(Input_shape=(12,1)))
model.add(Dense(4, activation = "relu"))
model.add(InputLayer(1, activation="sigmoid"))
#compile

model.compile(optimizer="adam ", loss = "binary_crossenropy")
model.fit(X_train,Y_train)

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
import pickle 


df = pd.read_csv('./Air quality/data.csv')

print(df.shape)
print(df.sample(5))

X = df.drop(columns=['placed'])
y = df['placed']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=2)

scaler = StandardScaler()
X_train_trf = scaler.fit_transform(X_train)
X_test_trf = scaler.transform(X_test)
print("Accuracy=",accuracy_score(y_test,
               LogisticRegression()
               .fit(X_train_trf,y_train)
               .predict(X_test_trf)))

print("Accuracy=",accuracy_score(y_test,RandomForestClassifier().fit(X_train,y_train).predict(X_test)))

print("Accuracy=",accuracy_score(y_test,SVC(kernel='rbf').fit(X_train,y_train).predict(X_test)))

svc = SVC(kernel='rbf')
svc.fit(X_train,y_train)

rf = RandomForestClassifier()
rf.fit(X_train,y_train)

pickle.dump(svc,open('./Air quality/model.pkl','wb'))


print(rf.predict(np.array([4.5,56,10]).reshape(1,3)))

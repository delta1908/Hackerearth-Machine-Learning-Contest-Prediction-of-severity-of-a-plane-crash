import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier
from sklearn import preprocessing

data=pd.read_csv('train.csv')
print(data.head())

k=[]
for i in list(data['Severity']):
    if i not in k:
        k.append(i)
print(k)

l=list(data['Severity'])
for i in range(len(l)):
    if l[i]==k[0]:
        l[i]=0
    elif l[i]==k[1]:
        l[i]=1
    elif l[i]==k[2]:
        l[i]=2
    elif l[i]==k[3]:
        l[i]=3

print(l)
data['Severity']=l

# Initialsing X
# After implementing recursive feature elimination it was found that only 3 features are important
X=data[['Safety_Score', 'Days_Since_Inspection','Control_Metric']]
X['Days_Since_Inspection']=X['Days_Since_Inspection']*X['Safety_Score']
preprocessing.normalize(X)
Y=data[['Severity']]
print(X)
print(Y)

#Using GradientBoostingClassifier
reg=GradientBoostingClassifier(max_depth =8,n_estimators=1200).fit(X,Y)
test=pd.read_csv('test.csv')
X_test=test[['Safety_Score', 'Days_Since_Inspection','Control_Metric']]
X_test['Days_Since_Inspection']=X_test['Days_Since_Inspection']*X_test['Safety_Score']
preprocessing.normalize(X_test)
pred=reg.predict(X_test)


print(pred)
pred=list(pred)
for i in range(len(pred)):
    if pred[i]==0:
        pred[i]=k[0]
    elif pred[i]==1:
        pred[i]=k[1]
    elif pred[i]==2:
        pred[i]=k[2]
    elif pred[i]==3:
        pred[i]=k[3]
print(pred)

import csv
with open('predictions.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Accident_ID","Severity"])
    for i in range(len(pred)):
        writer.writerow([test["Accident_ID"][i],pred[i]])
print(X)

#Crossvalidation Set
from sklearn.model_selection import cross_validate
scoring=['accuracy','precision_macro','recall_macro']
scores=cross_validate(reg,X,Y,scoring=scoring,cv=5)
print(scores)
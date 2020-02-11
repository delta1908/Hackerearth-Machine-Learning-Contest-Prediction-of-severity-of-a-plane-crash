# Hackerearth-Machine-Learning-Contest-Prediction-of-severity-of-a-plane-crash
Prediction of severity of a plane crash

Model Used: GradientBoostingClassifier

Also I tried ensembling RandomForestClassifer,GradientBoostingClassifier,DecisionTreeClassifer with different hyper parameters like: max_depth, n_estimators, etc.

Implementing Recursive features elimination for automatic tuning of the number of features.

Important features: Safety_Score, Days_of_Inspection, Control_Metric

Feature Importances of Safety_Score, Days_of_Inspection, Control_Metric: array([0.14311583, 0.57658576, 0.28029841]) respectively.

max_depth(The maximum depth of the tree):8

n_estimators(The number of trees in the forest):1200

Crossvalidation score: {'test_accuracy': array([0.96601699, 0.96601699, 0.9725    , 0.9695    , 0.97747748]), 'train_accuracy': array([0.99962495, 0.99974997, 0.99975   , 0.999875  , 0.99975006]), 'test_precision_macro': array([0.96538563, 0.96623864, 0.97235075, 0.96851767, 0.97851166]), 'train_precision_macro': array([0.99966862, 0.9997013 , 0.99978298, 0.99988553, 0.99971331]), 'test_recall_macro': array([0.96566631, 0.96811274, 0.97331775, 0.96884035, 0.97656679]), 'train_recall_macro': array([0.99961063, 0.999795  , 0.99978298, 0.9998975 , 0.99978307])}

Test Score: 87.80235
World Rank: 10

Link to the Leaderboard: https://www.hackerearth.com/challenges/competitive/airplane-accident-severity-hackerearth-machine-learning-challenge/leaderboard/how-severe-can-an-airplane-accident-be-03e7a3f1/

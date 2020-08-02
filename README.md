# Heart-disease-prediction
Heart disease or Cardiovascular disease is one of the biggest causes of motality (i.e., causing 1 out of 4 deaths in the US) among the population of the world. Therefore, prediction of the Cardiovascular disease is considered one of the important subjects in the clinical data analysis. However, several contributory risk factors such as diabetes, high blood pressure, high cholesterol, abnormal pulse rate etc. lead to cardiac arrest. So, the purpose of this work is to predict if any patient has chances of having a heart disease or not. With this objective different models are trained using patients data collected by the Cleveland Clinic Foundation. The dataset (Cleveland) can be found in the 
following link:
https://archive.ics.uci.edu/ml/datasets/Heart+Disease

The following models are trained using the collected data.
• SVM
• Naive Bayes
• Logistic Regression
• Decision Tree
• Random Forest
• Extreme Gradient Boost
• Light Gradient Boost

The following methods are applied:
• KNN imputer has been applied to fill the missing values of the data.
• 10 most important features are selected using embeded feature selection (e.g., Extra Tree) and investigating correlation.
• The top features are used to train the aforementioned models.
• The best model achieved 90% accuracy (f1 = 0.90) in classifying patients with heart diease vs no heart disease.

# -*- coding: utf-8 -*-
"""Psychosocial Dimensions of Student Life.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14mY0yV4NnD7565_o7LCyoR9umKBg9fUR

#Dataset retrival
"""

# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All"
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session

dataset = pd.read_csv('/content/CSE_student_performances.csv')

"""# Preprocessing the dataset: handling null values, ensuring consistent shapes, and verifying data types."""

dataset.shape

dataset.dtypes

dataset.columns

dataset.isnull().sum()

dataset.fillna(0, inplace=True)
dataset.isnull().sum()

"""#Data Anaylsis"""

[21, 'Male', 'Good','Yes','Yes','No','8', 10, 'Yes']

dataset.head()

# make a correlation plot of gender and depressionstatus

import seaborn as sns
import matplotlib.pyplot as plt
sns.catplot(x='Gender', y='DepressionStatus', data=dataset, kind='bar', ci=None)
plt.xlabel('Gender')
plt.ylabel('Depression Status')
plt.title('Correlation between Gender and Depression Status')
plt.show()

# prompt: make correlation plot of SleepPerDayHours, DepressionStatus violin plot

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os
import seaborn as sns
import matplotlib.pyplot as plt

dataset = pd.read_csv('/content/CSE_student_performances.csv')

sns.violinplot(x='SleepPerDayHours', y='DepressionStatus', data=dataset)
plt.xlabel('Sleep Per Day Hours')
plt.ylabel('Depression Status')
plt.title('Correlation between Sleep Per Day Hours and Depression Status')
plt.show()

# according to the dataset if student have good performance on study and make a enough notes that has the high correlations with DepressionStatus
# a lit bit more deppressions on females
# a lot student make a note that's why the deprresive students more than other
# depression more at 21 age and sometimes depression at 23 age
# if student make a note that will be good academic performance
# less sleep cause more depressions

"""#Feature Engineering"""

from sklearn.preprocessing import LabelEncoder, OrdinalEncoder, StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer

ordinal = ['AcademicPerformance', 'TakingNoteInClass', 'FaceChallangesToCompleteAcademicTask', 'LikePresentation', 'LikeNewThings']
scale = ['SleepPerDayHours', 'NumberOfFriend']
ohe = ['Gender']

preprocessor = ColumnTransformer(
    transformers=[
        ('ordinal', OrdinalEncoder(), ordinal),
        ('scale', StandardScaler(), scale),
        ('ohe', OneHotEncoder(), ohe)
    ])

from sklearn.ensemble import RandomForestClassifier
# from sklearn.ensemble import ExtraTreesClassifier
# from sklearn.tree import DecisionTreeClassifier
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('imputer', SimpleImputer(strategy='mean')),
    ('classifier', RandomForestClassifier())
])

"""#Training and Model Selection"""

X = dataset.drop(['DepressionStatus'], axis=1)
y = dataset['DepressionStatus']

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

"""##Custom model selection"""

pip install lazypredict

from lazypredict.Supervised import LazyRegressor
from lazypredict.Supervised import LazyClassifier

clf = LazyClassifier(verbose=0, ignore_warnings=False, custom_metric=None)
models, predictions = clf.fit(X_train, X_test, y_train, y_test )
models

"""##Training"""

label = LabelEncoder()
y_train_label = label.fit_transform(y_train)
y_test_label = label.transform(y_test)

pipeline.fit(X_train, y_train_label)

accuracy = pipeline.score(X_test, y_test_label)
print(f'Model Accuracy: {accuracy}')

"""#Testing

##Analysis of prediction
"""

plt.figure(figsize=(8, 4))
importances = pipeline.named_steps['classifier'].feature_importances_
indices = np.argsort(importances)[::-1]
features = X.columns
sns.barplot(x=importances[indices], y=[features[i] for i in indices], palette='Blues_d')
plt.title('Feature Importances - Random Forest Classifier')
plt.xlabel('Relative Importance')
plt.ylabel('Features')
plt.show()

sns.pairplot(data=dataset, hue="DepressionStatus")

"""##Custom testing"""

columns = ['Age ', 'Gender', 'AcademicPerformance', 'TakingNoteInClass',
       'FaceChallangesToCompleteAcademicTask',
       'LikePresentation', 'SleepPerDayHours', 'NumberOfFriend',
       'LikeNewThings']

data_test = pd.DataFrame([[25, 'Male', 'Good','No','No','Yes',10, 90, 'Yes']], columns=columns)
for col in data_test.columns:
        print(col,": ", data_test[col].values)
result = pipeline.predict(data_test)
result

confidence = pipeline.predict_proba(data_test)
confidence
#array(['Sometimes', 'Yes', 'No'], dtype=object)

"""#Save Pipeline"""

import joblib

filename = 'my_pipeline.pkl'
joblib.dump(pipeline, filename)

print("Pipeline saved as", filename)

pipeline = joblib.load('my_pipeline.pkl')
pipeline.predict(data_test)
pipeline.predict_proba(data_test)
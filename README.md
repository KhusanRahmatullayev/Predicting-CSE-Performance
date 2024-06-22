# CSE Student Performance Prediction Model
## Overview
This repository contains a machine learning model designed to predict the academic performance of Computer Science and Engineering (CSE) students. The model is trained on a dataset that includes various attributes related to students' demographics, behaviors, and habits.
## Dataset
The dataset used for this project is CSE_student_performances.csv, which includes 99 entries and 10 features. The features are:

__Age__: The age of the student (integer).
**Gender**: The gender of the student (categorical: "Male" or "Female").
**AcademicPerformance**: The academic performance of the student (categorical: "Average", "Good", "Excellent").
**TakingNoteInClass**: Whether the student takes notes in class (categorical: "Yes", "No", "Sometimes").
**DepressionStatus**: The depression status of the student (categorical: "Yes", "No", "Sometimes").
**FaceChallangesToCompleteAcademicTask**: If the student faces challenges to complete academic tasks (categorical: "Yes", "No", "Sometimes").
**LikePresentation**: If the student likes presentations (categorical: "Yes", "No").
**SleepPerDayHours**: The number of hours the student sleeps per day (integer).
**NumberOfFriend**: The number of friends the student has (float, can be null).
**LikeNewThings**: If the student likes new things (categorical: "Yes", "No").

## Model

The machine learning model used is designed to classify the academic performance of students based on the provided features. The model goes through the following steps:

#### 1. Data Preprocessing:
- Handling missing values.
- Encoding categorical variables.
- Normalizing numerical features.
#### 2. Model Training:
- Splitting the dataset into training and testing sets.
- Training a classification model (Decision Tree, Random Forest).
- Evaluating the model's performance using appropriate metrics (accuracy, precision).

## Getting Started
#### Prerequisites
To run the model, you need to have Python installed along with the following libraries:
- pandas
- numpy
- scikit-learn

You can install the required libraries using pip:
```sh
 pip install pandas numpy scikit-learn 
```
## Running the Model
 #### 1. Clone the repository:
```sh
 git clone https://github.com/https://github.com/KhusanRahmatullayev/Predicting-CSE-Performance
 cd CSE_student_performance_prediction
```
#### 2. Ensure the dataset is in the repository:

The dataset CSE_student_performances.csv should already be included in the repository. Confirm that it is present in the root directory of the project.

#### 3. Run the model training script:
```sh
python psychosocial_dimensions_of_student_life.py
```
This script will preprocess the data, train the model, and evaluate its performance

## Results
The model's performance will be displayed in the console output, showing metrics such as accuracy, precision, and recall. You can further tune the model and improve its performance by experimenting with different algorithms and hyperparameters.

## Contributing
If you wish to contribute to this project, please fork the repository and submit a pull request. For major changes, please open an issue to discuss what you would like to change.

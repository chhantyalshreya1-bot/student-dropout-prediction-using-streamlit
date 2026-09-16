# Student Dropout Prediction

This project predicts whether a student is likely to drop out based on academic, personal, and other student-related factors using machine learning.

The project includes data preprocessing, exploratory data analysis (EDA), feature selection, model training, evaluation, hyperparameter tuning, and deployment using Streamlit.

## Dataset

The dataset used in this project is the **Student Dropout Prediction Dataset** from Kaggle.

Dataset Link: https://www.kaggle.com/datasets/meharshanali/student-dropout-prediction-dataset/data

## Project Workflow

The project follows these main steps:

1. Data Loading and Exploration
2. Data Cleaning and Preprocessing
3. Exploratory Data Analysis (EDA)
4. Feature Selection
5. Train-Test Split
6. Feature Scaling
7. Model Training
8. Model Evaluation
9. Cross-Validation and Hyperparameter Tuning
10. Model Selection
11. Streamlit Deployment

## Data Preprocessing

- Filled missing numerical values using median and categorical values using mode.
- Removed duplicate rows and irrelevant coloumn.
- Applied ordinal encoding and one-hot encoding to categorical features.
- Standardized features using StandardScaler.
- Identified potential outliers using the IQR method and retained valid observations.

## Exploratory Data Analysis

EDA was performed to understand the data and identify important patterns.

- Examined the distribution of the target variable.
- Analyzed student age distribution.
- Compared attendance, GPA, and study hours across dropout groups.
- Analyzed dropout rates across departments.
- Used a correlation heatmap to identify relationships between numerical features.

## Models and Evaluation

The following machine learning models were trained and compared:

- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost

Cross-validation and GridSearchCV were used for model evaluation and hyperparameter tuning.

Logistic Regression was selected as the final model because it achieved the highest recall for identifying students who are likely to drop out.


## Streamlit Deployment

- The final trained model was saved using Pickle and deployed as an interactive Streamlit web application.

- The application allows users to enter student information and receive a dropout prediction along with the predicted probability.

## How to Run

### 1. Download or clone this repository

Download the project from GitHub or clone it using Git.

**GitHub Repository:** [https://github.com/chhantyalshreya1-bot/student-dropout-prediction-using-streamlit]

### 2. Open the project folder in VS Code

Open the terminal inside the project folder.

### 3. Install the required libraries

```bash
pip install -r requirements.txt

### 4. Run the streamit application 
streamlit run app.py




## Project Structure

- app.py - Streamlit application
- student_dropout_prediction.ipynb - Jupyter Notebook containing data analysis and model development
- student_dropout_dataset_v3.csv - Dataset used for the project
- model.pkl - Trained machine learning model
- scaler.pkl - Saved feature scaler
- feature_columns.pkl - Feature columns used by the model
- requirements.txt - Required Python libraries
- README.md - Project documentation
- .gitignore - Files ignored by Git

## Results

The final model used in this project is Logistic Regression.

- Accuracy: 74.5%
- Recall for dropout students: 77%
- F1-score for dropout students: 59%

Logistic Regression was selected because identifying students who may drop out was the main focus of the project.
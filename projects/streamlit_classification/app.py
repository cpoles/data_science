# streamlit run app.py
# Streamlit application for ML Classification
# Uses sklearn original datasets

# Import libraries
import time
import numpy as np
import pandas as pd
import pandas_profiling
import streamlit as st
import sklearn.metrics
import sklearn.datasets
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from streamlit_pandas_profiling import st_profile_report

# Title bar
st.title(f"ML Classification with Logistic Regression")

# Side bar
st.sidebar.subheader("**Select a dataset**")
# Dataset selection
dataset = st.sidebar.selectbox('Dataset', ['Iris 💮', 'Wine 🍷', 'Breast Cancer 🎗️'])
# Train/Test ratio
test_size = st.sidebar.slider('Select size of Test set (Default: 0.70/0.30)', 0.2, 0.9, 0.7)
# Hyperparameters
st.sidebar.subheader("**Hyperparameters Configuration**")
# Solver
solver = st.sidebar.selectbox('Algorithm', ['lbfgs', 'sag', 'newton-cg', 'liblinear'])
# Regularization
penalty = st.sidebar.radio('Regularization:', ['l1', 'l2', 'elasticnet'])
# Tolerance
tol = st.sidebar.text_input('Tolerance for stopping criteria (default = 1e-4):', '1e-4')
# Max Iterations
max_iter = st.sidebar.text_input('Number of iterations: (default = 50)', '50')

# Parameters
params = {'penalty': penalty, 'tol': float(tol), 'max_iter': int(max_iter), 'solver': solver}


# --- HELPER FUNCTIONS --- #
@st.cache_data
def load_data(dataset):
    '''
        Loads a sklearn dataset

        :param str dataset: The name of the dataset to be loaded

        :return: sklearn dataset
    '''
    if dataset == 'Iris':
        data = sklearn.datasets.load_iris()
    elif dataset == 'Wine':
        data = sklearn.datasets.load_wine()
    else:
        data = sklearn.datasets.load_breast_cancer()

    return data

def data_preprocess(dataset, test_size):
    '''
        Preprocesses the dataset for training

        :param np.array dataset: The whole dataset
        :param float test_size

        :return: tuple with train and test data
    '''
    # Split dataset into train and test
    X_train, X_test, y_train, y_test = train_test_split(dataset.data, dataset.target, test_size=float(test_size), random_state=42)

    # Standardize data
    scaler = MinMaxScaler()

    # Fit and transform train data
    X_train = scaler.fit_transform(X_train)
    
    # Transform test data
    X_test = scaler.transform(X_test)

    return X_train, X_test, y_train, y_test

def create_model(params, train_data):
    '''
        Returns a trained Logistic Regression model

        @params
        :param dict params: Dictionary of hyperparameters
        :param tuple train_data: The training data (X_train, y_train)
    '''

    # Load train data
    X_train, y_train = train_data

    # Create LR Clf Model
    clf = LogisticRegression(solver=params['solver'],
                             max_iter=params['max_iter'],
                             penalty=params['penalty'],
                             tol=params['tol']) 
    
    # Fit the Model
    clf.fit(X_train, y_train)

    return clf

def create_profile_report(dataset):
    '''
        Create a profile report of a given dataset

        :param np.array dataset: The dataset to be profiled
    '''
    # concatenate target and features
    data = np.hstack([dataset.data, dataset.target.reshape(dataset.data.shape[0], -1)])
    # create dataframe
    df = pd.DataFrame(data=data, columns=dataset.feature_names+['target'])
    # create profile report
    pr = df.profile_report()
    return pr, df


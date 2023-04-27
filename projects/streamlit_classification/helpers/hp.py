import streamlit as st
import numpy as np
import pandas as pd
import sklearn.datasets
from ydata_profiling import ProfileReport
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score



# --- HELPER FUNCTIONS --- #
@st.cache_data
def load_data(dataset):
    '''
        Loads a sklearn dataset

        :param str dataset: The name of the dataset to be loaded

        :return: sklearn dataset
    '''
    if dataset == 'Iris 💮':
        data = sklearn.datasets.load_iris()
    elif dataset == 'Wine 🍷':
        data = sklearn.datasets.load_wine()
    else:
        data = sklearn.datasets.load_breast_cancer()

    return data

@st.cache_data
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

        :param dict params: Dictionary of hyperparameters
        :param tuple train_data: The training data (X_train, y_train)

        :return  Trained LR model
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

@st.cache_data
def create_profile_report(dataset):
    '''
        Create a profile report of a given dataset

        :param np.array dataset: The dataset to be profiled

        :return profile report of dataset
    '''
    # concatenate target and features
    data = np.column_stack([dataset.data, dataset.target])
    # create dataframe
    df = pd.DataFrame(data=data, columns=list(dataset.feature_names)+['target'])
    # create profile report
    pr = ProfileReport(df)
    return pr, df

def get_model_metrics(model, test_set):
    '''
        Returns model predictions, confusion matrix and accuracy

        :params model: sklearn LR model
        :params sklearn.linear_model._logistic.LogisticRegression
    
        :params np.array test_set: The dataset used for predictions

        :return dict predictions, accuracy, confusion matrix
    '''
    # Unpack test set
    X_test, y_test = test_set
    # Predictions
    predictions = model.predict(X_test)
    # Accuracy
    accuracy = accuracy_score(y_test, predictions)
    # Confusion Matrix
    c_matrix = confusion_matrix(y_test, predictions)

    return predictions, accuracy, c_matrix
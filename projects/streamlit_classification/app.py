# streamlit run app.py
# Streamlit application for ML Classification
# Uses sklearn original datasets

# Import libraries
import time
import numpy as np
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
from helpers import hp
import ydata_profiling
from streamlit_pandas_profiling import st_profile_report

# Title bar
st.title(f"ML Classification with Logistic Regression")

# --- SIDEBAR --- #
st.sidebar.subheader("**Select a dataset**")
# Dataset selection
dataset = st.sidebar.selectbox('Dataset', ['Iris 💮', 'Wine 🍷', 'Breast Cancer 🎗️'])
# Generate Profile report
eda = st.sidebar.button('Profile Report')
# Train/Test ratio
test_size = st.sidebar.slider('Test Size', 0.2, 0.9, 0.3)
# Hyperparameters
st.sidebar.subheader("**Hyperparameters Configuration**")
# Solver
solver = st.sidebar.selectbox('Algorithm', ['liblinear', 'saga', 'newton-cg', 'lbfgs'])
# Regularization
penalty = st.sidebar.radio('Regularization:', ['l1', 'l2', 'elasticnet'])
# Tolerance
tol = st.sidebar.text_input('Tolerance for stopping criteria (default = 1e-4):', '1e-4')
# Max Iterations
max_iter = st.sidebar.text_input('Number of iterations: (default = 50)', '50')
# --- Train Button --- #
train_button = st.sidebar.button('Train model')

# Parameters
params = {'penalty': penalty, 'tol': float(tol), 'max_iter': int(max_iter), 'solver': solver}


# --- Model Info --- #
# Load data
data = hp.load_data(dataset)
st.subheader(f'Dataset {dataset}')

X_train, X_test, y_train, y_test = hp.data_preprocess(data, test_size)

# -- Profile Report --- #
if eda:
    # profile report
    with st.spinner('Creating profile report'):
        pr, df = hp.create_profile_report(data)

    components.html(pr.html, height=1000)

# --- Model Training --- #
if train_button:
    # Create Model
    with st.spinner('Training model'):
        time.sleep(5)
        model = hp.create_model(params, (X_train, y_train))
        st.success('Model trained.')

    # Model output and metrics
    metrics = hp.get_model_metrics(model, (X_test, y_test))

    c1, c2, c3, c4 = st.columns(4)
    
    c1.metric('Accuracy', round(metrics['accuracy'], 2))   
    c2.metric('Precision', round(metrics['precision'], 2))
    c3.metric('Recall', round(metrics['recall'], 2))
    c4.metric('F1 Score:', round(metrics['f1_score']))
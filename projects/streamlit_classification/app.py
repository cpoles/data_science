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

# suppress message
st.set_option('deprecation.showPyplotGlobalUse', False)

# --- SIDEBAR --- #
st.sidebar.subheader("**Select a dataset**")
# Dataset selection
dataset = st.sidebar.selectbox('Dataset', ['Iris 💮', 'Wine 🍷', 'Breast Cancer 🎗️'])
# Generate Profile report
eda = st.sidebar.button('Profile Report')
# Display Dataset
display_df = st.sidebar.checkbox('Display Dataset')

# --- ML MODELS SELECTION --- #
sel_model = st.sidebar.selectbox('Model', ['Logistic Regression', 'Support Vector Machine'])

# Hyperparameters
st.sidebar.subheader("**Hyperparameters Configuration**")
# Train/Test ratio
test_size = st.sidebar.slider('Test Size', 0.2, 0.9, 0.3)

# --- Logistic Regression --- #
if sel_model == 'Logistic Regression':
    solver = st.sidebar.selectbox('Algorithm', ['liblinear', 'sag', 'newton-cg', 'lbfgs'])
    penalty = st.sidebar.radio('Regularization:', ['l1', 'l2', 'none'])
    tol = st.sidebar.text_input('Tolerance for stopping criteria (default = 1e-4):', '1e-4')
    max_iter = st.sidebar.text_input('Number of iterations: (default = 50)', '50')

    # Validate algorithm and penalty
    algo_pen = {
        'liblinear': ['l1', 'l2'],
        'sag': ['l2', 'none'], 
        'newton-cg': ['l2', 'none'], 
        'lbfgs': ['l2', 'none']
    }

    if penalty not in algo_pen[solver]:
        pens = ', '.join(algo_pen[solver])
        st.error(f'''The **{solver}** algorithm only supports **{pens}** penalties.''')
        train_button = st.sidebar.button('Train model', disabled=True)
    else:
        # Parameters
        params = {'penalty': penalty, 'tol': float(tol), 'max_iter': int(max_iter), 'solver': solver}
         # --- Train Button --- #
        train_button = st.sidebar.button('Train model')

# -- Support Vector Machine -- #
if sel_model == 'Support Vector Machine':
    C = st.sidebar.number_input("C (Regularization parameter)", 0.01, 10.0, step=0.01, key="C")
    kernel = st.sidebar.radio("Kernel", ("rbf", "linear"), key="kernel") 
    gamma = st.sidebar.radio("Gamma (Kernal coefficient)", ("scale", "auto"), key="gamma")
    # Parameters
    params = {'C': C, 'kernel': kernel, 'gamma': gamma}
    train_button = st.sidebar.button('Train model')

# --- Model Info --- #
# Load data
data, df, labels = hp.load_data(dataset)

st.subheader(f'Dataset {dataset}')
# Split data into Train and Test sets
X_train, X_test, y_train, y_test = hp.data_preprocess(data, test_size)

# -- Profile Report --- #
if eda:
    # profile report
    with st.spinner('Creating profile report'):
        time.sleep(5)
        pr = hp.create_profile_report(df)
        st.success('Profile report created.')

    components.html(pr.html, height=1000, scrolling=True)

# -- Display Dataset -- #
if display_df:
    st.write(df)


# --- Model Training --- #
if train_button:
    # -- Metrics -- #
    st.header(f'{sel_model} results')
    # Create Model
    with st.spinner('Training model'):
        time.sleep(5)
        model = hp.create_model(sel_model, params, (X_train, y_train))
        st.success('Model trained.')

    # Model output and metrics
    metrics = hp.get_model_metrics(model, (X_test, y_test))

    c1, c2, c3, c4 = st.columns(4)
    
    c1.metric('Accuracy', metrics['accuracy'].round(2))   
    c2.metric('Precision', metrics['precision'].round(2))
    c3.metric('Recall', metrics['recall'].round(2))
    c4.metric('F1 Score:', metrics['f1_score'].round(2))

    # -- Plot Confusion Matrix for Multiclass and ROC for Binary Class -- #
    cm = hp.plot_metrics(model, (X_test, y_test), labels)
    st.pyplot()
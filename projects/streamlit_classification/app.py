# streamlit run app.py
# Streamlit application for ML Classification
# Uses sklearn original datasets

# Import libraries
import time
import numpy as np
import pandas as pd
import streamlit as st
from helpers import hp

# Title bar
st.title(f"ML Classification with Logistic Regression")

# --- SIDEBAR --- #
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




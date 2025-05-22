import streamlit as st
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

st.set_page_config(page_title="Model Performance")
st.title("Model Performance")
st.header("Model Performance")


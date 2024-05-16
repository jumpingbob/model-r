import streamlit as st
import pandas as pd
from pycaret.regression import *
import os

st.title("ああ")
uploaded_file = st.file_uploader("pklファイルをアップロードしてください。", type=['pkl'])

if uploaded_file is not None:
    with open(os.path.join("temp_model.pkl"), "wb") as f:
        f.write(uploaded_file.getvalue())
    model = load_model("temp_model.pkl")
    feature_importance = model.feature_importances_
    df_feature_importance = pd.DataFrame({'Feature': model.feature_names_, 'Importance': feature_importance})
    st.write(df_feature_importance)

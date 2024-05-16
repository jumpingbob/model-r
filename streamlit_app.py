import streamlit as st
import pandas as pd
from pycaret.classification import load_model

st.title("ああ")
uploaded_file = st.file_uploader("pklファイルをアップロードしてください。", type=['pkl'])

model = load_model(uploaded_file)
feature_importance = model.feature_importances_
df_feature_importance = pd.DataFrame({'Feature': model.feature_names_, 'Importance': feature_importance})
st.write(df_feature_importance)
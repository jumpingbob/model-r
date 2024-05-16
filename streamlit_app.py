 import streamlit as st
import pandas as pd
import pickle

# Streamlitアプリのタイトル
st.title("Pickleファイルの読み込みと表示")

# ファイルアップローダーを作成
uploaded_file = st.file_uploader("Pickleファイルを選択してください", type="pkl")

if uploaded_file is not None:
    # ファイルをバイナリモードで読み込み
    data = pickle.load(uploaded_file)
    
    # データがPandas DataFrameの場合は表示
    if isinstance(data, pd.DataFrame):
        st.write("データフレームの内容:")
        st.dataframe(data)
    else:
        st.write("読み込まれたデータ:")
        st.write(data)

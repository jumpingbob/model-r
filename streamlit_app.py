import streamlit as st
import pickle

# Streamlitアプリのタイトル
st.title("Pickleファイルの読み込みと表示")

# ファイルアップローダーを作成
uploaded_file = st.file_uploader("Pickleファイルを選択してください", type="pkl")

if uploaded_file is not None:
    try:
        # バイナリモードでファイルを読み込み
        data = pickle.load(uploaded_file)

        # データの型に応じて表示
        if isinstance(data, dict):
            st.write("辞書型データ:")
            for key, value in data.items():
                st.write(f"{key}: {value}")
        elif isinstance(data, list):
            st.write("リスト型データ:")
            for item in data:
                st.write(item)
        else:
            st.write("読み込まれたデータ:")
            st.write(data)
    except Exception as e:
        st.error(f"ファイルの読み込みに失敗しました: {e}")

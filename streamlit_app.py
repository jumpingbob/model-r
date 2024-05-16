import streamlit as st
import pandas as pd
import pickle

# モデルの.pklファイルのパス
model_path = "your_model.pkl"

# .pklファイルからモデルをロード
with open(model_path, 'rb') as f:
    model = pickle.load(f)

# モデルの説明変数を定義（ここでは例として、特徴の名前とそれに対応するデフォルトの値の辞書を使用）
features = {
    'Feature1': st.sidebar.number_input("Feature1", value=0.0),
    'Feature2': st.sidebar.number_input("Feature2", value=0.0),
    # 追加の特徴があればここに追加
}

# 特徴をデータフレームに変換
input_data = pd.DataFrame([features])

# モデルを使用して予測を行う
prediction = model.predict(input_data)

# 結果を表示
st.write('Prediction:', prediction)

import streamlit as st
from pycaret.classification import load_model, predict_model
import pandas as pd

# タイトルと説明の設定
st.title('PyCaretモデルによる予測アプリ')
st.write('このアプリは、PyCaretでトレーニングしたモデルを使って予測を行います。')

# サイドバーにユーザー入力フォームを作成
st.sidebar.header('入力パラメータ')

def user_input_features():
    feature1 = st.sidebar.number_input('Feature 1', min_value=0.0, max_value=100.0, value=50.0)
    feature2 = st.sidebar.number_input('Feature 2', min_value=0.0, max_value=100.0, value=50.0)
    feature3 = st.sidebar.number_input('Feature 3', min_value=0.0, max_value=100.0, value=50.0)
    feature4 = st.sidebar.number_input('Feature 4', min_value=0.0, max_value=100.0, value=50.0)
    
    data = {'Feature 1': feature1,
            'Feature 2': feature2,
            'Feature 3': feature3,
            'Feature 4': feature4}
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

# モデルの読み込み
model = load_model('your_model_name')  # 'your_model_name'を実際のモデル名に置き換えてください

# 予測の実行
prediction = predict_model(model, data=input_df)

# 結果の表示
st.subheader('入力パラメータ')
st.write(input_df)

st.subheader('予測結果')
st.write(prediction)

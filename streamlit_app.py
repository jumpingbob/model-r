import streamlit as st
import pandas as pd
from pycaret.regression import load_model, get_config
import tempfile
# Streamlitアプリケーションの設定
st.title('回帰モデルの特徴量重要度')

# 一時ファイルからモデルを読み込む
path = 'test_model'
model = load_model(path)
# 特徴量重要度を取得
feature_importances = model.feature_importances_
# 特徴量名を取得
feature_names = get_config('X').columns
# 特徴量重要度をデータフレームに変換
importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': feature_importances})
importance_df = importance_df.sort_values(by='Importance', ascending=False)
# 特徴量重要度を表示
st.write('特徴量重要度:')
st.dataframe(importance_df)
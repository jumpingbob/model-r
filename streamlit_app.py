import streamlit as st
import numpy as np
import plotly.express as px

# ユーザーからの入力を受け取り、それぞれの項目の値をリストに格納する
def get_user_input(features):
    user_input = []
    options = ["5.とても高い", "4.やや高い", "3.ふつう", "2.やや低い", "1.とても低い"]
    for feature in features:
        user_input.append(int(st.radio(f"**{feature}**の高さを選択してください", options=options, index=2, key=feature)[0]))  # 文字列の最初の文字を数値に変換
    return user_input

# 逆スコアリングを適用する
def reverse_scoring(user_input, reverse_indices):
    for i in reverse_indices:
        user_input[i] = 6 - user_input[i]  # 1から5の範囲なので、6 - current_valueで逆にする
    return user_input

# Zスコアの計算
def z_score_scaling(user_input):
    mean_val = np.mean(user_input)
    std_val = np.std(user_input)
    if std_val == 0:
        # 標準偏差が0の場合、すべてのZスコアを0に設定
        z_scores = [0 for _ in user_input]
    else:
        z_scores = [(x - mean_val) / std_val for x in user_input]
    return z_scores

# ストレスレベルを計算（要素とは独立に計算）
def calculate_stress_level(z_scores):
    # ストレスレベルはZスコアの合計（絶対値）で計算
    stress_level = np.sum(np.abs(z_scores))
    return stress_level

# 最も高い項目を特定する
def find_top_highest_features(scaled_values, features, top_n=3):
    sorted_indices = np.argsort(scaled_values)[-top_n:][::-1]
    highest_features = [(features[i], scaled_values[i]) for i in sorted_indices]
    return highest_features

# Streamlitアプリの実行
def main():
    st.title("メンタルヘルスセルフチェッカー")

    # セッション状態を初期化
    if 'user_inputs' not in st.session_state:
        st.session_state.user_inputs = []

    st.write("以下のラジオボタンで各項目を評価し、ストレスレベルおよびストレス要因を推定します。")
    st.markdown("直感的にあてはまる各項目の強さを選択してください。")

    # データを収集した際の質問項目
    features = [
        "anxiety level (不安レベル)",
        "self-esteem (自尊心の高さ)",
        "depression (うつ傾向)",
        "headache (頭痛の強度)",
        "sleep quality (睡眠の質)",
        "breathing problem (呼吸の苦しさ・息苦しさ)",
        "noise level (騒音レベル)",
        "living conditions (生活環境・状態)",
        "safety (安全性)",
        "basic needs (基本的欲求)",
        "academic performance (学業成績)",
        "study load (学業負担)",
        "teacher-student relationship (教師と生徒の関係)",
        "future career concerns (将来のキャリア・進路に関する懸念)",
        "peer pressure (仲間からのプレッシャー)",
        "extracurricular activities (課外活動における負担)",
        "bullying (外部からの圧力的な被害)"
    ]

    user_input = get_user_input(features)

    st.session_state.user_inputs = user_input  # 入力データをセッション状態に保存

    st.write("入力された値:", st.session_state.user_inputs)

    # 逆スコアリングを適用するインデックス
    reverse_indices = [1, 4, 7, 8, 9, 10, 12]  # 1: self-esteem, 4: sleep quality, 7: living conditions, 8: safety, 9: basic needs, 10: academic performance, 12: teacher-student relationship
    user_input = reverse_scoring(st.session_state.user_inputs, reverse_indices)

    st.write("Values after applying reverse scoring:", user_input)

    z_scores = z_score_scaling(user_input)

    st.write("Z-scores:", z_scores)

    stress_level = calculate_stress_level(z_scores)

    stress_level_rounded = round(stress_level, 2)  # 小数第二位まで四捨五入

    st.write("ストレスレベル:", stress_level_rounded)

    highest_features = find_top_highest_features(z_scores, features, top_n=3)
    st.write("ストレス要因上位3項目:")
    for feature, value in highest_features:
        st.write(f"{feature}: {value}")

    st.write("以下は、ユーザーのストレス要因をレーダーチャートで視覚化したものです。")
    fig = px.line_polar(
        r=z_scores + z_scores[:1],  # 周期的に閉じるために、最初の値を最後に追加
        theta=features + features[:1],  # 周期的に閉じるために、最初の項目を最後に追加
        line_close=True,
        title="ストレス要因",
    )
    st.plotly_chart(fig)

if __name__ == "__main__":
    main()

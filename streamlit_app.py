import streamlit as st
import numpy as np
import plotly.express as px

# 翻訳辞書を定義
translations = {
    "日本語": {
        "title": "メンタルヘルス推定アプリ",
        "intro": "以下のラジオボタンで各項目を評価し、ストレスレベルを計算します。",
        "select_language": "使用言語を選択してください",
        "input_values": "入力された値:",
        "reversed_values": "逆スコアリング適用後の値:",
        "scaled_values": "Min-Max正規化された値:",
        "stress_level": "ストレスレベル:",
        "highest_features": "最もストレスが高い要素:",
        "chart_title": "ストレス要素"
    },
    "English": {
        "title": "Mental Health Estimation App",
        "intro": "Evaluate each item using the radio buttons below and calculate the stress level.",
        "select_language": "Select language",
        "input_values": "Input values:",
        "reversed_values": "Values after reverse scoring:",
        "scaled_values": "Min-Max scaled values:",
        "stress_level": "Stress level:",
        "highest_features": "Top stress factors:",
        "chart_title": "Stress Factors"
    }
}

# ユーザーからの入力を受け取り、それぞれの項目の値をリストに格納する
def get_user_input(features, lang):
    user_input = []
    for feature in features:
        user_input.append(st.radio(f"{feature}を選択してください" if lang == "日本語" else f"Select {feature}", options=[1, 2, 3, 4, 5], index=2))
    return user_input

# 逆スコアリングを適用する
def reverse_scoring(user_input, reverse_indices):
    for i in reverse_indices:
        user_input[i] = 6 - user_input[i]  # 1から5の範囲なので、6 - current_valueで逆にする
    return user_input

# Min-Max正規化
def min_max_scaling(user_input):
    min_val = np.min(user_input)
    max_val = np.max(user_input)
    st.write(f"min_val: {min_val}, max_val: {max_val}")  # デバッグ出力
    if min_val == max_val:
        # すべての値が同じ場合、すべてのスケーリング値を0.5に設定
        scaled_values = [0.5 for _ in user_input]
    else:
        scaled_values = [(x - min_val) / (max_val - min_val) for x in user_input]
    st.write(f"scaled_values: {scaled_values}")  # デバッグ出力
    return scaled_values

# ストレスレベルを計算
def calculate_stress_level(scaled_values, feature_importances):
    stress_level = np.dot(scaled_values, feature_importances)
    st.write(f"stress_level: {stress_level}")  # デバッグ出力
    return stress_level

# 最も高い項目を特定する
def find_top_highest_features(scaled_values, features, top_n=3):
    sorted_indices = np.argsort(scaled_values)[-top_n:][::-1]
    highest_features = [(features[i], scaled_values[i]) for i in sorted_indices]
    return highest_features

# Streamlitアプリの実行
def main():
    # 使用言語を選択する
    lang = st.selectbox("使用言語を選択してください", ["日本語", "English"])

    # 言語に応じた翻訳を取得
    t = translations[lang]

    st.title(t["title"])

    # データを収集した際の質問項目
    features = [
        "anxiety_level (不安レベル)" if lang == "日本語" else "Anxiety Level",
        "self_esteem (自尊心)" if lang == "日本語" else "Self Esteem",
        "mental_health_history (精神保健の歴史)" if lang == "日本語" else "Mental Health History",
        "depression (うつ病)" if lang == "日本語" else "Depression",
        "headache (頭痛)" if lang == "日本語" else "Headache",
        "blood_pressure (血圧)" if lang == "日本語" else "Blood Pressure",
        "breathing_problem (呼吸問題)" if lang == "日本語" else "Breathing Problem",
        "noise_level (騒音レベル)" if lang == "日本語" else "Noise Level",
        "study_load (学業負担)" if lang == "日本語" else "Study Load",
        "future_career_concerns (将来のキャリアに関する懸念)" if lang == "日本語" else "Future Career Concerns",
        "social_support (社会的支援)" if lang == "日本語" else "Social Support",
        "peer_pressure (仲間からのプレッシャー)" if lang == "日本語" else "Peer Pressure",
        "extracurricular_activities (課外活動)" if lang == "日本語" else "Extracurricular Activities",
        "bullying (いじめ)" if lang == "日本語" else "Bullying"
    ]

    # 各質問項目の特徴量重要度
    feature_importances = np.array([
        0.050119,  # anxiety_level
        0.078640,  # self_esteem
        0.089115,  # mental_health_history
        0.062141,  # depression
        0.092308,  # headache
        0.088636,  # blood_pressure
        0.023618,  # breathing_problem
        0.056271,  # noise_level
        0.050188,  # study_load
        0.085528,  # future_career_concerns
        0.102331,  # social_support
        0.050649,  # peer_pressure
        0.079034,  # extracurricular_activities
        0.091422   # bullying
    ])

    st.write(t["intro"])

    user_input = get_user_input(features, lang)

    st.write(t["input_values"], user_input)

    # 逆スコアリングを適用するインデックス
    reverse_indices = [1, 12]  # 1: self_esteem, 12: extracurricular_activities
    user_input = reverse_scoring(user_input, reverse_indices)

    st.write(t["reversed_values"], user_input)

    scaled_values = min_max_scaling(user_input)

    st.write(t["scaled_values"], scaled_values)

    stress_level = calculate_stress_level(scaled_values, feature_importances)

    st.write(t["stress_level"], stress_level)

    highest_features = find_top_highest_features(scaled_values, features, top_n=3)
    st.write(t["highest_features"])
    for feature, value in highest_features:
        st.write(f"{feature}: {value}")

    st.write(t["chart_title"])
    fig = px.line_polar(
        r=scaled_values + scaled_values[:1],  # 周期的に閉じるために、最初の値を最後に追加
        theta=features + features[:1],  # 周期的に閉じるために、最初の項目を最後に追加
        line_close=True,
        title=t["chart_title"],
    )
    st.plotly_chart(fig)

if __name__ == "__main__":
    main()

import streamlit as st
import sympy as sp
import random

st.title("積分問題ジェネレーター")

# xをシンボルとして定義
x = sp.symbols('x')

# 問題を生成する関数
def generate_problem():
    # 基本的な関数
    basic_functions = [
        sp.sin(x), sp.cos(x), sp.tan(x),
        sp.exp(x), sp.log(x), sp.sqrt(x),
        x, x**2, x**3
    ]

    # 複合関数
    composite_functions = [
        sp.sin(x) * sp.exp(x),
        x * sp.log(x),
        sp.sqrt(x**2 + 1),
        x**2 / (x - 1),
        sp.exp(x) / (sp.exp(x) - 1),
        1 / (x**2 + x),
        sp.sin(x)**2,
        sp.cos(x)**3,
        sp.cos(3*x) * sp.cos(x),
        x * sp.exp(-x**2),
        (x**2 + 1)**2 / x**3,
        sp.cos(x) - sp.sin(x),
        (sp.cos(x) - 1) * (sp.cos(x)**2 + sp.cos(x) + 1) / sp.cos(x)**2,
        2*x + sp.exp(x),
        sp.sqrt(2*x - 3),
        x**2 / (x - 2)**2,
        x * sp.sqrt(x + 2),
        sp.exp(x) / (sp.exp(x) - 3)**2,
        sp.cos(x)**2 * sp.sin(x),
        3*x**2 / sp.sqrt(x**3 + 2),
        sp.sin(x) / x,
        sp.exp(x**2),
        sp.sqrt(1 - x**2),
        x**3 * sp.exp(-x**2),
        sp.log(x) / x,
        sp.sin(x)**3 * sp.cos(x),
        1 / sp.sqrt(1 - x**2),
        sp.tan(x),
    ]

    # 無作為に基本的な関数や複合関数を選択
    basic_prob = random.choice(basic_functions)
    composite_prob = random.choice(composite_functions)

    # 確率で基本関数と複合関数を選択
    if random.random() < 0.5:
        problem = basic_prob
    else:
        problem = composite_prob
    
    return problem

# セッション状態の初期化
if 'problem' not in st.session_state:
    st.session_state['problem'] = None
if 'solution' not in st.session_state:
    st.session_state['solution'] = None

# 問題を生成
if st.button("問題を生成"):
    st.session_state['problem'] = generate_problem()
    st.session_state['solution'] = None  # 新しい問題を生成する際に解答をリセット

# 問題を表示
if st.session_state['problem'] is not None:
    st.write("### 問題")
    st.latex(r"\int " + sp.latex(st.session_state['problem']) + r" \, dx")
    
    # 解答を計算
    if st.button("解答を表示"):
        st.session_state['solution'] = sp.integrate(st.session_state['problem'], x)

# 解答を表示
if st.session_state['solution'] is not None:
    st.write("### 解答")
    st.latex(sp.latex(st.session_state['solution']) + " + C")

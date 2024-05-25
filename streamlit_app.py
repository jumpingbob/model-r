import streamlit as st
import sympy as sp
import random

st.title("積分問題ジェネレーター")

# xをシンボルとして定義
x = sp.symbols('x')

# 問題を生成する関数
def generate_problem():
    problems = [
        sp.sin(x) * sp.exp(x),  # ∫sin(x)e^x dx
        x * sp.log(x),  # ∫x log(x) dx
        sp.sqrt(x**2 + 1),  # ∫√(x^2 + 1) dx
        x**2 / (x - 1),  # ∫x^2/(x-1) dx
        sp.exp(x) / (sp.exp(x) - 1),  # ∫e^x/(e^x - 1) dx
        1 / (x**2 + x),  # ∫1/(x^2 + x) dx
        sp.sin(x)**2,  # ∫sin^2(x) dx
        sp.cos(x)**3,  # ∫cos^3(x) dx
        sp.cos(3*x) * sp.cos(x),  # ∫cos(3x)cos(x) dx
        x * sp.exp(-x**2),  # ∫x e^(-x^2) dx
        (x**2 + 1)**2 / x**3,  # ∫(x^2 + 1)^2 / x^3 dx
        sp.cos(x) - sp.sin(x),  # ∫(cos(x) - sin(x)) dx
        (sp.cos(x) - 1) * (sp.cos(x)**2 + sp.cos(x) + 1) / sp.cos(x)**2,  # ∫(cos(x) - 1)(cos^2(x) + cos(x) + 1) / cos^2(x) dx
        2*x + sp.exp(x),  # ∫(2x + e^x) dx
        sp.sqrt(2*x - 3),  # ∫√(2x - 3) dx
        x**2 / (x - 2)**2,  # ∫x^2 / (x - 2)^2 dx
        x * sp.sqrt(x + 2),  # ∫x√(x + 2) dx
        sp.exp(x) / (sp.exp(x) - 3)**2,  # ∫e^x / (e^x - 3)^2 dx
        sp.cos(x)**2 * sp.sin(x),  # ∫cos^2(x)sin(x) dx
        3*x**2 / sp.sqrt(x**3 + 2),  # ∫3x^2 / √(x^3 + 2) dx
        x**3 / (x**2 - 1),  # ∫x^3 / (x^2 - 1) dx
        x / (x**2 + 4*x + 4),  # ∫x / (x^2 + 4x + 4) dx
        (x**3 + 1) / x,  # ∫(x^3 + 1) / x dx
        x * sp.exp(x**2),  # ∫x e^(x^2) dx
        sp.sqrt(x**2 + 4*x + 4),  # ∫√(x^2 + 4x + 4) dx
        x**3 / (x - 3)**2,  # ∫x^3 / (x - 3)^2 dx
        x**2 * sp.sqrt(x + 1),  # ∫x^2√(x + 1) dx
        sp.exp(x) / (sp.exp(x) + 1),  # ∫e^x / (e^x + 1) dx
        sp.sin(x) * sp.cos(2*x),  # ∫sin(x)cos(2x) dx
        sp.sin(2*x) * sp.cos(x),  # ∫sin(2x)cos(x) dx
        sp.cos(x)**3 * sp.sin(x),  # ∫cos^3(x)sin(x) dx
        x**3 / sp.sqrt(x**4 + 4),  # ∫x^3 / √(x^4 + 4) dx
        1 / (x**3 - x),  # ∫1 / (x^3 - x) dx 部分分数分解
        1 / (x**2 + 4*x + 4),  # ∫1 / (x^2 + 4*x + 4) dx 部分分数分解
        sp.sin(x) * sp.cos(x),  # ∫sin(x)cos(x) dx 積和の公式
        sp.sin(x)**2 * sp.cos(x),  # ∫sin^2(x)cos(x) dx 積和の公式
        sp.cos(x)**4 * sp.sin(x),  # ∫cos^4(x)sin(x) dx 積和の公式
    ]
    
    # 問題をランダムに選択
    problem = random.choice(problems)
    
    return problem

# セッション状態の初期化
if 'problem' not in st.session_state:
    st.session_state['problem'] = generate_problem()
if 'solution' not in st.session_state:
    st.session_state['solution'] = None

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

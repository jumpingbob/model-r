import streamlit as st
import sympy as sp
import random

st.title("積分問題ジェネレーター")

# xをシンボルとして定義
x = sp.symbols('x')

# 問題を生成する関数
def generate_problem():
    problems = [
        sp.integrate(sp.sin(x) * sp.exp(x), x),  # ∫sin(x)e^x dx
        sp.integrate(x * sp.log(x), x),  # ∫x log(x) dx
        sp.integrate(sp.sqrt(x**2 + 1), x),  # ∫√(x^2 + 1) dx
        sp.integrate(x**2 / (x - 1), x),  # ∫x^2/(x-1) dx
        sp.integrate(sp.exp(x) / (sp.exp(x) - 1), x),  # ∫e^x/(e^x - 1) dx
        sp.integrate(1 / (x**2 + x), x),  # ∫1/(x^2 + x) dx
        sp.integrate(sp.sin(x)**2, x),  # ∫sin^2(x) dx
        sp.integrate(sp.cos(x)**3, x),  # ∫cos^3(x) dx
        sp.integrate(sp.cos(3*x) * sp.cos(x), x),  # ∫cos(3x)cos(x) dx
        sp.integrate(x * sp.exp(-x**2), x),  # ∫x e^(-x^2) dx
    ]
    
    # 問題をランダムに選択
    problem = random.choice(problems)
    
    return problem

# 問題を取得
problem = generate_problem()

# 問題を表示
st.write("### 問題")
st.latex(r"\int " + sp.latex(problem) + r" \, dx")

# 解答を計算
solution = sp.integrate(problem, x)

# 解答を表示
st.write("### 解答")
st.latex(sp.latex(solution) + " + C")

# ボタンを押すと新しい問題を生成
if st.button("新しい問題を生成"):
    problem = generate_problem()
    st.experimental_rerun()
additional_problems = [
    sp.integrate((x**2 + 1)**2 / x**3, x),  # ∫(x^2 + 1)^2 / x^3 dx
    sp.integrate(sp.cos(x) - sp.sin(x), x),  # ∫(cos(x) - sin(x)) dx
    sp.integrate((sp.cos(x) - 1) * (sp.cos(x)**2 + sp.cos(x) + 1) / sp.cos(x)**2, x),  # ∫(cos(x) - 1)(cos^2(x) + cos(x) + 1) / cos^2(x) dx
    sp.integrate(2*x + sp.exp(x), x),  # ∫(2x + e^x) dx
    sp.integrate(sp.sqrt(2*x - 3), x),  # ∫√(2x - 3) dx
    sp.integrate(x**2 / (x - 2)**2, x),  # ∫x^2 / (x - 2)^2 dx
    sp.integrate(x * sp.sqrt(x + 2), x),  # ∫x√(x + 2) dx
    sp.integrate(sp.exp(x) / (sp.exp(x) - 3)**2, x),  # ∫e^x / (e^x - 3)^2 dx
    sp.integrate(sp.cos(x)**2 * sp.sin(x), x),  # ∫cos^2(x)sin(x) dx
    sp.integrate(3*x**2 / sp.sqrt(x**3 + 2), x),  # ∫3x^2 / √(x^3 + 2) dx
]

problems.extend(additional_problems)

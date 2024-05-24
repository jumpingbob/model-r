import streamlit as st
import sympy as sp
import random

# 関数リストを定義します
functions = [
    'x', 'x**2', 'x**3', 'sp.sin(x)', 'sp.cos(x)', 'sp.exp(x)', '1/x', 'sp.log(x)'
]

# 積分問題をランダムに生成する関数
def generate_problem():
    func_str = random.choice(functions)
    func = eval(func_str)
    return func_str, func

# 解答を表示する関数
def solve_integral(func):
    x = sp.symbols('x')
    integral = sp.integrate(func, x)
    return integral

st.title("積分問題生成器")

# 問題を生成
if st.button("問題を生成"):
    func_str, func = generate_problem()
    st.write(f"次の関数の不定積分を求めよ：$${sp.latex(func)}$$")
    
    # 解答を表示
    if st.button("解答を表示"):
        integral = solve_integral(func)
        st.write(f"解答：$${sp.latex(integral)}$$")

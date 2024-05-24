import streamlit as st
import sympy as sp
import random

# シンボルを定義
x = sp.symbols('x')

# 関数リストを定義します
functions = [
    'x', 'x**2', 'x**3', 'sp.sin(x)', 'sp.cos(x)', 'sp.exp(x)', '1/x', 'sp.log(x)',
    'x*sp.exp(x)', 'x*sp.sin(x)', 'x*sp.cos(x)', 'sp.exp(x**2)', 'sp.sin(x)*sp.cos(x)', 
    'sp.exp(x)*sp.sin(x)', 'sp.exp(x)*sp.cos(x)', 'sp.sin(x)**2', 'sp.cos(x)**2', 
    'sp.tan(x)', 'sp.cot(x)', '1/(x**2 + 1)', '1/(x**2 + 4)', '1/(x**2 + x + 1)', 
    'x/(x**2 + 1)', 'sp.exp(-x**2)', 'sp.exp(-x**2) * sp.cos(x)', 'sp.exp(-x**2) * sp.sin(x)'
]

# 積分問題をランダムに生成する関数
def generate_problem():
    func_str = random.choice(functions)
    func = eval(func_str)
    return func_str, func

# 解答を表示する関数
def solve_integral(func):
    integral = sp.integrate(func, x)
    return integral

st.title("積分問題生成器")

# セッション状態の初期化
if 'func_str' not in st.session_state:
    st.session_state['func_str'] = None
if 'func' not in st.session_state:
    st.session_state['func'] = None
if 'integral' not in st.session_state:
    st.session_state['integral'] = None

# 問題を生成
if st.button("問題を生成"):
    st.session_state['func_str'], st.session_state['func'] = generate_problem()
    st.session_state['integral'] = solve_integral(st.session_state['func'])

# 問題を表示
if st.session_state['func_str']:
    st.write(f"次の関数の不定積分を求めよ：$${sp.latex(sp.Integral(st.session_state['func'], x))}$$")
    
    # 解答を表示
    if st.button("解答を表示"):
        st.write(f"解答：$${sp.latex(st.session_state['integral'])}$$")



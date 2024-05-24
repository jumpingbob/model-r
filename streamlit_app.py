import streamlit as st
import sympy as sp
import random

# シンボルを定義
x, y, z = sp.symbols('x y z')

# 関数リストを定義します
functions = [
    'x', 'y', 'z', 'x**2', 'y**2', 'z**2', 'x**3', 'y**3', 'z**3', 
    'sp.sin(x)', 'sp.sin(y)', 'sp.sin(z)', 'sp.cos(x)', 'sp.cos(y)', 'sp.cos(z)', 
    'sp.exp(x)', 'sp.exp(y)', 'sp.exp(z)', '1/x', '1/y', '1/z', 'sp.log(x)', 'sp.log(y)', 'sp.log(z)',
    'x*y', 'x*z', 'y*z', 'x*y*z'
]

# 積分問題をランダムに生成する関数
def generate_problem():
    func_str = random.choice(functions)
    func = eval(func_str)
    variable = random.choice([x, y, z])
    return func_str, func, variable

# 解答を表示する関数
def solve_integral(func, variable):
    integral = sp.integrate(func, variable)
    return integral

st.title("積分問題生成器")

# セッション状態の初期化
if 'func_str' not in st.session_state:
    st.session_state['func_str'] = None
if 'func' not in st.session_state:
    st.session_state['func'] = None
if 'integral' not in st.session_state:
    st.session_state['integral'] = None
if 'variable' not in st.session_state:
    st.session_state['variable'] = None

# 問題を生成
if st.button("問題を生成"):
    st.session_state['func_str'], st.session_state['func'], st.session_state['variable'] = generate_problem()
    st.session_state['integral'] = solve_integral(st.session_state['func'], st.session_state['variable'])

# 問題を表示
if st.session_state['func_str']:
    st.write(f"次の関数の不定積分を求めよ（{st.session_state['variable']}について）：$${sp.latex(st.session_state['func'])}$$")
    
    # 解答を表示
    if st.button("解答を表示"):
        st.write(f"解答：$${sp.latex(st.session_state['integral'])}$$")

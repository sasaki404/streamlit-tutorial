from scipy.optimize import minimize
import streamlit as st
import numpy as np
from bokeh.plotting import figure

"""
# 2次関数と点の距離を最小化するアプリ
$y = ax^2 + bx + c$ と点$(s,t)$の距離が最小となる関数$y$上の点と、その時の距離を求めることができます。

#### 変数を入力してください
"""

a = st.number_input('a')
b = st.number_input('b')
c = st.number_input('c')
s = st.number_input('s')
t = st.number_input('t')


def f(x):
    return ((t-(a*(x**2)+b*x+c))**2+(s-x)**2)**0.5


res = minimize(fun=f, x0=0, method="SLSQP")
ans = res['x'].item()
ansy = a * ans * ans + b * ans + c
ansk = float(res['fun'])
st.write("関数と点の距離が最小となるときのx座標は", ans, "y座標は", ansy)
st.write("その時の最小の距離は", ansk)

x = np.arange(-100, 100, 0.1)
y = a * x ** 2 + b * x + c
p = figure(x_axis_label="x", y_axis_label="y",
           x_range=[-100, 100], y_range=[-100, 100])
p.line(x, y)
p.circle(x=s, y=t, size=12)
st.bokeh_chart(p)

import streamlit as st
import numpy as  np
import pandas as pd



number = st.sidebar.slider('pick a num', 0, 100, 40)


options = st.sidebar.multiselect(
    'what are you favorite colors',
    ['green','yellow','red','blue'],
    ['yellow','red']
)

st.sidebar.write(f'選択肢: {options} {number}')


left_col, center_col, right_col = st.columns(3)
left_col.slider('pick a num in left', 0,100,20)
right_col.slider('pick a num in right', 0,300,200)
center_col.slider('pick a num in center', 0,300,200)
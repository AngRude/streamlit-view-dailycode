import streamlit as st
st.write('# 안녕 수민아 반가워 난 이수의 웹페이지라고 해 음하하하')
view = [100 , 150 , 30]
st.write('# Youtube View')
st.write('## raw')
view
st.write('## bar chart')
st.bar_chart(view)
import pandas as pd
sview = pd.Series(view)
sview

import streamlit as st
st.write('# 내가짱이야 내가짱이야')
view = [100 , 150 , 30]
st.write('# Youtube View')
st.write('## raw')
view
st.write('## bar chart')
st.bar_chart(view)
import pandas as pd
sview = pd.Series(view)
sview

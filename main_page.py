import streamlit as st

st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")

import seaborn as sns

mpg = sns.load_dataset("mpg")

st.write("""
### 자동차 연비
""")

st.dataframe(mpg)

st.line_chart(mpg["mpg"])
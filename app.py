
import streamlit as st
import pandas as pd
st.title("DASHBOARD PAS")
df = pd.DataFrame({
    "Month":["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],
    "Sales":[1000,2000,3000,4000,5000,6000,125,123,1666,1256,2000,2500]
})
st.dataframe(df)
st.bar_chart(df.set_index("Month"))
st.line_chart(df.set_index("Month"))

import streamlit as st
from sklearn.datasets import load_iris

st.write('Hello World')
data = load_iris(as_frame=True).frame

st.write(data.head())
st.balloons()
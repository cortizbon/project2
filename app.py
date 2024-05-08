import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Hola, mundo")

np.random.seed(1234)

x = np.linspace(-5, 5, 1000)
e = np.random.normal(0, 10, 1000)
y = x ** 2

fig, ax = plt.subplots(1, 1, figsize=(10, 6))
ax.scatter(x, y)

st.pyplot(fig)
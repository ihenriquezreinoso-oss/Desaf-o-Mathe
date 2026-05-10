import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Modelo Interactivo: $y = B \sin(\omega t + \psi)$")

# Sliders interactivos
B = st.slider("Amplitud (B)", 0.0, 2.0, 1.0)
omega = st.slider("Frecuencia angular (ω)", 0.0, 20.0, 6.28)
psi = st.slider("Fase (ψ)", 0.0, float(np.pi), 0.0)

t = np.linspace(0, 10, 1000)
y = B * np.sin(omega * t + psi)

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(t, y)
ax.set_ylim(-2.2, 2.2)
ax.set_xlabel("Tiempo")
ax.set_ylabel("Amplitud")
ax.grid(True)

st.pyplot(fig)

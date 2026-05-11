import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Configuración de la página
st.set_page_config(page_title="Analizador de Biosensores", page_icon="🔬")

st.title("🧬 Simulación de Señal de Nanocantilever")
st.markdown("""
Esta herramienta permite modelar la respuesta de un biosensor basado en frecuencias resonantes. 
Ajusta los parámetros en la barra lateral para observar el comportamiento de la partícula.
""")

# Barra lateral profesional
st.sidebar.header("Configuración del Modelo")
B = st.sidebar.slider("Amplitud de Oscilación (𝜇m)", 0.0, 2.0, 1.0)
omega = st.sidebar.slider("Frecuencia Angular (rad/s)", 0.0, 20.0, 6.28)
psi = st.sidebar.slider("Desfase Inicial (rad)", 0.0, float(np.pi), 0.0)

st.sidebar.info("El modelo utiliza la ecuación general de movimiento armónico simple.")

# Cálculo
t = np.linspace(0, 10, 1000)
y = B * np.sin(omega * t + psi)

# Gráfico estético
plt.style.use('ggplot')
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(t, y, color='#4CAF50', label="Señal del Sensor")
ax.set_ylim(-2.5, 2.5)
ax.set_xlabel("Tiempo (s)")
ax.set_ylabel("Desplazamiento (𝜇m)")
ax.legend()

st.pyplot(fig)

# Métrica adicional
st.columns(3)[0].metric("Amplitud Máxima", f"{B} nm")
st.columns(3)[1].metric("Frecuencia", f"{omega/6.28:.2f} Hz")

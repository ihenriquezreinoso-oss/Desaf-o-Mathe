import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 1. Configuración de la página (Título en la pestaña del navegador e ícono)
st.set_page_config(page_title="Analizador de Biosensores", page_icon="🧬", layout="wide")

# 2. Título principal y descripción
st.title("🔬 Monitoreo de Señal: Nanocantilever")
st.markdown("""
Esta aplicación modela la oscilación de un biosensor al detectar microorganismos en un fluido. 
La **amplitud (B)** representa el desplazamiento máximo del sensor en micrómetros.
""")

# 3. Controles en la barra lateral (Sidebar)
st.sidebar.header("Configuración de la Señal")
b_val = st.sidebar.slider("Amplitud (B) [μm]", 0.0, 2.0, 1.008, help="Desplazamiento máximo en micrómetros")
w_val = st.sidebar.slider("Frecuencia Angular (ω) [rad/s]", 0.0, 20.0, 6.33)
p_val = st.sidebar.slider("Fase Inicial (ψ) [rad]", 0.0, float(np.pi), 0.0)

st.sidebar.markdown("---")
st.sidebar.write("**Modelo Matemático:**")
st.sidebar.latex(r"y(t) = B \cdot \sin(\omega t + \psi)")

# 4. Generación de los datos (Cálculos físicos)
t = np.linspace(0, 10, 1000)
y = b_val * np.sin(w_val * t + p_val)

# 5. Creación del diseño con columnas
col1, col2 = st.columns([3, 1])

with col1:
    # Estilo de gráfico profesional
    plt.style.use('ggplot')
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(t, y, color='#d62728', linewidth=2.5, label="Oscilación del sensor")
    ax.fill_between(t, y, alpha=0.1, color='#d62728')
    
    # Configuración de los ejes
    ax.set_title("Respuesta Dinámica (Escala Micrométrica)", fontsize=14)
    ax.set_xlabel("Tiempo (s)", fontsize=12)
    ax.set_ylabel("Amplitud (μm)", fontsize=12)
    ax.set_ylim(-2.5, 2.5)
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.legend(loc='upper right')
    
    # IMPORTANTE: Se pasa la figura 'fig' a st.pyplot
    st.pyplot(fig, use_container_width=True)

with col2:
    st.subheader("Datos del Sensor")
    st.metric(label="Amplitud", value=f"{b_val} μm")
    st.metric(label="Frecuencia", value=f"{w_val/(2*np.pi):.2f} Hz")
    st.info("Optimizado para evaluación de calidad microbiológica.")

# 6. Pie de página
st.caption("Proyecto de Ingeniería Civil en Biomedicina - 1er año UDD")


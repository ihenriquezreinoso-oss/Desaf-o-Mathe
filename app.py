import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 1. Configuración de la página
st.set_page_config(page_title="Analizador de Biosensores", page_icon="🧬", layout="wide")

# 2. Título y Contexto
st.title("🔬 Monitoreo de Señal: Nanocantilever")
st.markdown("""
Esta aplicación modela la oscilación de un biosensor al detectar partículas suspendidas en el aire. 
La **amplitud (B)** representa el desplazamiento máximo del sensor en micrómetros.
""")

# 3. Controles en la barra lateral
st.sidebar.header("Configuración de la Señal")
b_val = st.sidebar.slider("Amplitud (B) [μm]", 0.0, 2.0, 1.008)
w_val = st.sidebar.slider("Frecuencia Angular (ω) [rad/s]", 0.0, 20.0, 6.33)
p_val = st.sidebar.slider("Fase Inicial (ψ) [rad]", 0.0, float(np.pi), 0.0)

st.sidebar.markdown("---")
st.sidebar.write("**Modelo Matemático:**")
st.sidebar.latex(r"y(t) = B \cdot \sin(\omega t + \psi)")

# 4. Cálculos
t = np.linspace(0, 10, 1000)
y = b_val * np.sin(w_val * t + p_val)

# 5. Visualización Principal (Gráfico)
col1, col2 = st.columns([3, 1])

with col1:
    plt.style.use('ggplot')
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(t, y, color='#d62728', linewidth=2.5, label="Oscilación del sensor")
    ax.fill_between(t, y, alpha=0.1, color='#d62728')
    
    ax.set_title("Respuesta Dinámica (Escala Micrométrica)", fontsize=14)
    ax.set_xlabel("Tiempo (s)", fontsize=12)
    ax.set_ylabel("Amplitud (μm)", fontsize=12)
    ax.set_ylim(-2.5, 2.5)
    ax.grid(True, linestyle='--', alpha=0.6)
    
    st.pyplot(fig, use_container_width=True)

with col2:
    st.subheader("Datos del Sensor")
    st.metric(label="Amplitud", value=f"{b_val} μm")
    st.metric(label="Frecuencia", value=f"{w_val/(2*np.pi):.2f} Hz")
    st.info("Unidad de medida: Micrómetros (μm).")

# 6. NUEVA SECCIÓN: Fundamento del Voltaje (Lo que pediste agregar)
st.markdown("---")
with st.expander("🔍 ¿Cómo entra el Voltaje en el gráfico?"):
    st.markdown("""
    El sensor no mide "frecuencia" directamente como un número, sino que utiliza un **transductor piezoeléctrico** u óptico. 
    Así funciona el proceso:

    1. **Entrada de Datos:** La vibración mecánica de la viga genera una señal eléctrica.
    2. **Conversión a Voltaje:** El circuito electrónico convierte esa oscilación en una señal de **voltaje (V)** que varía en el tiempo.
    3. **El Gráfico (Dominio de la Frecuencia):** Para obtener el gráfico analizado, se aplica una **Transformada Rápida de Fourier (FFT)**. Esto toma la señal de voltaje y busca en qué frecuencias la amplitud (voltaje) es mayor.
    """)
    
    # Representación matemática de la FFT opcional
    st.latex(r"X(f) = \int_{-\infty}^{\infty} v(t) e^{-j 2\pi f t} dt")

# Pie de página
st.caption("Proyecto de Ingeniería Biomédica - Evaluación de calidad microbiológica del aire.")

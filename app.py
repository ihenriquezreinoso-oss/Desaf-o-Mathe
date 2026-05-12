import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 1. Configuración
st.set_page_config(page_title="Analizador de Biosensores", page_icon="🧬", layout="wide")

# 2. Título principal
st.title("🔬 Monitoreo de Señal: Nanocantilever")
st.markdown("Simulación de la respuesta dinámica del sensor ante partículas en suspensión.")

# 3. Controles (Sidebar)
st.sidebar.header("Parámetros del Sensor")
b_val = st.sidebar.slider("Amplitud (B) [μm]", 0.0, 2.0, 1.0)
w_val = st.sidebar.slider("Frecuencia (ω) [rad/s]", 0.0, 20.0, 6.3)

# 4. Cálculo de la señal senoidal
t = np.linspace(0, 10, 1000)
y = b_val * np.sin(w_val * t)

# 5. Visualización del Gráfico de Voltaje
col1, col2 = st.columns([3, 1])

with col1:
    plt.style.use('ggplot')
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(t, y, color='#d62728', linewidth=2, label="Señal de Voltaje (V)")
    ax.fill_between(t, y, alpha=0.1, color='#d62728')
    
    ax.set_title("Señal Eléctrica del Transductor", fontsize=14)
    ax.set_xlabel("Tiempo (s)", fontsize=12)
    ax.set_ylabel("Voltaje / Amplitud (μm)", fontsize=12)
    ax.set_ylim(-2.5, 2.5)
    
    st.pyplot(fig, use_container_width=True)

with col2:
    st.subheader("Estado Actual")
    st.metric(label="Desplazamiento", value=f"{b_val} μm")
    st.metric(label="Frecuencia", value=f"{w_val/(2*np.pi):.2f} Hz")

# 6. EXPLICACIÓN DEL PROCESO (Integrando el concepto de Fourier y Voltaje)
st.markdown("---")
st.subheader("⚙️ Fundamento del Procesamiento")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("**1. Transducción**")
    st.write("La vibración mecánica de la viga se convierte en una señal eléctrica (Voltaje) mediante un material piezoeléctrico.")

with c2:
    st.markdown("**2. Análisis de Fourier**")
    st.write("Se aplica una Transformada de Fourier para convertir esa señal de voltaje en información de frecuencia.")

with c3:
    st.markdown("**3. Detección**")
    st.write("Cualquier cambio en la frecuencia detectada indica la presencia de partículas sobre el sensor.")

st.info("Este flujo permite que un movimiento físico microscópico se transforme en datos digitales precisos.")


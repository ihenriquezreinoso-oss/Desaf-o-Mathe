import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 1. Configuración de la App
st.set_page_config(page_title="Analizador de Biosensores", page_icon="🧬", layout="wide")

st.title("🔬 Simulador de Biosensor: Nanocantilever")
st.markdown("Ajusta los parámetros para ver cómo cambia la señal eléctrica del sensor.")

# 2. Glosario rápido para el usuario (Para que sepan qué cambian)
with st.expander("❓ Guía rápida: ¿Qué estoy cambiando?"):
    st.write("""
    * **Amplitud (B):** Es el 'tamaño' de la onda. Representa qué tan fuerte está vibrando la viga del sensor en micrómetros ($\mu m$).
    * **Frecuencia (ω):** Es la 'velocidad' de la vibración. Si hay una partícula pesada, esta velocidad suele cambiar.
    * **Fase (ψ):** Es el 'punto de inicio' de la onda en el tiempo.
    """)

# 3. Controles con nombres claros
st.sidebar.header("Panel de Control")
b_val = st.sidebar.slider("Tamaño de Vibración (Amplitud μm)", 0.0, 2.0, 1.0)
w_val = st.sidebar.slider("Velocidad de Oscilación (Frecuencia)", 0.0, 20.0, 6.3)
p_val = st.sidebar.slider("Posición Inicial (Fase)", 0.0, float(np.pi), 0.0)

# 4. Cálculos
t = np.linspace(0, 10, 1000)
y = b_val * np.sin(w_val * t + p_val)

# 5. Gráfico Principal
col1, col2 = st.columns([3, 1])

with col1:
    plt.style.use('ggplot')
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(t, y, color='#d62728', linewidth=2, label="Señal de Voltaje")
    ax.fill_between(t, y, alpha=0.1, color='#d62728')
    
    ax.set_title("Señal en Tiempo Real", fontsize=14)
    ax.set_xlabel("Tiempo (segundos)", fontsize=12)
    ax.set_ylabel("Voltaje (Escala μm)", fontsize=12)
    ax.set_ylim(-2.5, 2.5)
    st.pyplot(fig, use_container_width=True)

with col2:
    st.subheader("Lectura Digital")
    st.metric(label="Desplazamiento Máximo", value=f"{b_val} μm")
    st.metric(label="Ciclos por segundo", value=f"{w_val/(2*np.pi):.2f} Hz")
    
# 6. Relación con el Voltaje
st.info("💡 Recuerda: Lo que ves arriba es la representación del voltaje generado por el transductor del sensor.")


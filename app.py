import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 1. Configuración de alto nivel
st.set_page_config(page_title="Sensor Biotecnológico", page_icon="🔬", layout="wide")

st.title("🧬 Monitoreo de Biosensor en Tiempo Real")
st.subheader("Proyecto: Evaluación de Calidad de Aire - CECOSF")

# 2. Explicación para perfiles no matemáticos
st.info("""
**¿Qué estamos viendo?** Este gráfico representa la oscilación de un sensor ultra sensible. 
Cuando una partícula en el aire toca el sensor, su forma de vibrar cambia. 
Aquí simulamos esa vibración convertida en una señal eléctrica (Voltaje).
""")

# 3. Panel de Control "A prueba de todo público"
st.sidebar.header("🕹️ Ajustes del Experimento")

# Usamos labels que expliquen la física y la matemática al mismo tiempo
b_val = st.sidebar.slider(
    "Amplitud / Intensidad del Choque (B)", 
    0.0, 2.0, 1.0, 
    help="Mide qué tan amplio es el movimiento de la viga. A mayor masa de la partícula, mayor puede ser el impacto."
)

w_val = st.sidebar.slider(
    "Frecuencia / Rapidez de Vibración (ω)", 
    0.0, 20.0, 6.3, 
    help="Mide cuántas veces oscila el sensor por segundo. Las partículas cambian la frecuencia de resonancia."
)

p_val = st.sidebar.slider(
    "Desfase / Punto de Inicio (ψ)", 
    0.0, float(np.pi), 0.0,
    help="Representa en qué momento exacto del ciclo empezamos a medir la señal."
)

# 4. Cálculos
t = np.linspace(0, 10, 1000)
y = b_val * np.sin(w_val * t + p_val)

# 5. Visualización Dual
col1, col2 = st.columns([2, 1])

with col1:
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(t, y, color='#2E86C1', linewidth=3, label="Señal del Transductor (Voltaje)")
    ax.fill_between(t, y, alpha=0.2, color='#2E86C1')
    
    # Ejes claros para el Decano
    ax.set_title("Ondas de Resonancia del Nanocantilever", fontsize=15, fontweight='bold')
    ax.set_xlabel("Tiempo de muestreo (ms)", fontsize=12)
    ax.set_ylabel("Potencial Eléctrico (V) / Desplazamiento (μm)", fontsize=12)
    ax.set_ylim(-2.5, 2.5)
    ax.grid(True, linestyle=':', alpha=0.6)
    st.pyplot(fig, use_container_width=True)

with col2:
    st.write("### 📊 Análisis de Datos")
    st.metric("Desplazamiento Máximo", f"{b_val} μm", help="Distancia física que se mueve la micro-viga.")
    st.metric("Frecuencia Detectada", f"{w_val/(2*np.pi):.2f} Hz", help="Cantidad de vibraciones completas por segundo.")
    
    # Explicación para el Bio-profe
    st.success(f"""
    **Interpretación Biológica:**
    Si este fuera un sensor real, una frecuencia de **{w_val/(2*np.pi):.2f} Hz** nos indicaría si el aire está limpio o si hay presencia de agentes patógenos alterando la masa del dispositivo.
    """)

# 6. Fundamentación técnica final
with st.expander("🛠️ Notas Técnicas para Facultad"):
    st.write("""
    El gráfico modela la **función de transferencia** del sensor. 
    1. La vibración mecánica es detectada por un cristal piezoeléctrico.
    2. El cristal genera un voltaje proporcional al desplazamiento ($y$).
    3. La señal resultante es procesada mediante una Transformada de Fourier para identificar cambios en la masa (detección de partículas).
    """)

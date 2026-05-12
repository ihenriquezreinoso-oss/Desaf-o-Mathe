import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 1. Configuración de la interfaz
st.set_page_config(page_title="Bio-Detector Inteligente", page_icon="🍃", layout="wide")

# Estilo personalizado para mejorar la estética
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

st.title("🍃 Detector de Partículas: Calidad de Aire CECOSF")
st.write("---")

# 2. SECCIÓN EXPLICATIVA INICIAL (Para el Profe de Bio y público general)
col_text, col_img = st.columns([2, 1])

with col_text:
    st.subheader("¿Cómo funciona este sensor?")
    st.write("""
    Imagina una **micro-viga** (como un trampolín invisible al ojo humano). 
    Cuando el aire está limpio, vibra a un ritmo constante. Si una partícula (polvo, polen o bacteria) 
    se posa sobre ella, la viga se vuelve más pesada y su 'latido' cambia.
    
    **Mueve los controles de la izquierda para simular diferentes escenarios.**
    """)

# 3. PANEL DE CONTROL INTUITIVO (Sidebar)
st.sidebar.header("🕹️ Simular Escenario")

# Traducimos la matemática a eventos físicos
st.sidebar.subheader("1. Gravedad del Impacto")
impacto = st.sidebar.select_slider(
    "¿Qué tan grande es la partícula?",
    options=["Minúscula", "Pequeña", "Mediana", "Grande"],
    value="Pequeña"
)
# Mapeo de impacto a Amplitud (B)
b_map = {"Minúscula": 0.2, "Pequeña": 0.8, "Mediana": 1.4, "Grande": 2.0}
b_val = b_map[impacto]

st.sidebar.subheader("2. Estado del Aire")
aire = st.sidebar.select_slider(
    "Densidad del flujo de aire",
    options=["Calmo", "Normal", "Turbulento"],
    value="Normal"
)
# Mapeo de aire a Frecuencia (w)
w_map = {"Calmo": 3.0, "Normal": 7.0, "Turbulento": 15.0}
w_val = w_map[aire]

st.sidebar.write("---")
st.sidebar.caption("⚙️ **Datos para el Decano (Ingeniería):**")
st.sidebar.text(f"Amplitud (B): {b_val} μm")
st.sidebar.text(f"Frecuencia (ω): {w_val} rad/s")

# 4. CÁLCULOS Y GRÁFICO
t = np.linspace(0, 10, 1000)
y = b_val * np.sin(w_val * t)

# Visualización central
st.subheader("📡 Visualización del 'Latido' del Sensor")
fig, ax = plt.subplots(figsize=(12, 4))
ax.plot(t, y, color='#00C853', linewidth=3)
ax.fill_between(t, y, color='#00C853', alpha=0.1)
ax.set_ylim(-2.2, 2.2)
ax.axis('off') # Quitamos los ejes para que sea más "limpio" y visual para el público general
st.pyplot(fig, use_container_width=True)

# 5. LECTURA DE RESULTADOS (A prueba de todo público)
res1, res2, res3 = st.columns(3)

with res1:
    st.metric("Estado de la Viga", "Oscilando" if b_val > 0 else "Inactiva")
with res2:
    estado_salud = "Óptimo" if w_val < 10 else "Alerta"
    st.metric("Calidad de Aire", estado_salud)
with res3:
    st.metric("Detección", f"{impacto}")

# 6. EXPLICACIÓN TÉCNICA (Oculta para quien quiera profundizar)
with st.expander("🔬 Especificaciones Técnicas (Uso Académico)"):
    st.markdown(f"""
    **Modelo Matemático:** $y(t) = {b_val} \cdot \sin({w_val} t)$
    
    Este gráfico representa la conversión de energía mecánica en eléctrica (Voltaje) 
    mediante un transductor piezoeléctrico. Los cambios en la frecuencia ($\omega$) 
    son directamente proporcionales al cambio de masa ($\Delta m$) en la superficie del nanocantilever.
    """)

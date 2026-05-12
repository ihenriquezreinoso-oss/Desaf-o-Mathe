import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 1. Configuración de nivel profesional
st.set_page_config(page_title="Modelamiento Biosensor", page_icon="🔬", layout="wide")

# 2. Encabezado descriptivo (Contexto del Proyecto)
st.title("🔬 Caracterización Dinámica de Nanocantilever")
st.markdown("""
Esta plataforma modela la respuesta de un sensor de masa para la detección de partículas suspendidas. 
La señal representa la **transducción piezoeléctrica**: cómo el movimiento físico se convierte en voltaje.
""")

# 3. Panel de Parámetros Técnicos
st.sidebar.header("Variables de Simulación")

# Mantenemos el rigor de los valores pero añadimos contexto
b_val = st.sidebar.slider(
    "Amplitud (B) [μm]", 
    min_value=0.0, max_value=2.0, value=1.008, step=0.001,
    help="Magnitud del desplazamiento físico de la micro-viga."
)

w_val = st.sidebar.slider(
    "Frecuencia Angular (ω) [rad/s]", 
    min_value=0.0, max_value=20.0, value=6.33,
    help="Velocidad de oscilación. Cambios en esta variable indican detección de masa."
)

# 4. Cálculo de la función de onda
t = np.linspace(0, 10, 1000)
y = b_val * np.sin(w_val * t)

# 5. Área de Visualización e Interpretación
col_graf, col_info = st.columns([2, 1])

with col_graf:
    # Gráfico con estándares de laboratorio
    plt.style.use('dark_background') # Le da un toque de 'instrumento de laboratorio'
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(t, y, color='#00FF41', linewidth=2, label="Señal de Salida (V)") # Color osciloscopio
    ax.axhline(0, color='white', linewidth=0.5, alpha=0.5)
    
    ax.set_title("Respuesta del Sensor (Dominio del Tiempo)", fontsize=14, color='white')
    ax.set_xlabel("Tiempo (s)", fontsize=10)
    ax.set_ylabel("Amplitud / Voltaje (μm)", fontsize=10)
    ax.set_ylim(-2.5, 2.5)
    ax.grid(True, linestyle='--', alpha=0.3)
    
    st.pyplot(fig, use_container_width=True)

with col_info:
    st.subheader("📊 Análisis del Modelo")
    
    # Explicación de qué estamos modelando exactamente
    st.write("**Fenómeno:**")
    st.info("""
    Estamos modelando la **Frecuencia de Resonancia**. 
    En un biosensor real, cuando una partícula se deposita sobre la viga, la masa aumenta y la frecuencia ($\omega$) disminuye.
    """)
    
    # Datos técnicos exactos para el Decano
    st.write("**Lectura de Instrumentación:**")
    st.metric("Voltaje Máximo", f"{b_val} V")
    st.metric("Frecuencia Natural", f"{w_val/(2*np.pi):.2f} Hz")

# 6. Fundamento del Proceso (Voltaje y Fourier)
st.divider()
st.subheader("⚙️ Cadena de Medición")

f1, f2, f3 = st.columns(3)

with f1:
    st.write("**1. Entrada Mecánica**")
    st.caption("La interacción con partículas genera un desplazamiento en el cantilever medido en micras.")

with f2:
    st.write("**2. Transducción**")
    st.caption("El efecto piezoeléctrico convierte este desplazamiento en una señal eléctrica de voltaje.")

with f3:
    st.write("**3. Análisis (FFT)**")
    st.caption("A partir de esta onda senoidal, se extrae la frecuencia característica mediante la Transformada de Fourier.")

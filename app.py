import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 1. TÍTULO Y CONFIGURACIÓN
st.set_page_config(page_title="Modelo Biosensor CECOSF", layout="wide")
st.title("Modelo Aplicado: Detección por Resonancia en Nanocantilevers")

# 2. DESCRIPCIÓN BREVE
st.markdown("""
Esta plataforma simula la respuesta de un biosensor mecánico diseñado para el monitoreo de la calidad del aire. 
A continuación, podrá interactuar con el modelo de la señal eléctrica generada cuando el sensor detecta 
partículas en suspensión (polvo, patógenos o aerosoles).
""")

# 3. CÁLCULOS TÉCNICOS
t = np.linspace(0, 10, 1000)

# Sidebar para edición de parámetros
st.sidebar.header("⚙️ Parámetros Editables")

b_val = st.sidebar.slider("Amplitud (B)", 0.0, 2.0, 1.0, step=0.01)
w_val = st.sidebar.slider("Frecuencia Angular (ω)", 0.0, 20.0, 6.3, step=0.1)
p_val = st.sidebar.slider("Fase Inicial (ψ)", 0.0, float(np.pi), 0.0)

y = b_val * np.sin(w_val * t + p_val)

# 4. GRÁFICO CON SEÑALIZACIÓN CLARA
st.subheader("📊 Visualización de la Señal (Dominio del Tiempo)")

fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(t, y, color='#d62728', linewidth=2.5, label="Voltaje de Salida")

# Señalización de Máximos Locales
ymax = y.max()
if ymax > 0:
    ax.axhline(ymax, color='gray', linestyle='--', alpha=0.5)
    ax.axhline(-ymax, color='gray', linestyle='--', alpha=0.5)
    ax.text(0.1, ymax + 0.1, f'Máximo: {ymax:.2f} μm', color='gray', fontweight='bold')

# Configuración de Ejes (Claros para todo público)
ax.set_xlabel("Tiempo (Segundos) - Eje X", fontsize=11)
ax.set_ylabel("Amplitud / Voltaje (Micrómetros μm) - Eje Y", fontsize=11)
ax.set_ylim(-2.5, 2.5)
ax.grid(True, which='both', linestyle=':', alpha=0.7)
ax.legend(loc="upper right")

st.pyplot(fig, use_container_width=True)

# 5. EXPLICACIÓN DE PARÁMETROS (Consecuencias y Por qué cambiarlos)
st.divider()
st.subheader("📝 Guía de Parámetros")
col_p1, col_p2, col_p3 = st.columns(3)

with col_p1:
    st.write("**Amplitud (B)**")
    st.caption("**Corresponde a:** El desplazamiento máximo de la micro-viga.")
    st.caption("**Consecuencia:** Hace la onda más alta o más baja.")
    st.caption("**¿Por qué cambiarlo?** Para simular qué tan fuerte fue el impacto de la partícula detectada.")

with col_p2:
    st.write("**Frecuencia (ω)**")
    st.caption("**Corresponde a:** La rapidez con la que vibra el sensor.")
    st.caption("**Consecuencia:** Comprime o expande la onda horizontalmente.")
    st.caption("**¿Por qué cambiarlo?** Es el dato clave: las partículas adheridas cambian la masa y, por ende, la frecuencia.")

with col_p3:
    st.write("**Fase (ψ)**")
    st.caption("**Corresponde a:** El punto exacto de inicio de la vibración.")
    st.caption("**Consecuencia:** Desplaza la onda hacia la izquierda o derecha.")
    st.caption("**¿Por qué cambiarlo?** Para sincronizar la medición con el momento exacto del choque de la partícula.")

# 6. LECTURA DE INSTRUMENTACIÓN
st.divider()
st.subheader("📑 Lectura de Instrumentación")
m1, m2, m3 = st.columns(3)
m1.metric("Voltaje de Pico", f"{b_val} V")
m2.metric("Frecuencia de Oscilación", f"{w_val/(2*np.pi):.2f} Hz")
m3.metric("Desplazamiento Máximo", f"{b_val} μm")

# 7. CADENA DE MEDICIÓN (A prueba de todo público)
st.divider()
st.subheader("🔗 Cadena de Medición: Del Aire al Dato")
st.info("""
1. **Impacto:** Una partícula en el aire choca con nuestro sensor (Nanocantilever).
2. **Movimiento:** El sensor vibra como un trampolín minúsculo (esto genera la Amplitud).
3. **Conversión:** Un material especial transforma ese movimiento en electricidad (Voltaje).
4. **Captura:** La computadora lee ese voltaje y dibuja la onda que ves arriba.
5. **Resultado:** Al analizar qué tan rápido vibra la onda, sabemos qué tipo de partícula se detectó.
""")

st.caption("A partir de esta onda senoidal, se extrae la frecuencia característica mediante la Transformada de Fourier.")

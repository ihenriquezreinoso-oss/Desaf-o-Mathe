import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# -----------------------------
# Configuración inicial
# -----------------------------
B0 = 1
omega0 = 2*np.pi
psi0 = 0

t = np.linspace(0, 10, 1000)

# -----------------------------
# Crear figura
# -----------------------------
fig, ax = plt.subplots(figsize=(12, 7))
plt.subplots_adjust(left=0.1, bottom=0.35)

# Función inicial
y = B0 * np.sin(omega0 * t + psi0)
[line] = ax.plot(t, y, lw=3)

ax.set_title("Modelo interactivo: y = B sin(ωt + ψ)", fontsize=16)
ax.set_xlabel("Tiempo")
ax.set_ylabel("Amplitud")
ax.grid(True)
ax.set_ylim(-5, 5)

# -----------------------------
# Crear sliders
# -----------------------------
ax_B = plt.axes([0.2, 0.22, 0.65, 0.03])
ax_omega = plt.axes([0.2, 0.16, 0.65, 0.03])
ax_psi = plt.axes([0.2, 0.10, 0.65, 0.03])

slider_B = Slider(ax_B, 'B', 0.1, 5.0, valinit=B0)
slider_omega = Slider(ax_omega, 'ω', 0.1, 20.0, valinit=omega0)
slider_psi = Slider(ax_psi, 'ψ', -2*np.pi, 2*np.pi, valinit=psi0)

# -----------------------------
# Actualización dinámica
# -----------------------------
def update(val):
    B = slider_B.val
    omega = slider_omega.val
    psi = slider_psi.val

    y = B * np.sin(omega * t + psi)
    line.set_ydata(y)

    ax.set_ylim(-B-1, B+1)

    fig.canvas.draw_idle()

slider_B.on_changed(update)
slider_omega.on_changed(update)
slider_psi.on_changed(update)

plt.show()

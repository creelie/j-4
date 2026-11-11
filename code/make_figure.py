"""Draws fig_m2.png: the invariant -|F|^2/(864 c^2 k^2) = (r^6+k)^(-7/3) (k=1)
of the Duff-Stelle membrane over a plane of the transverse space."""
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

out = sys.argv[1] if len(sys.argv) > 1 else "fig_m2.png"
y1, y2 = np.meshgrid(np.linspace(-1.8, 1.8, 241), np.linspace(-1.8, 1.8, 241))
r = np.hypot(y1, y2)
z = (r**6 + 1.0) ** (-7.0 / 3.0)
fig = plt.figure(figsize=(7.2, 5.0))
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(y1, y2, z, cmap="viridis", rstride=3, cstride=3, linewidth=0, antialiased=True)
ax.set_xlabel(r"$y^1$", labelpad=6)
ax.set_ylabel(r"$y^2$", labelpad=6)
ax.set_zlabel(r"$-|F|^2/(864\,c^2k^2)$", labelpad=8)
ax.view_init(elev=24, azim=-58)
ax.set_zlim(0, 1.05)
fig.tight_layout()
fig.savefig(out, dpi=220)

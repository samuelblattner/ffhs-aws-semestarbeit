"""
Module: AWD, Analysis, wissenschaftliches Rechnen und Datenvisualisierung
Course: BSc INF 2015, ZH5-Mo, FS16, Schuler Josef A.
This is my solution for the sixth of eight parts for the module at FFHS. This shows
some examples of how to visualize data using matplotlib.
"""

import matplotlib.pyplot as plt
import numpy as np
from sympy import *

from mpl_toolkits.mplot3d import Axes3D


# STATICS
DOMAIN_STEP_SIZE = 0.2

# Initialize Graphics
fig_surf = plt.figure()
ax_surf = fig_surf.add_subplot(111, projection='3d')
ax_surf.set_xlabel('X axis')
ax_surf.set_ylabel('Y axis')
ax_surf.set_zlabel('Z axis')

fig_bar = plt.figure()
ax_bar = fig_bar.add_subplot(111, projection='3d')
ax_bar.set_xlabel('X axis')
ax_bar.set_ylabel('Y axis')
ax_bar.set_zlabel('Z axis')

# Define domain
x_domain = {'start': 0, 'end': np.pi * 2, 'step': DOMAIN_STEP_SIZE}
y_domain = {'start': 0, 'end': np.pi * 2, 'step': DOMAIN_STEP_SIZE}

# Define 3D sin/cos mesh
X = np.arange(x_domain['start'], x_domain['end'], x_domain['step'])
Y = np.arange(y_domain['start'], y_domain['end'], y_domain['step'])

# Define and calculate 3D Diff and custom color map
x, y = symbols('x y')
diff_exp_x = diff(sin(x) + cos(y), x)
diff_exp_y = diff(sin(x) + cos(y), y)
ZDiff = [[abs(diff_exp_x.subs({x: cur_x, y: cur_y})) + abs(diff_exp_y.subs({x: cur_x, y: cur_y})) for cur_x in X] for cur_y in Y]
ZDiff = np.array(ZDiff, dtype='float')
ZDiff = ZDiff / ZDiff.max()

# Create meshgrid for surface
X, Y = np.meshgrid(X, Y)
Z = np.sin(X) + np.cos(Y)

# Render 3d bars
block_sizes = [DOMAIN_STEP_SIZE for d in range(0, len(X.flatten()))]
bar_colors = [(red, red*0.6, 0.3) for red in ZDiff.flatten()]
ax_bar.bar3d(Y.flatten(), X.flatten(), Z.flatten(), block_sizes, block_sizes, ZDiff.flatten(), color=bar_colors)

# Define and render ground Shadow map
ax_surf.contourf(X, Y, Z, zdir='z', offset=-2.1, cmap='gray', levels=np.linspace(-2, 2, 50))

# Render Surface
surf = ax_surf.plot_surface(X, Y, Z, color='r', facecolors=plt.cm.jet(ZDiff), rstride=1, cstride=1)

plt.show()

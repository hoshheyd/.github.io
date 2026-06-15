import numpy as np
import matplotlib.pyplot as plt

# Define the physical domain and regulatory scale
r = np.linspace(0.1, 5.0, 500)
r_reg = 1.0  # The SAGD phase-space regulatory scale
GM = 1.0     # Normalized mass parameter

# Classical Curvature (Runaway)
K_classical = GM / (r**3)

# SAGD Regulated Curvature (GERC Mechanism)
# The exponential factor models the geometric pushback and torsional channel shift
K_SAGD = (GM / (r**3)) * (1 - np.exp(-(r / r_reg)**4))

# Setup the publication-quality plot
plt.figure(figsize=(10, 6))
plt.style.use('dark_background')

# Plot the classical singular limit
plt.plot(r, K_classical, color='red', linestyle='--', linewidth=2, 
         label='Classical Runaway (Singular Limit)')

# Plot the SAGD regulated response
plt.plot(r, K_SAGD, color='cyan', linewidth=3, 
         label='SAGD Regulated Response (GERC)')

# Annotations and structural markers
plt.axvline(x=r_reg, color='yellow', linestyle=':', linewidth=1.5, alpha=0.7)
plt.text(r_reg + 0.1, 6, 'Regulatory Scale ($r_{reg}$)', color='yellow', fontsize=12)

# Formatting
plt.title('The Cosmic Thermostat: SAGD High-Curvature Regulation', fontsize=16, pad=15)
plt.xlabel('Radial Coordinate / Compression Scale ($r$)', fontsize=14)
plt.ylabel('Effective Metric Curvature ($\mathcal{K}$)', fontsize=14)
plt.ylim(0, 10)
plt.xlim(0, 5)
plt.legend(loc='upper right', fontsize=12)
plt.grid(True, alpha=0.2)

# Display the simulation
plt.tight_layout()
plt.show()

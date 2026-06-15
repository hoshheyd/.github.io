import numpy as np
import matplotlib.pyplot as plt

# Analytical Formulation: The GERC Regulatory Response
# Parametrar för simuleringen
r = np.linspace(0.1, 5.0, 500)
r_reg = 1.0  # SAGD-fasrumsregleringsskala
GM = 1.0     # Normaliserad massa

# Klassisk krökning (Singularitet)
K_classical = GM / (r**3)

# SAGD Reglerad krökning (GERC-mekanism)
K_SAGD = (GM / (r**3)) * (1 - np.exp(-(r / r_reg)**4))

# Skapa den vetenskapliga grafen
plt.figure(figsize=(10, 6))
plt.style.use('dark_background')

plt.plot(r, K_classical, color='red', linestyle='--', linewidth=2, 
         label='Klassisk singularitet')
plt.plot(r, K_SAGD, color='cyan', linewidth=3, 
         label='SAGD Reglerat GERC-svar')

plt.axvline(x=r_reg, color='yellow', linestyle=':', linewidth=1.5, alpha=0.7)
plt.text(r_reg + 0.1, 6, 'Regleringsskala ($r_{reg}$)', color='yellow', fontsize=12)

plt.title('GERC-mekanismen: Kosmisk termostat', fontsize=16)
plt.xlabel('Radiell koordinat ($r$)', fontsize=14)
plt.ylabel('Effektiv krökning ($\mathcal{K}$)', fontsize=14)
plt.ylim(0, 10)
plt.legend()
plt.grid(True, alpha=0.2)

# Spara bilden lokalt för att kunna ladda upp den till README
plt.savefig('cosmic_thermostat.png', dpi=300)
plt.show()

#!/bin/python

import matplotlib.pyplot as plt
import numpy as np

density_lh2 = 0.071 # kg/L
density_lox = 1.141 # kg/L

mass_ratio_lox_lh2 = 7 # this is dependent on how fuel rich the engine is burning, according to H2 + O2 -> H2O you would get 8, but then you have "hot-oxygen" problems and no cooling of nozzle by fuel
volume_lh2 = 1
volume_lox = mass_ratio_lox_lh2 * (density_lh2/density_lox)
volume_ratio_lox_lh2 = volume_lox/volume_lh2

print('Volume lh2 per liter of fuel {}'.format(volume_lh2))
print('Volume lox per liter of fuel {}'.format(volume_lox))

# dry-wet ratio: tank mass/(tank mass + propellant mass)
mass_per_liter_of_lh2_tank = np.linspace(0.001, 0.1, 100)
mass_of_lox_tank_per_liter_of_lh2 = mass_per_liter_of_lh2_tank * volume_ratio_lox_lh2
mass_of_combined_fuel_tanks = mass_per_liter_of_lh2_tank + mass_of_lox_tank_per_liter_of_lh2

mass_of_lox_per_liter_of_lh2 = density_lox * volume_ratio_lox_lh2
mass_of_combined_fuel_per_liter_of_lh2 = mass_of_lox_per_liter_of_lh2 + density_lh2

print('Mass of one liter of LH2 {}'.format(density_lh2))
print('Mass of corresponding amount of LOx {}'.format(mass_of_lox_per_liter_of_lh2))
print('Combined mass per one liter of LH2 {}'.format(mass_of_combined_fuel_per_liter_of_lh2))

dry_wet_ratio_lh2 = mass_per_liter_of_lh2_tank/(mass_per_liter_of_lh2_tank + density_lh2)
dry_wet_ratio_lox = mass_of_lox_tank_per_liter_of_lh2/(mass_of_lox_tank_per_liter_of_lh2 + mass_of_lox_per_liter_of_lh2)
dry_wet_ratio_combined = mass_of_combined_fuel_tanks/(mass_of_combined_fuel_tanks + mass_of_combined_fuel_per_liter_of_lh2)


ax = plt.axes()
ax.semilogy(mass_per_liter_of_lh2_tank, dry_wet_ratio_lh2 * 100, label='lh2')
ax.semilogy(mass_per_liter_of_lh2_tank, dry_wet_ratio_lox * 100, label='lox')
ax.semilogy(mass_per_liter_of_lh2_tank, dry_wet_ratio_combined * 100, label='lh2+lox')
ax.set(xlabel='mass of tank per liter of LH2 in kg',
       ylabel='dry-wet ratio of tank (percentage)')
ax.legend()
ax.grid(True, which='both')
ax.set_title('Dry-wet mass ratios for LH2 and LOx tanks')
plt.show()
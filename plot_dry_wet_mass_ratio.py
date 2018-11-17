#!/bin/python

import matplotlib.pyplot as plt
import numpy as np

# For literature comparison we always want to base ourselves on real life LH2+LOx combination
# The point is to figure out the dry-wet mass ratio for LH2 from literature that typically considers all propellants together
# So we assume that the tanks for LH2 and LOx are equal, but that LH2 is far less dense, and calculate from that the dry-wet ratio of LH2 tanks
density_lh2 = 0.071 # kg/L
density_lox = 1.141 # kg/L

# In KSP:
# Oxidizer has a density of 0.005 metric tonnes/5L, or 0.001 metric tonnes/L, or 1 kg/L
# LqdHydrogen has a density of 0.00007085 metric tonnes/L, or 0.07085 kg/L
# CryoTanks engines run in a ratio of 15:1 units, so 15 liter of LqdHydrogen for every 5 liters of Oxidizer

# Oxider can be many things, for example:
# LOx: then all the mass is oxygen
# N2O4: then 4*16/(2*14+4*16) = 69.6% is oxygen

# LOx would make the most sense for LH2, but this is KSP, and Oxidizer doesn't boiloff
# Note that all cited resources will use LOx, so the plotting will always talk about LOx, because we are interested in the LH2 part of the tanks
# Mass ratio when Oxidizer is LOx: (1*5)/(0.07085*15) = 4.705
# Mass ratio when Oxidizer is N2O4: (1*5)/(0.07085*15*0.696) = 6.760
# Density wise neither of two match 1 kg/L, LOx being the least dense of them all
# And choosing either of these two extreme answers is a bit weird, because 4.705 is extremely fuel rich, not applied typically at all, but 6.670 is for state of the art engines
# If we look at the actual density LOx has the lowest density of all the oxidizers
# KSP probably made a bit a random choice given the rounded number

# The fun thing is this whole consideration doesn't matter
# Because we are only interesting in the dry-mass of LH2 tanks for a real rocket
# A real rocket tank runs at a predefined ratio for that given engine design
# Thus includes a predefined ratio of LH2 and LOx in its tanks, thus also the combined dry-wet mass ratio
# This will tell us what a decent load-bearing tank is like (the shuttle external tank is not part of the main structure)

# The Arianne H-173 stage has a dry-wet ratio of 6.86% (see https://www.nasa.gov/pdf/382034main_018%20-%2020090706.05.Analysis_of_Propellant_Tank_Masses.pdf)
# It uses a Vulcain 2 engine, with a fuel to oxidizer ratio of 6.7 (http://www.astronautix.com/v/vulcain2.html)

mass_ratio_lox_lh2 = 6.7 # this is dependent on how fuel rich the engine is burning, according to H2 + O2 -> H2O you would get 8, but then you have "hot-oxygen" problems and no cooling of nozzle by fuel
desired_combined_dry_wet_ratio = 0.0686
volume_lh2 = 1
volume_lox = mass_ratio_lox_lh2 * (density_lh2/density_lox)
volume_ratio_lox_lh2 = volume_lox/volume_lh2

print('Volume lh2 per liter of fuel {}'.format(volume_lh2))
print('Volume lox per liter of fuel {}'.format(volume_lox))

# dry-wet ratio: tank mass/(tank mass + propellant mass)
mass_per_liter_of_lh2_tank = np.linspace(0.001, 0.1, 1000)
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

first_index_where_dry_wet_ratio_combined_exceeds_desired_value = np.where(dry_wet_ratio_combined > desired_combined_dry_wet_ratio)[0][0]
print('Dry-wet ratio mass ratio of LH2 tank {}% at a combined ratio {}%'.format(dry_wet_ratio_lh2[first_index_where_dry_wet_ratio_combined_exceeds_desired_value],
                                                                                dry_wet_ratio_combined[first_index_where_dry_wet_ratio_combined_exceeds_desired_value]))
print('Dry-wet ratio mass ratio of LOx tank {}% at a combined ratio {}, note that Oxidizer is not garuanteed to be LOx, and this only applies to a rocket running a fuel to oxidizer ratio of {}, so applicability is limited'.format(
                                                                                dry_wet_ratio_lox[first_index_where_dry_wet_ratio_combined_exceeds_desired_value],
                                                                                dry_wet_ratio_combined[first_index_where_dry_wet_ratio_combined_exceeds_desired_value],
                                                                                mass_ratio_lox_lh2))

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
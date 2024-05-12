import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator
import math

with open(.config_data.txt, r) as data_file
data = [float(num) if . in num else int(num) for num in data_file.read().split(n)]

array_data = np.loadtxt(.data_info.txt, dtype=int)

voltage_increment = data[1]
time_increment = data[0]

voltages_array = array_data  voltage_increment
time_array = np.arange(0, len(array_data))  time_increment

maximum_voltage = np.max(voltages_array)
max_voltage_index = np.argmax(voltages_array)
maximum_time = np.max(time_array)
max_time_index = np.argmax(time_array)

charging_info = [time_array[max_voltage_index], voltages_array[max_voltage_index]]
discharging_info = [time_array[max_voltage_index], voltages_array[max_voltage_index]]

figure, axes = plt.subplots(figsize=(16, 10), dpi=400)

axes.set_xlabel(Time, s, fontsize=16)
axes.set_ylabel(Voltage, V, fontsize=16)
axes.set_title(Capacitor Charge-Discharge Graph in RC-Circuit, fontsize=20)

line_charge, = axes.plot(charging_info[0], charging_info[1], color='blue')
line_discharge, = axes.plot(discharging_info[0], discharging_info[1], color='red')

line_charge.set_label(Capacitor Charge)
line_discharge.set_label(Capacitor Discharge)
axes.legend(prop={size 16})

x_limits = (0.0, math.ceil(maximum_time))
y_limits = (0.0, 3.5)
axes.set(xlim=x_limits, ylim=y_limits)

axes.xaxis.set_minor_locator(MultipleLocator(0.5))
axes.xaxis.set_major_locator(MultipleLocator(1.0))
axes.yaxis.set_minor_locator(MultipleLocator(0.25))
axes.yaxis.set_major_locator(MultipleLocator(0.5))
axes.grid(color=blue, which=both, linestyle='', linewidth=0.5)

charging_time = time_array[max_voltage_index] - time_array[0]
discharging_time = time_array[-1] - time_array[max_voltage_index]

axes.axvline(x=charging_time, ymin=y_limits[0], ymax=maximum_voltagey_limits[1], color='green', linestyle='dashed')
axes.axhline(y=maximum_voltage, xmin=x_limits[0], xmax=charging_timex_limits[1], color='green', linestyle='dashed')

axes.scatter(time_array[max_voltage_index], maximum_voltage, color='green')

axes.scatter(x=charging_time, y=0.0, color='green')
axes.text(x=charging_time+0.1, y=0.05, s=str(round(charging_time, 2)), fontsize=12)

axes.scatter(x=0.0, y=maximum_voltage, color='green')
axes.text(x=0.1, y=maximum_voltage+0.05, s=str(round(maximum_voltage, 2)), fontsize=12)

axes.text(x=(charging_time2-0.8), y=maximum_voltage2, s=(Charging Time  + str(round(charging_time, 2)) +  s), color='blue', fontsize=14)
axes.text(x=(charging_time+discharging_time2-0.8), y=maximum_voltage2, s=(Discharging Time  + str(round(discharging_time, 2)) +  s), color='red', fontsize=14)

figure.savefig(circuit_charges.svg)






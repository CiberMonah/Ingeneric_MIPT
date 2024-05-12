import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator
import math

with open("./configuration.txt", "r") as config_file:
config_data = [float(num) for num in config_file.read().split("\n")]

data_array = np.loadtxt("./data.txt", dtype=int)

voltage_step = config_data[1]
time_step = config_data[0]

voltages = data_array * voltage_step
times = np.arange(0, len(data_array)) * time_step

max_voltage = np.max(voltages)
max_voltage_index = np.argmax(voltages)
max_time = np.max(times)
max_time_index = np.argmax(times)

charging_data = [times[0:max_voltage_index:], voltages[0:max_voltage_index:]]
discharging_data = [times[max_voltage_index::], voltages[max_voltage_index::]]

figure, axes = plt.subplots(figsize = (16, 10), dpi = 400)

axes.set_xlabel("Time, s", fontsize = 16)
axes.set_ylabel("Voltage, V", fontsize = 16)
axes.set_title("Capacitor charge-discharge graph in RC-circuit", fontsize = 20)

charge_line, = axes.plot(charging_data[0], charging_data[1], color = 'blue')
discharge_line, = axes.plot(discharging_data[0], discharging_data[1], color = 'red')

charge_line.set_label("Capacitor charge")
discharge_line.set_label("Capacitor discharge")
axes.legend(prop={"size":16})

x_limits = (0.0, math.ceil(max_time))
y_limits = (0.0, 3.5)
axes.set(xlim = x_limits, ylim = y_limits)

axes.xaxis.set_minor_locator(MultipleLocator(0.5))
axes.xaxis.set_major_locator(MultipleLocator(1.0))
axes.yaxis.set_minor_locator(MultipleLocator(0.25))
axes.yaxis.set_major_locator(MultipleLocator(0.5))
axes.grid(color = "blue", which = "both", linestyle = ':', linewidth = 0.5)

charging_time = times[max_voltage_index] - times[0]
discharging_time = times[-1] - times[max_voltage_index]

axes.axvline(x = charging_time, ymin=y_limits[0], ymax = max_voltage/y_limits[1], color = 'green', linestyle='dashed')
axes.axhline(y = max_voltage, xmin=x_limits[0], xmax = charging_time/x_limits[1], color = 'green', linestyle='dashed')

axes.scatter(times[max_voltage_index], max_voltage, color='green')

axes.scatter(x = charging_time, y = 0.0, color='green')
axes.text(x=charging_time+0.1, y = 0.05, s=str(round(charging_time, 2)), fontsize = 12)

axes.scatter(x = 0.0, y = max_voltage, color = 'green')
axes.text(x = 0.1, y = max_voltage+0.05, s = str(round(max_voltage, 2)), fontsize = 12)

axes.text(x = (charging_time/2-0.8), y = max_voltage/2, s = ("Charging time: " + str(round(charging_time, 2)) + " s"), color = 'blue', fontsize = 14)
axes.text(x = (charging_time+discharging_time/2-0.8), y = max_voltage/2, s = ("Discharging time: " + str(round(discharging_time, 2)) + " s"), color = 'red', fontsize = 14)

figure.savefig("circuit_graph.svg")
#!/bin/python3
import matplotlib.pyplot as plt
import numpy


month_map = ["Jan", "Feb", "Mar", "Apr","May","Jun", "Jul", "Aug", "Sep","Oct","Nov","Dec"]
temperatures = []
years = []
min_temps = []
mean_temps = []
max_temps = []

line_count = 0
with open ("monthly_weather.txt") as file:
  for line in file:
    if line:
      # All element parsed
      elements = line.split()
      years.append(int(elements.pop(0)))
      num_elements = [eval(i) for i in elements]
      min_temps.append(numpy.min(num_elements))
      mean_temps.append(numpy.mean(num_elements))
      max_temps.append(numpy.max(num_elements))
      line_count += 1
      # if line_count > 20:
      #   break
      
t_years = tuple(years)
year_stats = {
  "min": tuple(min_temps),
  "mean": tuple(mean_temps),
  "max": tuple(max_temps)
}
x = numpy.arange(len(t_years))
width = 0.25
multiplier = 0

fig, ax = plt.subplots(layout='constrained')

for attribute, measurement in year_stats.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    # ax.bar_label(rects, padding=3)
    multiplier += 1

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Temperature (f)')
ax.set_title('Temperature Statistics')
ax.set_xticks(x + width, t_years)
ax.legend(loc='upper left')
ax.set_ylim(0, 100)
plt.show()
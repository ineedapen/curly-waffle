#!/usr/bin/env python

import psutil

# Get the total RAM and free RAM in bytes
total_ram = psutil.virtual_memory().total
free_ram = psutil.virtual_memory().available

# Calculate the RAM usage percentage
ram_usage = (total_ram - free_ram) * 100 / total_ram

# Print the RAM usage
print(f"RAM usage: {ram_usage:.2f}%")

# Check if RAM usage is more than 90% and print an alert if it is
if ram_usage > 90:
    print("RAM usage is more than 90%! Alert!")

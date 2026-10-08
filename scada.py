# SCADA Simulation using Python

import random
import time

print("===== SCADA SYSTEM =====")

for i in range(5):

    temperature = random.randint(20, 100)
    pressure = random.randint(10, 50)
    motor = random.choice(["ON", "OFF"])

    print("\n--- Sensor Data ---")
    print("Temperature :", temperature, "°C")
    print("Pressure    :", pressure, "bar")
    print("Motor       :", motor)

    # Alarm conditions
    if temperature > 80:
        print("ALARM: High Temperature!")

    if pressure > 40:
        print("ALARM: High Pressure!")

    if temperature <= 80 and pressure <= 40:
        print("System Status: NORMAL")

    time.sleep(1)

print("\nSCADA Monitoring Completed.")

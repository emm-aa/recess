# x = [0, 2, 4, 8, 10]
# y = [0, 4, 8, 16, 36]

# fig, ax = plt.subplots()
# ax.plot(x, y, marker="o", label="Data Points")

# ax.set_title("Basic Line graph ")
# ax.set_xlabel("x-Axis")
# ax.set_ylabel("Y-Axis")

# ax.legend()


# Simple bar graph
# x = [0, 2, 4, 8, 10]
# y = [0, 4, 8, 16, 36]


# plt.bar(x, y, label="Data Points", color="green")
# plt.xlabel("Multiple of 2")
# plt.ylabel("Multiple of 4")
# plt.title("Simple Bar Graph")
# plt.legend()
# plt.show()


# days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
# temperatures = [68, 72, 75, 71, 74]


# plt.plot(days, temperatures, label="Avg Temp", marker="o")

# plt.title("Weekly Temperatures")
# plt.xlabel("Day of the Week")
# plt.ylabel("Temperature (°F)")
# plt.legend()

import matplotlib.pyplot as plt

ages = [22, 24, 22, 28, 34, 26, 24, 30, 22, 29, 28, 31, 38, 36, 25, 23, 24]
plt.hist(ages, bins=5, edgecolor="black")

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

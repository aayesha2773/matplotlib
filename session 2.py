
import matplotlib.pyplot as plt
import numpy as np

#task 1
'''
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
steps = [3000, 4500, 6000, 5000, 7500, 9000, 8000]


plt.plot(days, steps, color="green", linewidth=2, marker="o")

plt.title("Daily Steps Over 7 Days")
plt.xlabel("Days of the Week")
plt.ylabel("Number of Steps")
plt.grid(True)
plt.show()
'''

#task 2
'''
months = ["January", "February", "March", "April", "May", "June"]


users = [600, 615, 630, 650, 670, 690]

plt.plot(
    months,
    users,
    marker="o",
    markerfacecolor="red",
    color="blue",
    linewidth=2
)


plt.title("Youtube Music Monthly Active Users")
plt.xlabel("Month")
plt.ylabel("Active Users (Millions)")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

'''

#task-3
'''
months = ["May", "June", "July", "August", "September"]


zomato_orders = [8, 10, 7, 12, 15]
swiggy_orders = [6, 9, 11, 8, 13]

plt.plot(
    months,
    zomato_orders,
    color="red",
    linestyle="-",
    marker="o",
    linewidth=2,
    label="Zomato"
)

plt.plot(
    months,
    swiggy_orders,
    color="orange",
    linestyle="--",
    marker="s",
    linewidth=2,
    label="Swiggy"
)

plt.title("Monthly Food Orders: Zomato vs Swiggy")
plt.xlabel("Month")
plt.ylabel("Number of Orders")
plt.legend()
plt.grid(True, alpha=0.5)

plt.tight_layout()
plt.show()

'''

#task-4 

months = ["May", "June", "July", "August", "September", "October"]
data_used = [12, 15, 10, 18, 20, 16]

plt.plot(months, data_used, marker="o", color="blue", linewidth=2)

plt.title("Monthly Data Usage Trend")
plt.xlabel("Month")
plt.ylabel("Data Used (GB)")
plt.grid(True)
plt.show()


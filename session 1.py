import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


#task 1

'''
# Number of daily steps walked over a week
days = ["Monday", "Tuesday", "Wednesday", "Thursday",
        "Friday", "Saturday", "Sunday"]

steps = [3000, 4500, 6000, 5000, 7500, 9000, 8000]

# line plot
plt.plot(days, steps, marker="o", label="Daily Steps")
plt.title("My Daily Steps Over 7 Days")
plt.xlabel("Days of the Week")
plt.ylabel("Number of Steps")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)


plt.tight_layout()
plt.show()
'''

#task 2

'''
posts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
likes = [120, 150, 180, 140, 220, 200, 280, 250, 320, 400]

plt.plot(posts, likes, marker="o", label="Instagram Likes")
plt.title("Likes Received on My Last 10 Instagram Posts")
plt.xlabel("Instagram Post Number")
plt.ylabel("Number of Likes")
plt.grid(True)
plt.legend()
plt.show()
'''

#task 3


import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

spotify_hours = [2, 1.5, 3, 2.5, 4, 5, 3.5]
youtube_hours = [1, 2, 1.5, 2, 3, 4, 2.5]

fig, ax = plt.subplots(1, 2, figsize=(12, 5))

# First plot: Spotify
ax[0].plot(days, spotify_hours, marker="o", color="green")
ax[0].set_title("Daily Spotify Listening Hours")
ax[0].set_xlabel("Days of the Week")
ax[0].set_ylabel("Listening Hours")
ax[0].grid(True)

# Second plot: YouTube 
ax[1].plot(days, youtube_hours, marker="o", color="red")
ax[1].set_title("Daily YouTube Viewing Hours")
ax[1].set_xlabel("Days of the Week")
ax[1].set_ylabel("Viewing Hours")
ax[1].grid(True)

plt.tight_layout()
plt.show()

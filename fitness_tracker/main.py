import pandas as pd
import matplotlib.pyplot as plt

# Sample data: Day, Steps, Calories burned, Distance (in km)
data = {
    "Day": ["2024-12-01", "2024-12-02", "2024-12-03", "2024-12-04", "2024-12-05"],
    "Steps": [5000, 6000, 7500, 4000, 8000],
    "Calories": [900, 240, 300, 160, 320],
    "Distance": [3.5, 4.0, 5.0, 2.8, 5.6],   # in kilometers
    "Active_Minutes": [35, 40, 50, 28, 56],  # in minutes
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Convert 'Day' column to datetime for better handling
df["Day"] = pd.to_datetime(df["Day"])

# Calculate basic statistics
total_steps = df["Steps"].sum()
avg_steps = df["Steps"].mean()
total_calories = df["Calories"].sum()
avg_calories = df["Calories"].mean()
total_distance = df["Distance"].sum()
avg_distance = df["Distance"].mean()
total_activemin = df["Active_Minutes"].sum()
avg_activemin = df["Active_Minutes"].mean()

# Print basic statistics
print(f"Total steps: {total_steps}")
print(f"Average steps per day: {avg_steps}")
print(f"Total calories burned: {total_calories}")
print(f"Average calories burned per day: {avg_calories}")
print(f"Total distance traveled: {total_distance} km")
print(f"Average distance per day: {avg_distance} km")
print(f"Total Active Minutes: {total_activemin} min")
print(f"Average Active Minutes: {avg_activemin} min")
# Plotting the data
plt.figure(figsize=(10, 6))

# Steps plot
plt.subplot(2, 2, 1)
plt.plot(df["Day"], df["Steps"], marker='o', color='b', label='Steps')
plt.title("Steps Over Time")
plt.xlabel("Day")
plt.ylabel("Steps")

# Calories plot
plt.subplot(2, 2, 2)
plt.plot(df["Day"], df["Calories"], marker='o', color='r', label='Calories')
plt.title("Calories Burned Over Time")
plt.xlabel("Day")
plt.ylabel("Calories")

# Distance plot
plt.subplot(2, 2, 3)
plt.plot(df["Day"], df["Distance"], marker='*', color='g', label='Distance')
plt.title("Distance Traveled Over Time")
plt.xlabel("Day")
plt.ylabel("Distance (km)")

# Minutes plot
plt.subplot(2, 2, 4)
plt.plot(df["Day"], df["Active_Minutes"], marker='+', color='m', label='Active_Minutes')
plt.title("The total active minutes spent exercisinge")
plt.xlabel("Day")
plt.ylabel("Active_Minutes (min)")

# Show all plots
plt.tight_layout()
plt.show()

# Save analysis as a CSV file
df.to_csv("fitness_analysis.csv", index=False)

# Saving basic stats to a text file
with open("fitness_analysis_report.txt", "w") as f:
    f.write(f"Total steps: {total_steps}\n")
    f.write(f"Average steps per day: {avg_steps}\n")
    f.write(f"Total calories burned: {total_calories}\n")
    f.write(f"Average calories burned per day: {avg_calories}\n")
    f.write(f"Total distance traveled: {total_distance} km\n")
    f.write(f"Average distance per day: {avg_distance} km\n")
    f.write(f"Total Active Minutes: {total_activemin} min\n")
    f.write(f"Average Active Minutes: {avg_activemin} min\n")


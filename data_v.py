# import tkinter as tk

# root = tk.Tk()


# C = tk.Canvas(root, height=500, width=400, bd=1.5, bg='white')
# C.pack()


# C.create_arc(50, 50, 200, 150, start=0, extent=180, fill='yellow', outline='black', width=2)

# root.mainloop()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generate sample data
np.random.seed(42)
data = {
    'Player': [f'Player {i+1}' for i in range(30)],
    'Batting Avg': np.random.uniform(20, 60, 30),
    'Bowling Avg': np.random.uniform(20, 50, 30),
    'Fielding Catches': np.random.randint(0, 10, 30),
    'Result': np.random.choice(['Win', 'Loss', 'Draw'], 30)
}

# Create DataFrame
df = pd.DataFrame(data)

# Set seaborn theme for better visuals
sns.set_theme()

# 1. Bar Chart - Batting Average of Players
plt.figure(figsize=(12, 6))
sns.barplot(data=df, x='Player', y='Batting Avg', palette='viridis')
plt.title('Batting Average of Players')
plt.xticks(rotation=90)
plt.xlabel('Player')
plt.ylabel('Batting Average')
plt.show()

# 2. Bar Chart - Bowling Average of Players
plt.figure(figsize=(12, 6))
sns.barplot(data=df, x='Player', y='Bowling Avg', palette='coolwarm')
plt.title('Bowling Average of Players')
plt.xticks(rotation=90)
plt.xlabel('Player')
plt.ylabel('Bowling Average')
plt.show()

# 3. Bar Chart - Fielding Catches by Players
plt.figure(figsize=(12, 6))
sns.barplot(data=df, x='Player', y='Fielding Catches', palette='magma')
plt.title('Fielding Catches by Players')
plt.xticks(rotation=90)
plt.xlabel('Player')
plt.ylabel('Fielding Catches')
plt.show()

# 4. Pie Chart - Match Result Distribution
plt.figure(figsize=(8, 8))
df['Result'].value_counts().plot.pie(autopct='%1.1f%%', colors=['#4daf4a', '#e41a1c', '#377eb8'])
plt.title('Match Result Distribution')
plt.ylabel('')
plt.show()

# 5. Box Plot - Batting and Bowling Averages Comparison
plt.figure(figsize=(10, 6))
sns.boxplot(data=df[['Batting Avg', 'Bowling Avg']])
plt.title('Batting and Bowling Averages Distribution')
plt.xlabel('Stat Type')
plt.ylabel('Average')
plt.show()

# 6. Count Plot - Result Count
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Result', palette='pastel')
plt.title('Count of Wins, Losses, and Draws')
plt.xlabel('Match Result')
plt.ylabel('Count')
plt.show()


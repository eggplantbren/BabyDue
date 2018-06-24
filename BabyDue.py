import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Load the data
data = pd.read_csv("data.csv")

# Extract two columns and change units
weeks = data.iloc[:,0]/7
frac = data.iloc[:,2] / np.sum(data.iloc[:,2])

# Plot
plt.plot(weeks, 100.0*frac, "o-")
plt.xlabel("Weeks")
plt.ylabel("Percentage")
plt.show()


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Script parameters
filename_data    = "../data/michelson.csv"

ext = "eps"

filename_boxplot = "../images/michelson_boxplot." + ext
filename_scatter = "../images/michelson_scatter." + ext
filename_ci      = "../images/michelson_ci." + ext

speed_exact = 299792458e-6 # Exact speed of light, defined by NIST

# Read the data
df       = pd.read_csv(filename_data, header = 5)
m, n     = df.shape

speed_mean   = np.mean(df["speed"])
speed_median = np.median(df["speed"])
speed_max    = np.max(df["speed"])
speed_min    = np.min(df["speed"])

speed_var   = np.var(df["speed"])
speed_sd    = np.sqrt(speed_var)

# Mean
plt.figure()
plt.plot([-0.35, +0.35], [speed_mean, speed_mean], "r--", label = "mean")
plt.plot([-0.35, +0.35], [speed_exact, speed_exact], "k-", label = "exact")
plt.scatter([0] * m, df["speed"], s = 1, label = "measurement")
plt.axis([-1, +1, speed_min * 0.9999, speed_max * 1.0001])

plt.xticks([0], ["Speed of Light"])
plt.ylabel("Millions of Meters per Second")
plt.legend(loc = 0)

plt.savefig(filename_scatter)
plt.close()

# CI
plt.figure()
plt.plot([-0.5, +0.5], [speed_mean - 1.96 * speed_sd, speed_mean - 1.96 * speed_sd], "r-",
         label = "CI"
)
plt.plot([-0.5, +0.5], [speed_mean + 1.96 * speed_sd, speed_mean + 1.96 * speed_sd], "r-")
plt.plot([-0.35, +0.35], [speed_exact, speed_exact], "k-", label = "exact")
plt.scatter([0] * m, df["speed"], s = 1, label = "measurement")
plt.axis([-1, +1, speed_min * 0.9999, speed_max * 1.0001])

plt.xticks([0], ["c"])
plt.ylabel("Millions of Meters per Second")
plt.legend(loc = 0)

plt.savefig(filename_ci)
plt.close()

# Boxplot
plt.figure()

plt.boxplot(df["speed"], labels = ["c"])
plt.ylabel("Millions of Meters per Second")
plt.legend(loc = 0)

plt.savefig(filename_boxplot)
plt.close()

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Script parameters
filename_data    = "../data/michelson.csv"

ext = "eps"

filename_boxplot = "../images/michelson_boxplot." + ext
filename_scatter = "../images/michelson_scatter." + ext
filename_ci      = "../images/michelson_ci." + ext

# Read the data
df       = pd.read_csv(filename_data)
m, n     = df.shape

kps_mean   = np.mean(df["kps_air"])
kps_median = np.median(df["kps_air"])
kps_max    = np.max(df["kps_air"])
kps_min    = np.min(df["kps_air"])

kps_var   = np.var(df["kps_air"])
kps_sd    = np.sqrt(kps_var)

# Mean
plt.figure()
plt.plot([-0.35, +0.35], [kps_mean, kps_mean], "r--", label = "mean")
plt.plot([0] * m, df["kps_air"], "k.")
plt.axis([-1, +1, kps_min * 0.9999, kps_max * 1.0001])
plt.xticks([0], ["c"])

plt.savefig(filename_scatter)
plt.close()

# CI
plt.figure()
plt.plot([-0.5, +0.5], [kps_mean - 1.96 * kps_sd, kps_mean - 1.96 * kps_sd], "r-")
plt.plot([-0.5, +0.5], [kps_mean + 1.96 * kps_sd, kps_mean + 1.96 * kps_sd], "r-")
plt.plot([0] * m, df["kps_air"], "k.")
plt.axis([-1, +1, kps_min * 0.9999, kps_max * 1.0001])
plt.xticks([0], ["c"])

plt.savefig(filename_ci)
plt.close()

# Boxplot
plt.figure()
plt.boxplot(df["kps_air"], labels = ["c"])

plt.savefig(filename_boxplot)
plt.close()

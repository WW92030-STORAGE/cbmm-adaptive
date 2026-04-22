import matplotlib.pyplot as plt
import numpy as np

constant = 0.001        # convert from us to ms
data = np.array([
    [26680.12156, 33497.95999, 34571.75685, 37343.29499], 
    [26846.86908, 32987.02029, 34690.64632, 37170.5913]
]) * constant

stdevs = np.array([
    [219.3694902, 317.2550247, 462.999935, 783.3495378], 
    [734.4577631, 565.8544794, 618.6369083, 272.9870165]
]) * constant

# Put eBPF data inside here
ebpfmode = True
if ebpfmode:
    data = np.array([
        [27609.13304, 37234.98449, 38398.51235, 39051.78857],
        [28933.01627, 36810.94771, 38667.55928, 39748.92288], 
    ]) * constant

    stdevs = np.array([
        [845.1661715, 341.3795039, 533.1284445, 482.3592509], 
        [424.1658662, 276.6968672, 536.38078, 261.8912859]
    ]) * constant

data = data.T
stdevs = stdevs.T

colors = ["#D5E8D4", "#FFE6CC", "#F8CECC", "#CDD9E9", "#F1E6C6", "#DBCFE1"]
edge_colors = ["#82B366", "#D79B00", "#B85450", "#6C8EBF", "#D6B656", "#9673A6"]
hatches = ["/", "x", "|", "\\", "+", "-"]
markers = ["o", "^", "P", "s", "v", "^"]

true_colors = [[colors[2], colors[3]]]
true_hatches = [hatches[0], hatches[3]]
true_edge_colors = [edge_colors[2], edge_colors[3]]

true_colors = colors
true_hatches = hatches
true_edge_colors = edge_colors

# String labels
bars = [
    "CBMM", "MULTIPLICATIVE" if ebpfmode else "DAMO-MULTIPLICATIVE"
]

blobs = [
    "A", "B", "C", "D"
]

num_experiments = data.shape[0]
num_points = data.shape[1]

x = np.arange(num_experiments)
bar_width = 0.15

plt.rcParams["font.size"] = 20
plt.figure()

fig, ax = plt.subplots()

print("NP", num_points)

print(stdevs)

for i in range(num_points):
    offset = (i - num_points / 2) * bar_width + bar_width / 2
    ax.bar(x + offset, data[:, i], width=bar_width, label=bars[i], color = true_colors[i], hatch = true_hatches[i], edgecolor = true_edge_colors[i], yerr = stdevs[:, i], capsize = 4)

# Labels
plt.xlabel('Workload (YCSB mongodb)')
plt.ylabel('Throughput (kOps/s)')
plt.title('')

# plt.ylim(bottom = 20, top = 40)

plt.xticks(x, blobs)
fig.legend(frameon=False, loc="upper center", ncol=2, bbox_to_anchor=(0.5, 0.95)) # Might need to change 1.06
plt.subplots_adjust(top=0.8, bottom=0.2, left=0.2, right=0.95) # Might need to adjust these numbers slightly; don't use tight_layout

plt.savefig("plot.pdf")
plt.savefig("plot.png")
plt.show()
import matplotlib.pyplot as plt
import numpy as np

constant = 0.001

labels = ['CBMM-eBPF', 'Multiplicative', 'CBMM-DAMO', 'DAMO-Mult']

motivation = True
if not motivation:
    data = np.array([269051.625, 266279.625, 260684.875, 255950.5]) * constant
    stdevs = np.array([5794.428455, 7279.164884, 7501.768009, 5059.814706]) * constant
else:
    labels = ["0", "-5", "-10", "-20", "-30"]
    data = np.array([264910.75, 264534.75, 259577.25, 263057.125, 266068]) * constant
    stdevs = np.array([10585.70358, 13798.6055, 9852.335978, 10045.88183, 11245.3837]) * constant
colors = ["#D5E8D4", "#FFE6CC", "#F8CECC", "#CDD9E9", "#F1E6C6", "#DBCFE1"]
edge_colors = ["#82B366", "#D79B00", "#B85450", "#6C8EBF", "#D6B656", "#9673A6"]
hatches = ["/", "x", "|", "\\", "+", "-"]
markers = ["o", "^", "P", "s", "v", "^"]

true_colors = colors
true_hatches = hatches
true_edge_colors = edge_colors

plt.bar(labels, data, color = true_colors, edgecolor = edge_colors, yerr = stdevs, capsize = 4)
plt.title('Avg. Runtime (s)')
plt.xlabel('Policy')
plt.ylabel('Runtime')

# plt.ylim(bottom = 200000 * constant, top = 300000 * constant)

plt.show()

plt.savefig("plot.png")
plt.savefig("plot.pdf")
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

out_file = sys.argv[1]
x_label = sys.argv[2]
y_label = sys.argv[3]

Y = []
i = 0
for l in sys.stdin:
    A = l.rstrip().split()
    Y.append(float(A[0]))

width=3
height=1
fig = plt.figure(figsize=(width,height),dpi=300)

ax = fig.add_subplot(1,1,1)

ax.hist(Y, bins=50)
ax.set_xlabel(x_label)
ax.set_ylabel(y_label)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

plt.savefig(out_file,bbox_inches='tight')

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from PIL import Image
from matplotlib.patches import ArrowStyle


def setdata(filename):
    x_list = []
    y_list = []
    fd = open(filename, 'rt') 	# specify appropriate data file here
    for line in fd:
        data = line[:-1].split(' ')
        x_list.append(float(data[0]))
        y_list.append(float(data[1]))
    return x_list, y_list


params = {'text.usetex': True,
          'text.latex.preamble': r'\usepackage{newtxtext,newtxmath}',
          'legend.fontsize': 12, 'axes.labelsize': 12,
          'axes.titlesize': 12, 'xtick.labelsize': 12,
          'ytick.labelsize': 12, 'font.family': 'serif',
          'grid.color': 'k', 'grid.linestyle': ':',
          'grid.linewidth': 0.5,
          }
plt.rcParams.update(params)

fig = plt.figure(figsize=(5, 5))
ax = fig.add_subplot(111)

plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

ax.set_xlabel(r'$a \longrightarrow$', fontsize=14)
ax.set_ylabel(r'$d \longrightarrow $', fontsize=14)
ax.set_xlim([-5, -1])
ax.set_ylim([0.4, 1])
ax.set_aspect('equal', 'datalim')

(x_list, y_list) = setdata('NS1')
ax.plot(x_list, y_list, color='WHITE', linewidth=2)
(x_list, y_list) = setdata('NS2')
ax.plot(x_list, y_list, color='WHITE', linewidth=2)

ax.text(-3.2, 0.58, "$\mathit{NS}+I$", color="White", fontsize="12",
        rotation=40)

ax.grid(c='gainsboro', zorder=2)

xlim = ax.get_xlim()
ylim = ax.get_ylim()

im = Image.open("./inzhang3.png")
ax.imshow(im, extent=[*xlim, *ylim], aspect='auto', resample=None)

pdf = PdfPages('snapshot.pdf')
pdf.savefig(dpi=300)
pdf.close()
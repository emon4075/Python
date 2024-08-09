# -*- coding: utf-8 -*-
"""W3_Learn.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lhpTRI5ZPVxVExGsEFXqNmMeMFkrR5j3
"""

# Version Check
import matplotlib

print(matplotlib.__version__)

#  Simple Plot
import matplotlib.pyplot as plt

x_points = [1, 2, 3, 4]
y_points = [1, 4, 9, 16]
plt.plot(x_points, y_points)
plt.show()

# Plot With Marker
import matplotlib.pyplot as plt

x_points = [1, 2, 3, 4]
y_points = [1, 19, 10, 16]
plt.plot(x_points, y_points, "o")
# plt.plot(x_points,y_points)
plt.show()

# Plot With Only Y Axis
import matplotlib.pyplot as plt

y_axis = [9, 4, 1, 0]
plt.plot(y_axis)
plt.show()

# Plot With Formatted String
import matplotlib.pyplot as plt

y_axis = [9, 4, 1, 0]
plt.plot(y_axis, "o-.k", ms=15, mec="r", mfc="c")
plt.show()

# Line Style
from matplotlib import pyplot as plt

y_axis = [1, 3, 9, 2]
# plt.plot(y_axis,linestyle = "dotted")
# plt.plot(y_axis,linestyle = ":")
# plt.plot(y_axis,ls = "dashed")
# plt.plot(y_axis,ls = "-.",color = "m")
# plt.plot(y_axis,ls = "--",color = "m", linewidth = 5)
plt.plot(y_axis, ls="--", color="m", lw=5)
plt.show()

from matplotlib import pyplot as plt

x1 = [1, 2, 3, 4, 5]
y1 = [1, 3, 6, 8, 1]
y2 = [0, 1, 0, 2, 7]
x2 = [5, 4, 3, 2, 1]
y3 = [0, 1, 0, 4, 7]
x3 = [5, 4, 2, 1, 1]
plt.plot(
    x1, y1, x2, y2, x3, y3, lw=2, ls=":", marker="o", markersize=10, mec="k", mfc="c"
)
plt.show()

# Labels
from matplotlib import pyplot as plt

x1 = [1, 2, 3, 4, 5, 6, 7, 9]
y1 = [0, 2, 1, 4, 5, 3, 2, 0]
plt.plot(x1, y1, marker="o", mfc="k")
plt.xlabel("Price", fontsize=12)
plt.ylabel("Increase", fontsize=12)
# plt.title("Laptop Price",fontsize=20)
# plt.title("Laptop Price",fontsize=20,loc="right")
plt.show()

# Labels With Grid Lines
from matplotlib import pyplot as plt

x1 = [1, 2, 3, 4, 5, 6, 7, 9]
y1 = [0, 2, 1, 4, 5, 3, 2, 0]
plt.plot(x1, y1, marker="o", mfc="k")
plt.xlabel("Price", fontsize=12)
plt.ylabel("Increase", fontsize=12)
# plt.title("Laptop Price",fontsize=20)
# plt.title("Laptop Price",fontsize=20,loc="right")
# plt.grid()
# plt.grid(axis="x")
plt.grid(axis="y", linewidth=0.5, color="m", ls="-.")
plt.show()

from matplotlib import pyplot as plt

x1 = [1, 2, 3, 4, 5]
y1 = [0, 2, 5, 2, 1]
x2 = [1, 2, 3, 4, 5]
y2 = [0, 2, 5, 2, 1]

plt.subplot(2, 2, 1)
plt.plot(x1, y1, marker="X")
plt.grid(axis="y", lw=1, color="m", ls=":")
# plt.title("Sports")

plt.subplot(2, 2, 2)
plt.plot(x2, y2, marker="o", mec="k", mfc="y")
plt.grid(axis="y", color="b", ls="-.", lw=1)
# plt.title("Swimming")

plt.suptitle("Data Sets")
plt.show()

# Scatter With Coloring Every Point Indivisually
from matplotlib import pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [1, 2, 3, 4, 5, 6, 7, 8]
co = ["red", "green", "blue", "cyan", "magenta", "yellow", "black", "orange"]
plt.scatter(x, y, c=co)
plt.show()

# Scatter
from matplotlib import pyplot as plt

x1 = [1, 2, 3, 4, 5]
y1 = [0, 1, 5, 2, 5]
x2 = [1, 2, 3, 4, 5]
y2 = [0, 2, 5, 2, 1]
color = ["hotpink", "yellow", "cyan", "magenta", "green"]
# First One
plt.subplot(1, 2, 1)
plt.scatter(x1, y1, c="cyan")
plt.title("First")


# Second One
plt.subplot(1, 2, 2)
plt.scatter(x2, y2, c=color)
plt.title("Second")


# Final
plt.suptitle("Data Sets")
plt.show()

# Scatter
from matplotlib import pyplot as plt
from random import uniform as U

x1 = [1, 2, 3, 4, 5]
y1 = [0, 1, 5, 2, 5]
x2 = [1, 2, 3, 4, 5]
y2 = [0, 2, 5, 2, 1]
color = ["hotpink", "yellow", "cyan", "magenta", "green"]
sizes = [100, 200, 300, 400, 500]
a = U(0, 1)
# First One
plt.subplot(1, 2, 1)
plt.scatter(x1, y1, c="cyan", s=sizes, alpha=a)
plt.title("First")


# Second One
plt.subplot(1, 2, 2)
plt.scatter(x2, y2, c=color, alpha=a)
plt.title("Second")


# Final
plt.suptitle("Data Sets")
plt.show()

# Bars
from matplotlib import pyplot as plt

x = ["A", "B", "C", "D", "E"]
y = [1, 2, 3, 4, 2]
col = ["magenta", "yellow", "green", "red", "cyan"]
plt.bar(x, y, color=col, width=0.5)
plt.title("Bar", loc="left")
plt.xlabel("Letters")
plt.ylabel("Numbers")
plt.show()

# Horizontal Bars
from matplotlib import pyplot as plt

x = ["A", "B", "C", "D", "E"]
y = [1, 2, 3, 4, 2]
col = ["magenta", "yellow", "green", "red", "cyan"]
plt.barh(x, y, color=col, height=0.5)
plt.title("Bar", loc="left")
plt.xlabel("Letters")
plt.ylabel("Numbers")
plt.show()

# Histogram
from matplotlib import pyplot as plt

ages = [
    59,
    51,
    40,
    48,
    66,
    61,
    45,
    41,
    59,
    51,
    58,
    50,
    56,
    60,
    63,
    66,
    40,
    47,
    53,
    49,
    63,
    51,
    45,
    70,
    42,
    48,
    60,
    64,
    68,
    63,
    70,
    69,
    47,
    42,
    64,
    61,
    64,
    49,
    54,
    59,
    59,
    58,
    68,
    55,
    51,
    49,
    60,
    49,
    51,
    46,
    60,
    64,
    49,
    67,
    50,
    65,
    65,
    41,
    67,
    45,
    64,
    52,
    46,
    44,
    45,
    51,
    56,
    52,
    70,
    66,
    56,
    40,
    70,
    47,
    44,
    61,
    41,
    58,
    56,
    41,
    65,
    41,
    68,
    65,
    47,
    48,
    49,
    62,
    70,
    44,
    43,
    47,
    47,
    64,
    44,
    65,
    49,
    49,
    59,
    58,
]
plt.hist(ages, color="hotpink")
plt.title("Histogram")
plt.xlabel("Ages")
plt.ylabel("Frequency")
plt.show()

# Basic Pie
from matplotlib import pyplot as plt

y = [20, 85, 90, 23, 1]
mylabels = ["Apple", "Banana", "Grapes", "Weed", "Tobacco"]
# plt.pie(y,labels = mylabels,startangle = 90)
plt.pie(y, labels=mylabels)
plt.show()

# Pie
from matplotlib import pyplot as plt

y = [20, 85, 90, 23, 10]
mylabels = ["Apple", "Banana", "Grapes", "Weed", "Tobacco"]
myexplode = [0, 0.2, 0.4, 0, 0]
mycolors = ["black", "blue", "cyan", "magenta", "green"]
plt.pie(y, labels=mylabels, explode=myexplode, shadow=True, colors=mycolors)
plt.legend(title="Fruits")
plt.show()

import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
def update_lines(num, dataLines, lines):
    for line, data in zip(lines, dataLines):
        line.set_data(data[0:2, :num])
        line.set_3d_properties(data[2, :num])
    return lines
fig = plt.figure()
ax = p3.Axes3D(fig)
data = []
from oribitals import sys
for obj in sys:
    data.append(np.array([obj.x, obj.y, obj.z]))
lines = [ax.plot(dat[0, 0:1], dat[1, 0:1], dat[2, 0:1])[0] for dat in data]
ax.set_xlim3d([-1.0, 1.0])
ax.set_xlabel('X')
ax.set_ylim3d([-1.0, 1.0])
ax.set_ylabel('Y')
ax.set_zlim3d([-1.0, 1.0])
ax.set_zlabel('Z')
ax.set_title('3D Test')
line_ani = animation.FuncAnimation(fig, update_lines, 500, fargs=(data, lines), interval=10, blit=False)
plt.show()
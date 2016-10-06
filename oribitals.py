#laplacian model
import numpy as np
import math
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
from math import *
t = 0
tInt = 400
c = -900000
sys = []

class OBJ:
	def __init__(self, x, y, z, xv, yv, zv, q, name, m = 1.0):
		self.x = [x]
		self.y = [y]
		self.z = [z]
		self.xv = xv
		self.yv = yv
		self.zv = zv
		self.q = q
		self.m = m
		self.name = name
		sys.append(self)

	def move(self):
		self.x.append(self.x[-1] + self.xv*tInt)
		self.y.append(self.y[-1] + self.yv*tInt)
		self.z.append(self.z[-1] + self.zv*tInt)

	def acc(self):
		for i in sys:
			if i.name != self.name:
				d = sqrt(((self.x[-1]-i.x[-1])**2)+((self.y[-1]-i.y[-1])**2)+((self.z[-1]-i.z[-1])**2))
				mag = (c*self.q*i.q)/(d**2)/self.m
				self.xv += ((i.x[-1] - self.x[-1])/d)*mag
				self.yv += ((i.y[-1] - self.y[-1])/d)*mag
				self.zv += ((i.z[-1] - self.z[-1])/d)*mag

a = OBJ(1.0, 0.0, 0.0, 0.0, 0, 0, -0.0000005, 'a')
b = OBJ(0.0, 1.0, 0.0, 0.0, 0, 0, 0.0000005, 'b')
d = OBJ(0.0, 0.0, 0.5, 0.0, 0, 0, -0.0000005, 'd')
for i in range(10000):
	for j in sys:
		j.move()
		j.acc()
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
line_ani = animation.FuncAnimation(fig, update_lines, 5000, fargs=(data, lines), interval=1, blit=False)
plt.show()

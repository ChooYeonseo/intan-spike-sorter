# In this file we will generate the geometry of the probe and print it as an example
# The Probe we use in link lab is as follows. It is an 8 channel probe.

import numpy as np
from probeinterface import Probe
from probeinterface.plotting import plot_probe

n = 8
positions = np.zeros((n, 2))

L_x = [35,27,43,21,52,18,60,17]
L_y = [20, 100, 180, 260, 340, 400, 480, 560]

assert len(L_x) == n, "number of coordinate doesn't match"
for i, j in enumerate(L_x):
    x = j
    y = 20 + 80*i
    positions[i] = x, y

probe = Probe(ndim=2, si_units='um')
probe.set_contacts(positions=positions, shapes='square', shape_params={'width': 13}, contact_ids=np.array([8,9,5,10,7,4,6,3]))

print(probe)

polygon = [(0, 700), (0, 566), (10, 180), (23, 20), (35, 0),(47, 20), (60, 180), (83, 566), (83, 700)]
probe.set_planar_contour(polygon)
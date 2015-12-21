# -----------------------------------------------------------------------------
# Copyright (c) 2011-2016, Nicolas P. Rougier.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------
import numpy as np
from glumpy import app
from glumpy.graphics.collections import PointCollection
from glumpy.transforms import PolarProjection, Position

window = app.Window(1024,1024, color=(1,1,1,1))

@window.event
def on_draw(dt):
    window.clear()
    points.draw()

transform = Position(PolarProjection())
points = PointCollection("agg", transform = transform)

n = 10000
R = np.random.uniform(0.2,0.8,n)
T = np.random.uniform(0,2*np.pi,n)
Z = np.zeros(n)

points.append (np.dstack((R,T,Z)).reshape(n,3) )
window.attach(points["transform"])
window.attach(points["viewport"])
app.run()

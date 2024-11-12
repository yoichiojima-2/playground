# Create a mandelbrot fractal image and display it

import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

def mandelbrot_set(width, height, xmin, xmax, ymin, ymax, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    return (r1, r2, np.array([[mandelbrot(complex(r, i), max_iter) for r in r1] for i in r2]))

width, height = 800, 800
xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
max_iter = 255

r1, r2, mandelbrot_set = mandelbrot_set(width, height, xmin, xmax, ymin, ymax, max_iter)

plt.figure(figsize=(12, 12))
plt.imshow(mandelbrot_set.T, extent=(xmin, xmax, ymin, ymax))
plt.axis('off')
plt.show()

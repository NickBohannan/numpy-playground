import os
import imageio
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage

DIR = "tutorial-x-ray-image-processing"

xray_image = imageio.v3.imread(os.path.join(DIR, "00000011_001.png"))

#############################
# Laplacian-Gaussian Filter #
#############################

xray_image_laplace_gaussian = ndimage.gaussian_laplace(xray_image, sigma=1)

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 10))

axes[0].set_title("Original")
axes[0].imshow(xray_image, cmap="gray")
axes[1].set_title("Laplacian-Gaussian (edges)")
axes[1].imshow(xray_image_laplace_gaussian, cmap="gray")
for i in axes:
    i.axis("off")
plt.show()

####################################
# Gradient Magnitude (POP, POP!!!) #
####################################

x_ray_image_gaussian_gradient = ndimage.gaussian_gradient_magnitude(
    xray_image, sigma=2)

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 10))

axes[0].set_title("Original")
axes[0].imshow(xray_image, cmap="gray")
axes[1].set_title("Gaussian gradient (edges)")
axes[1].imshow(x_ray_image_gaussian_gradient, cmap="gray")
for i in axes:
    i.axis("off")
plt.show()

import os
import imageio
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage

DIR = "tutorial-x-ray-image-processing"

xray_image = imageio.v3.imread(os.path.join(DIR, "00000011_001.png"))

plt.imshow(xray_image, cmap="gray")
plt.axis("off")
plt.show()

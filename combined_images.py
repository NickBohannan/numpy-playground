import os
import imageio
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage

DIR = "tutorial-x-ray-image-processing"

num_imgs = 9

combined_xray_images_1 = np.array(
    [imageio.v3.imread(os.path.join(
        DIR, f"00000011_00{i}.png")) for i in range(num_imgs)]
)

fig, axes = plt.subplots(nrows=1, ncols=num_imgs, figsize=(30, 30))

for img, ax in zip(combined_xray_images_1, axes):
    ax.imshow(img, cmap='gray')
    ax.axis('off')

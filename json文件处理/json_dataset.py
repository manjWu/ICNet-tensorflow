import numpy as np
import matplotlib.pyplot as plt
import PIL.Image

label_file = '/Users/wumanjia/Desktop/1/IMG_7143_json/label.png'
lbl = np.asarray(PIL.Image.open(label_file))
print(np.unique(lbl))
print(lbl.dtype)
# assert lbl.dtype == np.int32

for label_value in np.unique(lbl):
    mask = lbl == label_value
    plt.imshow(mask, cmap='gray')
    plt.show()
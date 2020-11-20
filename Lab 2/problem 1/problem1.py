from PIL import Image
import numpy as np 
from math import sqrt

# считаем картинку в numpy array
img = Image.open("/home/antpotapov2019/lunar_images/lunar03_raw.jpg")
data = np.array(img)
x = data.min()

for i in range(data.shape[0]):
    data[i] = data[i] - x

y = data.max()

for i in range(data.shape[0]):
    data[i] = (255 // y) * data[i]
# запись картинки после обработки
res_img = Image.fromarray(data)
res_img.save("/home/antpotapov2019/lunar_images/lunar03_raw_result.jpg")
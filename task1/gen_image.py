
import math
import random
import numpy as np
import cv2
import matplotlib.pyplot as plt

# Read the image 
# Get image's dimension
# Split read image into channels
test_image = cv2.imread("task1/test_img.jpg")
height, width, channel = test_image.shape
blue, green, red = cv2.split(test_image)

# Random init seed
random.seed()
# Limit the area of artifacts to avoid out of bound
limit_area = math.floor(min(height, width)/10)
# Set the range for the size of the artifacts
maximum_value = math.floor(limit_area*0.6)
minimum_value = math.floor(limit_area*0.4)

for index in range(10):
    x = random.randint(0 + limit_area, width - limit_area)
    y = random.randint(0 + limit_area, height - limit_area)

    random_area = random.randint(minimum_value, maximum_value)

    blue[y-random_area:y + random_area, x-random_area:x +
         random_area] = (blue[y-random_area:y+random_area, x-random_area:x+random_area] + random.randint(50, 150)) % 255
    green[y-random_area:y+random_area, x-random_area:x +
          random_area] = (green[y-random_area:y+random_area, x-random_area:x+random_area] + random.randint(50, 150)) % 255
    red[y-random_area:y+random_area, x-random_area:x +
        random_area] = (red[y-random_area:y+random_area, x-random_area:x+random_area] + random.randint(50, 150)) % 255

# Merge into result image
result_image = cv2.merge([red, green, blue]) 
# Convert the input image RGB for displaying in plot
test_image = cv2.cvtColor(test_image, cv2.COLOR_BGR2RGB) 

# Show the plot
plt.subplot(221), 
plt.imshow(test_image), plt.title('Input')
plt.xticks([]), 
plt.yticks([])
plt.subplot(222), 
plt.imshow(result_image), plt.title('Result')
plt.xticks([]), 
plt.yticks([])
plt.show
plt.waitforbuttonpress(0)
plt.close('all')

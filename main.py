import cv2 as cv
import numpy as np
import random
import imageio

def create_image():
  img = np.zeros([60,200,1], np.uint8)
  return img


def spiced_salt(image):
  height, width, channels = image.shape
  for row in range(height):
    for col in range(width):
      image[row,col] = int(random.random()*2)*255


def move_salt_left(image):
  tmp = image[0:60,0]
  for i in range(0,199):
    image[0:60,i] = image[0:60,i+1]
  image[0:60,199] = tmp


def move_salt_right(image):
  tmp = image[0:60,199]
  for i in range(199,0,-1):
    image[0:60,i] = image[0:60,i-1]
  image[0:60,0] = tmp


def cover_salt(top, shape, image):
  height, width, channels = image.shape
  for row in range(height):
    for col in range(width):
      if (shape[row,col]==[255]):
        image[row,col] = top[row,col]


text = "JjNb"
background = create_image()
topfloor = create_image()
mark = create_image()
spiced_salt(background)
spiced_salt(topfloor)
cv.putText(mark, text, (40, 40), cv.FONT_HERSHEY_COMPLEX_SMALL, 2.0, (255, 255, 255), 2)

frames = []
t1 = cv.getTickCount()

for i in range(0, 200):
  dst = background.copy()
  cover_salt(topfloor, mark, dst)
  move_salt_left(background)
  move_salt_right(topfloor)
  frames.append(dst)

t2 = cv.getTickCount()

imageio.mimsave('result.gif', frames, 'GIF', duration=0.02)
time = (t2-t1)/cv.getTickFrequency()
print("Make successfully\nUsage time:%s ms"%(time*1000))
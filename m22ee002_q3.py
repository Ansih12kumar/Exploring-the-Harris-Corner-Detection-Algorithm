# -*- coding: utf-8 -*-
"""m22ee002_q3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11lBt2pd16VY-3D-ZRYqp7M-_o3L4ioQ3
"""

from google.colab import drive
drive.mount('/content/drive')

path='drive/My Drive/m22ee002_q3'

import cv2
import numpy as np
import matplotlib.pyplot as plt
from google.colab import drive


drive.mount('/content/drive')


F = np.array([[3.34638533e-07, 7.58547151e-06, -2.04147752e-03],
              [-5.83765868e-06, 1.36498636e-06, 2.67566877e-04],
              [1.45892349e-03, -4.37648316e-03, 1.0]])


img1path = '/content/drive/My Drive/m22ee002_q3/000000.png'
img2path = '/content/drive/My Drive/m22ee002_q3/000023.png'
img1 = cv2.imread(img1path, cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(img2path, cv2.IMREAD_GRAYSCALE)


def compepipolarlines(F, pts, which_image):
    if which_image == 1:
        return np.dot(F, np.concatenate([pts, np.ones((pts.shape[0], 1))], axis=1).T).T
    elif which_image == 2:
        return np.dot(F.T, np.concatenate([pts, np.ones((pts.shape[0], 1))], axis=1).T).T


pts1 = np.array([(0, 0)])
lines1 = compepipolarlines(F, pts1, which_image=1)


pts2 = np.array([(0, 0)])
lines2 = compepipolarlines(F, pts2, which_image=2)


def draw_epipol_lines(img, lines, color=(0, 255, 0), thickness=2):
    for r in lines:
        x0, y0 = map(int, [0, -r[2] / r[1]])
        x1, y1 = map(int, [img.shape[1], -(r[2] + r[0] * img.shape[1]) / r[1]])
        img = cv2.line(img, (x0, y0), (x1, y1), color, thickness)
    return img


img1_lines = draw_epipol_lines(cv2.cvtColor(img1, cv2.COLOR_GRAY2BGR), lines1, thickness=4)

img2_lines = draw_epipol_lines(cv2.cvtColor(img2, cv2.COLOR_GRAY2BGR), lines2, thickness=4)


fig, axes = plt.subplots(1, 2, figsize=(20, 10))
axes[0].imshow(cv2.cvtColor(img1_lines, cv2.COLOR_BGR2RGB))
axes[0].axis('off')
axes[0].set_title('Image 1 with epipolar lines')

axes[1].imshow(cv2.cvtColor(img2_lines, cv2.COLOR_BGR2RGB))
axes[1].axis('off')
axes[1].set_title('Image 2 with epipolar lines')

plt.show()

import cv2

img1 = cv2.imread('/content/drive/My Drive/m22ee002_q3/000000.png', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('/content/drive/My Drive/m22ee002_q3/000023.png', cv2.IMREAD_GRAYSCALE)

img1height, img1width = img1.shape[:2]
print("Image 1 size: {}x{}".format(img1width, img1height))


img2height, img2width = img2.shape[:2]
print("Image 2 size: {}x{}".format(img2width, img2height))

import cv2
import numpy as np
from google.colab import drive


drive.mount('/content/drive')


F = np.array([[3.34638533e-07, 7.58547151e-06, -2.04147752e-03],
              [-5.83765868e-06, 1.36498636e-06, 2.67566877e-04],
              [1.45892349e-03, -4.37648316e-03, 1.0]])


img1path = '/content/drive/My Drive/m22ee002_q3/000000.png'
img2path = '/content/drive/My Drive/m22ee002_q3/000023.png'
img1 = cv2.imread(img1path, cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(img2path, cv2.IMREAD_GRAYSCALE)


def comp_epipol_lines(F, pts, which_image):
    if which_image == 1:
        return np.dot(F, np.concatenate([pts, np.ones((pts.shape[0], 1))], axis=1).T).T
    elif which_image == 2:
        return np.dot(F.T, np.concatenate([pts, np.ones((pts.shape[0], 1))], axis=1).T).T


pts1 = np.array([(0, 0)])
lines1 = comp_epipol_lines(F, pts1, which_image=1)


pts2 = np.array([(0, 0)])
lines2 = comp_epipol_lines(F, pts2, which_image=2)


def sampl_points_on_line(line, img_shape):
    sampled_points = []
    x0, y0 = map(int, [0, -line[2] / line[1]])
    x1, y1 = map(int, [img_shape[1], -(line[2] + line[0] * img_shape[1]) / line[1]])
    length = np.sqrt((x1 - x0)**2 + (y1 - y0)**2)
    for x in range(0, img_shape[1], 10):
        y = int((y1 - y0) / (x1 - x0) * x + y0)
        if 0 <= x < img_shape[1] and 0 <= y < img_shape[0]:

            if np.abs(line[0] * x + line[1] * y + line[2]) < 1:
                sampled_points.append((x, y))
    return sampled_points


correspondingpoints1 = [sampl_points_on_line(line, img1.shape) for line in lines1]


correspondingpoints2 = [sampl_points_on_line(line, img2.shape) for line in lines2]

print("Corresponding points on epipolar lines in the first image:")
print(correspondingpoints1)
print("\nCorresponding points on epipolar lines in the second image:")
print(correspondingpoints2)

import cv2
import numpy as np
from google.colab import drive
import matplotlib.pyplot as plt


drive.mount('/content/drive')


F = np.array([[3.34638533e-07, 7.58547151e-06, -2.04147752e-03],
              [-5.83765868e-06, 1.36498636e-06, 2.67566877e-04],
              [1.45892349e-03, -4.37648316e-03, 1.0]])


img1_path = '/content/drive/My Drive/m22ee002_q3/000000.png'
img2_path = '/content/drive/My Drive/m22ee002_q3/000023.png'
img1 = cv2.imread(img1_path, cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(img2_path, cv2.IMREAD_GRAYSCALE)


def comp_epipol_lines(F, pts, which_image):
    if which_image == 1:
        return np.dot(F, np.concatenate([pts, np.ones((pts.shape[0], 1))], axis=1).T).T
    elif which_image == 2:
        return np.dot(F.T, np.concatenate([pts, np.ones((pts.shape[0], 1))], axis=1).T).T


pts1 = np.array([(0, 0)])
lines1 = comp_epipol_lines(F, pts1, which_image=1)

pts2 = np.array([(0, 0)])
lines2 = comp_epipol_lines(F, pts2, which_image=2)


def sampl_points_on_line(line, img_shape):
    sampled_points = []
    x0, y0 = map(int, [0, -line[2] / line[1]])
    x1, y1 = map(int, [img_shape[1], -(line[2] + line[0] * img_shape[1]) / line[1]])
    length = np.sqrt((x1 - x0)**2 + (y1 - y0)**2)
    for x in range(0, img_shape[1], 10):
        y = int((y1 - y0) / (x1 - x0) * x + y0)
        if 0 <= x < img_shape[1] and 0 <= y < img_shape[0]:
            # Ensure point lies on the epipolar line
            if np.abs(line[0] * x + line[1] * y + line[2]) < 1:
                sampled_points.append((x, y))
    return sampled_points


correspondingpoints1 = [sampl_points_on_line(line, img1.shape) for line in lines1]


correspondingpoints2 = [sampl_points_on_line(line, img2.shape) for line in lines2]


img1_with_lines = cv2.cvtColor(img1, cv2.COLOR_GRAY2BGR)
for points, line in zip(correspondingpoints2, lines1):
    color = tuple(np.random.randint(0, 255, 3).tolist())
    for point in points:
        img1_with_lines = cv2.circle(img1_with_lines, tuple(point), 5, color, -1)
    img1_with_lines = cv2.line(img1_with_lines, (0, int(-line[2]/line[1])), (img1.shape[1], int(-(line[2] + line[0]*img1.shape[1])/line[1])), color, 1)


img2_with_lines = cv2.cvtColor(img2, cv2.COLOR_GRAY2BGR)
for points, line in zip(correspondingpoints1, lines2):
    color = tuple(np.random.randint(0, 255, 3).tolist())
    for point in points:
        img2_with_lines = cv2.circle(img2_with_lines, tuple(point), 5, color, -1)
    img2_with_lines = cv2.line(img2_with_lines, (0, int(-line[2]/line[1])), (img2.shape[1], int(-(line[2] + line[0]*img2.shape[1])/line[1])), color, 1)


plt.figure(figsize=(16, 6))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img1_with_lines, cv2.COLOR_BGR2RGB))
plt.title('Image 1 with Epipolar Lines and Corresponding Points')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(img2_with_lines, cv2.COLOR_BGR2RGB))
plt.title('Image 2 with Epipolar Lines and Corresponding Points')
plt.axis('off')

plt.show()

import cv2
import numpy as np
from google.colab import drive
import matplotlib.pyplot as plt


drive.mount('/content/drive')


F = np.array([[3.34638533e-07, 7.58547151e-06, -2.04147752e-03],
              [-5.83765868e-06, 1.36498636e-06, 2.67566877e-04],
              [1.45892349e-03, -4.37648316e-03, 1.0]])


img1_path = '/content/drive/My Drive/m22ee002_q3/000000.png'
img2_path = '/content/drive/My Drive/m22ee002_q3/000023.png'
img1 = cv2.imread(img1path, cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(img2path, cv2.IMREAD_GRAYSCALE)

def comp_epipol_lines(F, pts, which_image):
    if which_image == 1:
        return np.dot(F, np.concatenate([pts, np.ones((pts.shape[0], 1))], axis=1).T).T
    elif which_image == 2:
        return np.dot(F.T, np.concatenate([pts, np.ones((pts.shape[0], 1))], axis=1).T).T


pts1 = np.array([(0, 0)])
lines1 = comp_epipol_lines(F, pts1, which_image=1)


pts2 = np.array([(0, 0)])
lines2 = comp_epipol_lines(F, pts2, which_image=2)


def sampl_points_on_line(line, img_shape):
    sampled_points = []
    x0, y0 = map(int, [0, -line[2] / line[1]])
    x1, y1 = map(int, [img_shape[1], -(line[2] + line[0] * img_shape[1]) / line[1]])
    length = np.sqrt((x1 - x0)**2 + (y1 - y0)**2)
    for x in range(0, img_shape[1], 10):
        y = int((y1 - y0) / (x1 - x0) * x + y0)
        if 0 <= x < img_shape[1] and 0 <= y < img_shape[0]:

            if np.abs(line[0] * x + line[1] * y + line[2]) < 1:
                sampled_points.append((x, y))
    return sampled_points


correspondingpoints1_to_2 = [sampl_points_on_line(line, img1.shape) for line in lines1]


correspondingpoints2_to_1 = [sampl_points_on_line(line, img2.shape) for line in lines2]


for points1, points2 in zip(correspondingpoints1_to_2, correspondingpoints2_to_1):
    for pt1, pt2 in zip(points1, points2):
        cv2.line(img1, pt1, pt2, (255, 0, 0), thickness=2, lineType=cv2.LINE_AA)
        cv2.line(img2, pt2, pt1, (255, 0, 0), thickness=2, lineType=cv2.LINE_AA)


img1 = cv2.cvtColor(img1, cv2.COLOR_GRAY2BGR)
img2 = cv2.cvtColor(img2, cv2.COLOR_GRAY2BGR)


combined_img = np.hstack((img1, img2))

plt.figure(figsize=(12, 6))
plt.imshow(combined_img)
plt.title('Corresponding Points Connected with Lines')
plt.axis('off')
plt.show()

import cv2
import numpy as np
from google.colab import drive
import matplotlib.pyplot as plt

drive.mount('/content/drive')


F = np.array([[3.34638533e-07, 7.58547151e-06, -2.04147752e-03],
              [-5.83765868e-06, 1.36498636e-06, 2.67566877e-04],
              [1.45892349e-03, -4.37648316e-03, 1.0]])


img1path = '/content/drive/My Drive/m22ee002_q3/000000.png'
img2path = '/content/drive/My Drive/m22ee002_q3/000023.png'
img1 = cv2.imread(img1path, cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(img2path, cv2.IMREAD_GRAYSCALE)


def comp_epipol_lines(F, pts, which_image):
    if which_image == 1:
        return np.dot(F, np.concatenate([pts, np.ones((pts.shape[0], 1))], axis=1).T).T
    elif which_image == 2:
        return np.dot(F.T, np.concatenate([pts, np.ones((pts.shape[0], 1))], axis=1).T).T


pts1 = np.array([(0, 0)])
lines1 = comp_epipol_lines(F, pts1, which_image=1)


pts2 = np.array([(0, 0)])
lines2 = comp_epipol_lines(F, pts2, which_image=2)


def sampl_points_on_line(line, img_shape):
    sampled_points = []
    x0, y0 = map(int, [0, -line[2] / line[1]])
    x1, y1 = map(int, [img_shape[1], -(line[2] + line[0] * img_shape[1]) / line[1]])
    length = np.sqrt((x1 - x0)**2 + (y1 - y0)**2)
    for x in range(0, img_shape[1], 10):
        y = int((y1 - y0) / (x1 - x0) * x + y0)
        if 0 <= x < img_shape[1] and 0 <= y < img_shape[0]:

            if np.abs(line[0] * x + line[1] * y + line[2]) < 1:
                sampled_points.append((x, y))
    return sampled_points


correspondingpoints1_to_2 = [sampl_points_on_line(line, img1.shape) for line in lines1]


correspondingpoints2_to_1 = [sampl_points_on_line(line, img2.shape) for line in lines2]

for points2, line1 in zip(correspondingpoints2_to_1, lines1):
    for pt2 in points2:
        pt1 = (0, int(-line1[2] / line1[1]))
        cv2.line(img1, pt1, pt2, (0, 0, 255), thickness=2, lineType=cv2.LINE_AA)
        cv2.line(img2, pt2, pt1, (0, 0, 255), thickness=2, lineType=cv2.LINE_AA)


img1 = cv2.cvtColor(img1, cv2.COLOR_GRAY2BGR)
img2 = cv2.cvtColor(img2, cv2.COLOR_GRAY2BGR)

combined_img = np.hstack((img1, img2))

plt.figure(figsize=(12, 6))
plt.imshow(combined_img)
plt.title('Corresponding Points Connected with Lines')
plt.axis('off')
plt.show()
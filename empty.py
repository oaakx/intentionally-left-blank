import cv2

im = cv2.imread('empty-page.png', 0)
w, h = im.shape
npixels = im.size

nwhite = 0
for i in range(w):
  for j in range(h):
    if im[i, j] == 255:
      nwhite += 1

print(float(nwhite)/npixels * 100)
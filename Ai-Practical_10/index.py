import cv2

d = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

i = cv2.imread('image1.png')
g =cv2.cvtColor(i, cv2.COLOR_RGB2GRAY)

f = d.detectMultiScale(g,scaleFactor=1.1, minNeighbors=5)

for (x,y,w,h) in f:
    cv2.rectangle(i, (x,y), (x+w, y+h), (0,0,255), 2)

cv2.imshow('image', i)
cv2.waitKey(0)



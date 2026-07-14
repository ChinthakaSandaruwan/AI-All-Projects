import cv2

m = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')



i1 = cv2.imread("1.png")

i2 = cv2.cvtColor(i1, cv2.COLOR_BGR2GRAY)

f = m.detectMultiScale(i2,scaleFactor=1.05,minNeighbors=5)

for (x,y,w,h) in f:
    cv2.rectangle(i1 , (x,y) , (x+w,y+h) , (0,0,255), 2)

cv2.imshow('Viewer', i1)

cv2.waitKey(500000)
import cv2 
from insightface.app import FaceAnalysis 
import numpy

fa = FaceAnalysis(name="buffalo_l")

# using CPU (no CUDA GPU available)
fa.prepare(ctx_id=-1, det_size=(640,640))

img1 = cv2.imread("img3.png")
img2 = cv2.imread("img4.png")


faces1 = fa.get(img1)
faces2 = fa.get(img2)

face1 = faces1[0]
face2 = faces2[0]

code1 =face1.embedding
code2 =face2.embedding

distance = numpy.linalg.norm(code1 - code2)
print("Distance:",distance)

# print(code1)
# print(code2)

x1,y1,x2,y2 = map(int,face1.bbox)
cv2.rectangle(img1,(x1,y1),(x2,y2),(0,0,255),2)


cv2.imshow("img1",img1)
cv2.waitKey(0)


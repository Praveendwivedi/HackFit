from get_skeleton import get_skeleton
import cv2
from PIL import  Image
from numpy import asarray
from matplotlib import pyplot as plt
import numpy as np
# cap = cv2.VideoCapture(0)
# success, image = cap.read()
image = Image.open('yoga_poses\pose_1_0.jpg')
image1 = asarray(image)
res1=get_skeleton(image1)
coord1=[]
xcoord1=[]
ycoord1=[]
l1=list(res1.pose_landmarks.landmark)
for i in l1:
    x=i.x
    y=i.y
    coord1.append([x,y])
    xcoord1.append(x)
    ycoord1.append(y)
print(coord1)
# plt.scatter(xcoord1,ycoord1,label="image1",color="r")

image = Image.open('yoga_poses\pose_1_2.jpg')
image2 = asarray(image)
res2=get_skeleton(image2)
coord2=[]
xcoord2=[]
ycoord2=[]
print('----------------------')
l2=list(res2.pose_landmarks.landmark)
for i in l2:
    x=i.x
    y=i.y
    coord2.append([x,y])
    xcoord2.append(x)
    ycoord2.append(y)
    # coord2.append[[i.x,i.y]]
print(coord2)


########################################################
primary = np.array(coord1)

secondary = np.array(coord2)

# Pad the data with ones, so that our transformation can do translations too
n = primary.shape[0]
pad = lambda x: np.hstack([x, np.ones((x.shape[0], 1))])
unpad = lambda x: x[:,:-1]
X = pad(primary)
Y = pad(secondary)

# Solve the least squares problem X * A = Y
# to find our transformation matrix A
A, res, rank, s = np.linalg.lstsq(X, Y)

transform = lambda x: unpad(np.dot(pad(x), A))

print("Target:")
print(secondary)
print("Result:")
print(transform(primary))
print("Max error:", np.abs(secondary - transform(primary)).max())
xcoord2=[]
ycoord2=[]
for i in secondary:
    xcoord2.append(i[0])
    ycoord2.append(i[1])
plt.scatter(xcoord2,ycoord2,label="image1",color="r")
xcoord1=[]
ycoord1=[]
for i in transform(primary):
    xcoord1.append(i[0])
    ycoord1.append(i[1])
plt.scatter(xcoord1,ycoord1,label="image2",color="b")
plt.show()
# print(res1.pose_landmarks.landmark,res2.pose_landmarks.landmark)
'''
while True:
    while True:
        if success:
            res=get_skeleton(data)
            if cv2.waitKey(5) & 0xFF == 27:
                break
        break
'''
    # print(res.pose_landmarks)
# cap.release()

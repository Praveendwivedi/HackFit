from get_skeleton import get_skeleton
import cv2
from PIL import  Image
from numpy import asarray
# cap = cv2.VideoCapture(0)
# success, image = cap.read()
image = Image.open('yoga_poses\pose_1_0.jpg')
image1 = asarray(image)
res1=get_skeleton(image1)
print(res1)
image = Image.open('yoga_poses\pose_1_2.jpg')
image2 = asarray(image)
res2=get_skeleton(image2)
print(res2)
'''
while True:
    while True:
        if success:
            res=get_skeleton(data)
            if cv2.waitKey(5) & 0xFF == 27:
                break
        break
    # print(res.pose_landmarks)
# cap.release()
'''
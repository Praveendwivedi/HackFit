import cv2
import os

from IP_codes.get_skeleton import get_skeleton
import cv2
from PIL import  Image
from numpy import asarray
from matplotlib import pyplot as plt
import numpy as np
from playsound import playsound



# Folder which contains all the images
# from which video is to be generated
# os.chdir("yoga_poses")
folder = "yoga_poses\\Surya_Namaskar"


def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        print(filename)
        if img is not None:
            images.append(img)
    return images


images = load_images_from_folder(folder)
total_cnt = len(images)
cnt = 0

cap = cv2.VideoCapture(0)
def landmark_list(res):
    if res.pose_landmarks is None:
        return []
    return list(res.pose_landmarks.landmark)
def get_coord(l):
    coord=[]
    for i in l:
        x=i.x
        y=i.y
        coord.append([x,y])
    return coord
def check_matching(im1,im2,threshold):
    res1=get_skeleton(im1,True)
    l1=landmark_list(res1)
    if not l1 :
        return False
    coord1=get_coord(l1)
    primary = np.array(coord1)
    
    res2=get_skeleton(im2)
    l2=landmark_list(res2)
    coord2=get_coord(l2)
    secondary = np.array(coord2)

    n = primary.shape[0]
    pad = lambda x: np.hstack([x, np.ones((x.shape[0], 1))])
    unpad = lambda x: x[:,:-1]
    X = pad(primary)
    Y = pad(secondary)

    # Solve the least squares problem X * A = Y
    # to find our transformation matrix A
    A, res, rank, s = np.linalg.lstsq(X, Y)

    transform = lambda x: unpad(np.dot(pad(x), A))
    m=np.abs(secondary - transform(primary)).max()
    if m<=threshold:
        return True
    return False
cv2.imshow('tutorial', images[cnt])
while cap.isOpened():
    # Capture the video frame
    ret, frame = cap.read()
    # Display the resulting frame
    # cv2.imshow('frame', frame)
    # cv2.imshow('tutorial', images[cnt])
    testImage = asarray(images[cnt])
    threshold=0.09
    if check_matching(frame,testImage,threshold):
        print("matched.........")
        playsound('IP_codes\\beep.wav')
        cnt += 1

        if cnt == total_cnt:
            print("completed ")
            break
        get_skeleton(asarray(images[cnt]))
        cv2.imshow('tutorial', images[cnt])


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()


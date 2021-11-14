import cv2
import os

print(os.getcwd())

# Folder which contains all the images
# from which video is to be generated
os.chdir("D:\\Hackathons\\HackFit\\Media\\yoga_poses")
folder = "D:\\Hackathons\\HackFit\\Media\\yoga_poses"


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

vid = cv2.VideoCapture(0)

while (True):
    # Capture the video frame
    ret, frame = vid.read()
    # Display the resulting frame
    cv2.imshow('frame', frame)
    cv2.imshow('tutorial', images[cnt])
    if check_matching(frame, images[cnt]):
        print("matched.........")
        cnt += 1
        if cnt == total_cnt:
            print("completed ")
            break


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()


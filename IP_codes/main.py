import cv2

print(os.getcwd())

# Folder which contains all the images
# from which video is to be generated
os.chdir("D:\\Hackathons\\HackFit\\Media\\yoga_poses")
path = "D:\\Hackathons\\HackFit\\Media\\yoga_poses"

images = [img for img in os.listdir(image_folder)
              if img.endswith(".jpg") or
                 img.endswith(".jpeg") or
                 img.endswith("png")]

for im in images:
    cv.imshow(im)



# define a video capture object
vid = cv2.VideoCapture(0)

while (True):

    # Capture the video frame
    ret, frame = vid.read()

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()

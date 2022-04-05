##################
### Image Capture
##################

# Uncomment following code to see image capturing:

# import cv2, time
#
# video = cv2.VideoCapture(0)
#
# check, frame = video.read()
#
# print(check)
# print(frame)
#
# gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
# time.sleep(3)
# cv2.imshow('Capturing',gray)
#
# cv2.waitKey(0)
# video.release()
# cv2.destroyAllWindows


##################
### VDO Capture
##################

import cv2, time

video = cv2.VideoCapture(0)

count=1

while True:
    count = count+1
    check, frame = video.read()

    print(check)
    print(frame)

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #time.sleep(3)
    cv2.imshow('Capturing',gray)

    key = cv2.waitKey(1)

    if key==ord('q'):
        break

print('*'*50)
print(count)
video.release()
cv2.destroyAllWindows

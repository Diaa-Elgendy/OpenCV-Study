import cv2

video = cv2.VideoCapture("image/road.webm")

fps = int(video.get(cv2.CAP_PROP_FPS))
frame_num = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
w = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(fps, "FPS")
print(frame_num, "Frame Number")
print('Width: ', w)
print('Height: ', h)
print('Duration {} seconds'.format(frame_num // fps))

print('===============================')

while video.isOpened():
    graped, frame = video.read()  # graped => always true until we reached last frame
    key = cv2.waitKey(1)
    if (key & 0xFF) == ord('q') or not graped:  # when button q is clicked or we reach last frame quit
        break

    if (key & 0xFF) == ord('0'):
        print('Rested')
        video.set(cv2.CAP_PROP_POS_FRAMES, 0)  # when button 0 is clicked return to first frame

    cv2.imshow('Video', frame)
    cv2.waitKey(fps)  # to show image synced with fps

print('===============================')
 
import webbrowser
import cv2

# video = cv2.VideoCapture("image/road.webm")

# fps = int(video.get(cv2.CAP_PROP_FPS))
# frame_num = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
# w = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
# h = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
#
# print(fps, "FPS")
# print(frame_num, "Frame Number")
# print('Width: ', w)
# print('Height: ', h)
# print('Duration {} seconds'.format(frame_num // fps))
#
# print('===============================')
# while video.isOpened():
#     graped, frame = video.read()  # graped => always true until we reached last frame
#     frame = cv2.resize(frame, (800, 500))
#     key = cv2.waitKey(1)
#     if (key & 0xFF) == ord('q') or not graped:  # when button q is clicked or we reach last frame quit
#         print('Quit')
#         break
#
#     if (key & 0xFF) == ord('0'):
#         print('Rested')
#         video.set(cv2.CAP_PROP_POS_FRAMES, 0)  # when button 0 is clicked return to first frame
#
#     cv2.imshow('Video', frame)
#     cv2.waitKey(fps)  # to show image synced with fps


print('========== Save Video ==========')
video = cv2.VideoCapture("image/pepole.gif")

codec = cv2.VideoWriter_fourcc(*'mp4v')  # Video compression types
fps = int(video.get(cv2.CAP_PROP_FPS))
frame_num = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
w = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
colored_video = True
writer = cv2.VideoWriter('ped.mp4', codec, fps, (w, h))
writer.release()
video.release()
# webbrowser.open('ped.mp4')


# print('========== Reverse Video ==========')
#
# original_video = cv2.VideoCapture("image/pepole.gif")
# codec = cv2.VideoWriter_fourcc(*'mp4v')  # Video compression types
# fps = int(original_video.get(cv2.CAP_PROP_FPS))
# frame_num = int(original_video.get(cv2.CAP_PROP_FRAME_COUNT))
# w = int(original_video.get(cv2.CAP_PROP_FRAME_WIDTH))
# h = int(original_video.get(cv2.CAP_PROP_FRAME_HEIGHT))
# colored_video = True
#
# writer_backward = cv2.VideoWriter('ped_reversed.gif', codec, fps, (w, h), colored_video)
# frame_index = original_video.get(cv2.CAP_PROP_FRAME_COUNT)
#
# while frame_index > -1:
#     original_video.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
#     graped, frame = original_video.read()
#
#     key = cv2.waitKey(1)
#     if (key & 0xFF) == ord('q') or not graped:
#         break
#
#     writer_backward.write(frame)
#     frame_index -= 1
#
# writer_backward.release()
# original_video.release()
# webbrowser.open('ped_reversed.gif')

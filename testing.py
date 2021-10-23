import numpy as np
import cv2

cap = cv2.VideoCapture(0)


while True:
	ret, frame = cap.read()
	#width = int(cap.get(3))
	#height = int(cap.get(4))


corners = cv2.goodFeaturesToTrack(gray, 10, 0.01, 10)
corners = np.int0(corners)



for corner in corners:
	x, y = corner.ravel()
	cv2.circle(frame, (x, y), 5, (255, 0, 0), -1)

	#displays the video stream
	cv2.imshow('frame', frame)

	if cv2.waitKey(1) == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
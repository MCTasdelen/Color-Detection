import cv2

from PIL import Image

from color_limit import limit_func


yellow = [0, 255, 255]  # yellow in BGR colorspace
green = [0,255,0]
red = [0,0,255]
blue = [255,0,0]
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    # mirroring solution
    frame = cv2.flip(frame, 1)
    #bgr to hsv
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = limit_func(color=green)
    #masking
    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox
        #rectangle drawing
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)
        central_point_x=(x1+x2)/2
        central_point_y = (y1 + y2) / 2
        # circle drawing by central point
        frame = cv2.circle(frame,(int(central_point_x), int(central_point_y)),3,(0,0,255),1)

    cv2.imshow('frame', frame)

    esc = cv2.waitKey(1)
    if esc == 27:
        break
cap.release()

cv2.destroyAllWindows()

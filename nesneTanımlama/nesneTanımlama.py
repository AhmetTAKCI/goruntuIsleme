import cv2
import numpy as np


def main():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break


        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


        lower_red = np.array([0, 100, 100])
        upper_red = np.array([10, 255, 255])


        mask = cv2.inRange(hsv, lower_red, upper_red)


        res = cv2.bitwise_and(frame, frame, mask=mask)


        cv2.imshow("Frame", frame)
        cv2.imshow("Mask", mask)
        cv2.imshow("Result", res)


        k = cv2.waitKey(1) & 0xFF
        if k == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

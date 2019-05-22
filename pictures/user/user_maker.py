import cv2

cap = cv2.VideoCapture(0)
ret = True

while ret:
    ret, frame = cap.read()

    cv2.imshow("user maker", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        img = "user.png"
        cv2.imwrite(img, frame)

        cap.release()
        cv2.destroyAllWindows()
        break

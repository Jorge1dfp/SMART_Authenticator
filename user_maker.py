import cv2


def user_maker(x):
    cap = cv2.VideoCapture(0)
    ret = True

    while ret:
        ret, frame = cap.read()

        cv2.imshow("user maker", frame)

        if cv2.waitKey(1) & 0xFF == ord('c'):
            img = "C:\\Users\\T3kn1kal\\eclipse-workspace\\Unit-7\\src\\SMART_Authenticator\\pictures" + x
            cv2.imwrite(img, frame)
            cap.release()
            cv2.destroyAllWindows()
            break



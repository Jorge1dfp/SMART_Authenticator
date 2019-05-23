import cv2

cap = cv2.VideoCapture(0)
ret = True

while ret:
    ret, frame = cap.read()

    cv2.imshow("user maker", frame)

    names = {"user1.png", "user2.png", "user3.png"}
    for x in names:
        if cv2.waitKey(1) & 0xFF == ord('c'):
            img = "C://Users//Jorge Flores//PycharmProjects//SMART_Authenticator//pictures//user//" + x
            cv2.imwrite(img, frame)
            cap.release()
            cv2.destroyAllWindows()
            ret = False
            break
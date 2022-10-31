import cv2

import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
def distance():
    cap = cv2.VideoCapture(2)
    detector = FaceMeshDetector(maxFaces = 1)

    while True:
        success, img = cap.read()
        img, faces = detector.findFaceMesh(img, draw=False)

        if faces:
            face = faces[0]
            pointLeft = face[145]
            pointRight = face[374]
            #cv2.circle(img, pointLeft, 5, (83, 227, 39), cv2.FILLED)
            #cv2.circle(img, pointRight, 5, (83, 227, 39), cv2.FILLED)
            #cv2.line(img, pointLeft, pointRight, (83, 227, 39), 3)
            w, _ = detector.findDistance(pointLeft, pointRight)
            rw = 6.7
            #d = 50
            #fl = (w*d)/rw
            fl = 455
            d = (rw * fl)/w
            if d >= 48: 
                print("Distance is okay: {}".format(d))
            else:
                print("Distance is close: {}".format(d))
            return(d)
            #cvzone.putTextRect(img, f'Distance: {int(d)}cm', (face[10][0] - 125, face[10][1] - 30), scale=2)
            
        #cv2.imshow("Capture", img)
        #cv2.waitKey(1)

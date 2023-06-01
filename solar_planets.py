import cv2 

img = cv2.imread("solar-system.jpg")
cv2.imshow("output",img)

cv2.putText(img,
            "Sun",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX
            0.5,
            (255,255,255)
            )
        
cv2.putText(img,
            "Mecury",
            (30,350),
            cv2.FONT_HERSHEY_COMPLEX
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Venus",
            (40,400),
            cv2.FONT_HERSHEY_COMPLEX
            0.5,
            (239,125,235)
            )

cv2.putText(img,
            "Earth",
            (50,450),
            cv2.FONT_HERSHEY_COMPLEX
            0.5,
            (255,255,255)
            )
            
cv2.putText(img,
            "Mars",
            (40,500),
            cv2.FONT_HERSHEY_COMPLEX
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Jupiter",
            (50,550),
            cv2.FONT_HERSHEY_COMPLEX
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Saturn",
            (60,600),
            cv2.FONT_HERSHEY_COMPLEX
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Uranus",
            (70,650),
            cv2.FONT_HERSHEY_COMPLEX
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Neptune",
            (80,700),
            cv2.FONT_HERSHEY_COMPLEX
            0.5,
            (255,255,255)
            )

cv2.imshow("Output",img)
cv2.waitKey(0)

cv2.imwrite("Solar_systemwithname.jpg",img)
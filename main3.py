import cv2 

tiger = cv2.imread("tiger.jpg")

#varaibles for text 
color = (0,0,0)
origin = (100,100)
font = cv2.FONT_HERSHEY_COMPLEX
fontscale = 4
thickness = 10
image = cv2.putText(tiger, "This is a tiger", origin, font, fontscale, color, thickness, cv2.LINE_AA)

cv2.imshow("Tiger image", image)

cv2.waitKey()
cv2.destroyAllWindows()
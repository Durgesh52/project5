import cv2
img=cv2.imread('solar-system.jpg')

cv2.putText(img,"Sun",(100,80),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(255,255,255))
cv2.putText(img,"mercury",(110,180),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(255,255,255))
cv2.putText(img,"venus",(190,270),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(255,255,255))
cv2.putText(img,"earth",(300,270),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(255,255,255))
cv2.putText(img,"mars",(400,250),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(255,255,255))
cv2.putText(img,"Jupieter",(500,200),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(255,255,255))
cv2.putText(img,"saturn",(720,110),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(255,255,255))
cv2.putText(img,"uranus",(950,130),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(255,255,255))
cv2.putText(img,"neptune",(1000,50),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(255,255,255))
cv2.imwrite('Solar_systemwithname.jpg',img)
cv2.imshow("ss",img)
cv2.waitKey(0)


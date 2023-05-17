import cv2


img = cv2.imread("solar-system.jpg")




cv2.putText(img, "Sol", (100, 80), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255))
cv2.putText(img, "Mercurio", (125, 245), cv2.FONT_HERSHEY_COMPLEX, 0.3, (144, 128, 112))
cv2.putText(img, "Venus", (200, 260), cv2.FONT_HERSHEY_COMPLEX, 0.3, (0, 165, 255))
cv2.putText(img, "Terra", (295, 265), cv2.FONT_HERSHEY_COMPLEX, 0.3, (0, 128, 0))
cv2.putText(img, "Marte", (385, 250), cv2.FONT_HERSHEY_COMPLEX, 0.3, (0, 0, 139))
cv2.putText(img, "Jupiter", (570, 370), cv2.FONT_HERSHEY_COMPLEX, 0.3, (107, 147, 193))
cv2.putText(img, "Saturno", (770, 290), cv2.FONT_HERSHEY_COMPLEX, 0.3, (189, 212, 225))
cv2.putText(img, "Urano", (980, 290), cv2.FONT_HERSHEY_COMPLEX, 0.3, (230, 216, 173))
cv2.putText(img, "Netuno", (1125, 285), cv2.FONT_HERSHEY_COMPLEX, 0.3, (143, 10, 18))



#exibir a imagem com o texto
cv2.imshow("resultado", img)
cv2.waitKey(0)
cv2.imwrite("solar_system.jpg",img)
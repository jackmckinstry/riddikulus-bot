import cv2
from PIL import Image

s_img = cv2.resize(cv2.imread("wizardRobot.jpg"),(350,350))
l_img = cv2.imread("harryPotter.png")
x_offset = 100
y_offset = 100
l_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1]] = s_img

#test
cv2.namedWindow('Display image')          ## create window for display
cv2.imshow('Display image', l_img)        ##show img in display
cv2.waitKey(5000)  

Image.fromarray(l_img).save("img_result.png")
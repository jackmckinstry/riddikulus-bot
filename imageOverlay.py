import cv2

s_img = cv2.imread("wizardRobot.jpg")
l_img = cv2.imread("harryPotter.png")
x_offset=y_offset=50
l_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1]] = s_img

cv2.namedWindow('Display image')          ## create window for display
cv2.imshow('Display image', l_img)
cv2.waitKey(1000)  
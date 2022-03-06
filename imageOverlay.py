import cv2
from PIL import Image, ImageSequence

def fileName(status):
    match status:
        case "accio":
            return "accioGif.gif"
        case "alohomora":
            return "alohomoraGif.gif"
        case "avada kedavra":
            return "avadaKedavraGif.gif"
        case "expecto patronum":
            return "expectoPatronumGif.gif"
        case "expelliarmus":
            return "expelliarmusGif.gif"
        case "lumos":
            return "lumosGif.gif"
        case "":
            return "muggleGif.gif"
        case "obliviate":
            return "obliviateGif.gif"
        case "riddikulus":
            return "riddikulusGif.gif"
        case "sectumempra":
            return "sectumSempraGif.gif"
        case "wingardium leviosa":
            return "wingardiumLeviosaGif.gif"

sImg = cv2.resize(cv2.imread("wizardRobot.jpg"),(350,350))
lImg = cv2.imread(fileName)
xOffset = 100
yOffset = 100

lImg[yOffset:yOffset+sImg.shape[0], xOffset:xOffset+sImg.shape[1]] = sImg
#test
cv2.namedWindow('Display image')          ## create window for display
cv2.imshow('Display image', lImg)        ##show img in display
cv2.waitKey(5000)  

Image.fromarray(lImg).save("img_result.png")
from PIL import Image, ImageSequence

def fileName(status):
    match status:
        case "accio":
            return "gif/accioGif.gif"
        case "alohomora":
            return "gif/alohomoraGif.gif"
        case "avada kedavra":
            return "gif/avadaKedavraGif.gif"
        case "expecto patronum":
            return "gif/expectoPatronumGif.gif"
        case "expelliarmus":
            return "gif/expelliarmusGif.gif"
        case "lumos":
            return "gif/lumosGif.gif"
        case "muggle":
            return "gif/muggleGif.gif"
        case "obliviate":
            return "gif/obliviateGif.gif"
        case "riddikulus":
            return "gif/riddikulusGif.gif"
        case "sectum sempra":
            return "gif/sectumSempraGif.gif"
        case "wingardium leviosa":
            return "gif/wingardiumLeviosaGif.gif"

def xOffSet(status):
    match status:
        case "accio":
            return 130
        case "alohomora":
            return 0
        case "avada kedavra":
            return 180
        case "expecto patronum":
            return 250
        case "expelliarmus":
            return 260
        case "lumos":
            return 20
        case "muggle":
            return 0
        case "obliviate":
            return 120
        case "riddikulus":
            return 220
        case "sectum sempra":
            return 400
        case "wingardium leviosa":
            return 35

def yOffSet(status):
    match status:
        case "accio":
            return 40
        case "alohomora":
            return 50
        case "avada kedavra":
            return 40
        case "expecto patronum":
            return 120
        case "expelliarmus":
            return 25
        case "lumos":
            return 110
        case "muggle":
            return 0
        case "obliviate":
            return 0
        case "riddikulus":
            return 90
        case "sectum sempra":
            return 45
        case "wingardium leviosa":
            return 45

def reSize(status):
    match status:
        case "accio":
            return 100
        case "alohomora":
            return 100
        case "avada kedavra":
            return 60
        case "expecto patronum":
            return 100
        case "expelliarmus":
            return 75
        case "lumos":
            return 35
        case "muggle":
            return 1
        case "obliviate":
            return 80
        case "riddikulus":
            return 120
        case "sectum sempra":
            return 60
        case "wingardium leviosa":
            return 95

def produceGif(status):
    toOpen = fileName(status)
    xPos = xOffSet(status)
    yPos = yOffSet(status)
    resizeVal = reSize(status)

    background = Image.open("pfp.png").resize((resizeVal,resizeVal))

    animated_gif = Image.open(toOpen)

    frames = []
    for frame in ImageSequence.Iterator(animated_gif):
        frame = frame.copy()
        frame.paste(background, (xPos,yPos))
        frames.append(frame)

    frames[0].save('output.gif', save_all=True, append_images=frames[1:]) 
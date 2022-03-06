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

background = Image.open("wizardRobot.jpg").resize((100,100))

animated_gif = Image.open("gif/accioGif.gif")

frames = []
for frame in ImageSequence.Iterator(animated_gif):
    frame = frame.copy()
    frame.paste(background, (130,40))
    frames.append(frame)

frames[0].save('output.gif', save_all=True, append_images=frames[1:]) 
from PIL import Image, ImageSequence

background = Image.open("img.jpg")
animated_gif = Image.open("GIFF.gif")

frames = []
for frame in ImageSequence.Iterator(animated_gif):
    output = background.copy()
    frame_px = frame.load()
    output_px = output.load()
    transparent_foreground = frame.convert('RGBA')
    transparent_foreground_px = transparent_foreground.load()
    for x in range(frame.width):
        for y in range(frame.height):
            if frame_px[x, y] in (frame.info["background"], frame.info["transparency"]):
                continue
            output_px[x, y] = transparent_foreground_px[x, y]
    frames.append(output)

frames[0].save('output.gif', save_all=True, append_images=frames[1:-1]) 


from PIL import Image, ImageFilter

image = Image.open("image.jpg")
image_filtered = image.filter(ImageFilter.BLUR)
image_filtered.show()
image_filtered.save("blurred.png", "png")
image.thumbnail((400, 400))
image.crop((100, 100, 300, 300))
image.resize((400, 400))
image.rotate(90)
image.convert("L")


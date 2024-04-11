# pip install pillow
from PIL import Image, ImageFilter, ImageOps #, ImageEnhance, ImageDraw, ImageFont, ImageChops, ImageColor, ImageStat
import io

# image = Image.open(io.BytesIO(b"some data"))
image = Image.open("vesika.jpg")
# image.convert('L') # grayscale
# image = image.filter(ImageFilter.BLUR)
# Image.save("blurred.png", "png")
# Image.thumbnail((400, 400))
# Image.crop((100, 100, 300, 300))
# Image.transpose(Image.FLIP_LEFT_RIGHT)
# image.resize((28, 28), Image.ANTIALIAS)
# Image.rotate(90)
# Image.convert("L")

image = ImageOps.grayscale(image)
image.show()

# ImageOps.flip(image)
# ImageOps.mirror(image)
# ImageOps.invert(image)
# ImageOps.grayscale(image)
# ImageOps.expand(image)
# ImageOps.pad(image)
# ImageOps.fit(image)
# ImageOps.contain(image)
# ImageOps.crop(image)
# ImageOps.solarize()
# ImageOps.colorize()
# ImageOps.autocontrast()
# ImageOps.deform()
# ImageOps.exif_transpose()

# ImageFilter.GaussianBlur
# ImageFilter.MedianFilter
# ImageFilter.UnsharpMask
# ImageFilter.BLUR
# ImageFilter.CONTOUR
# ImageFilter.BoxBlur
# ImageFilter.DETAIL
# ImageFilter.EDGE_ENHANCE
# ImageFilter.EDGE_ENHANCE_MORE
# ImageFilter.EMBOSS
# ImageFilter.FIND_EDGES
# ImageFilter.SMOOTH
# ImageFilter.SMOOTH_MORE
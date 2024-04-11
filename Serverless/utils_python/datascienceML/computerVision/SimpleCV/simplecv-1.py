
# https://www.youtube.com/watch?v=UZSm7Q2bZoc
# pip install --upgrade SimpleCV==1.3

#from SimpleCV import Camera, Display, Image, ImageClass, Color
import SimpleCV

# cam = Camera()
# while True:
#     img = cam.getImage()
#     img.binarize() # black/white
#     img.drawText("you look grea ")
#     img.show()
#     if img.isKeyDown('q'):
#        break

# img = Image("test.jpg")
# blobs = img.findBlobs()
# blobs = img.findBlobs(threshval=128, minsize=200)
# blobs.draw(width=2, autocolor=True) # color=Color.RED
# if blobs is not None:
#     blobs.draw()
# img.show()

# img.binarize() # b/w
# img = img.invert()
# img = img.scale(0.3)
# img.adaptiveScale()
# text = img.readText() 
# text = text[13:-32]
# img.edges().dilate()
# img.blur()
# img.applyGaussianFilter()
# img.crop()
# img.flipVertical()
# img.grayscale()
# img.resize()
# img.rotate()
# img.toGray()

# img.findBarcode()
# img.findBlobs()
# img.findBlobsFromMask()
# img.findBlobsFromPalette()
# img.findChessboard()
# img.findCircle()
# img.findChessboard()
# img.findCorners()
# img.findFloodFillBlobs()
# img.findHaarFeatures() 'face' 'eye' 'mustache'
# img.findKeypointMatch()
# img.findKeypoints()
# img.findLines()
# img.findMotion()
# img.findSkintoneBlobs()
# img.smartFindBlobs()

# cam = Camera()
# disp = Display((640,480))
# while disp.isNotDone():
#     img = cam.getImage().binarize() # b/w
#     img.drawText("Hello World!", 40,40, fontsize=60, color=Color.RED)
#     img.save(disp) #show it
#     if disp.mouseLeft:
#         break


# from SimpleCV import JpegStreamCamera, JpegStreamer
# import webbrowser
# import time

# cam = JpegStreamCamera("http://192.168.1.1:8080")
# #cam.calibrate()
# output = JpegStreamer("http://localhost:8080", st=0.1)
# time.sleep(1)
# webbrowser.open("http://localhost:8080", new=0, autoraise=False)
# while True:
#     img = cam.getImage()
#     #img.show()
#     img.edges().dilate().invert().scale(2).save(output)
#     time.sleep(0.05)
    

# find the yellow star cookie in the corner
# import numpy as np
# img = Image("cookies.jpg")
# blobs = img.findBlobs(threshval=128, minsize=200)
# blobs.draw(color=Color.RED, width=-1, autocolor=True) # width -1 : fill
# img.show()
# areaAvg = np.mean(blobs.area())
# areaStd = np.std(blobs.area())
# # filter cookies by area, draw those green
# lilcookies = blobs.filter(blobs.area() < areaAvg + 2.5 * areaStd)
# lilcookies.draw(width=-1, color=Color.GREEN)
# img.show()
# # sort the cookies so the yellow ones are at 0
# lilcookies = lilcookies.sortColorDistance(Color.YELLOW)
# lilcookies[0:4].draw(width=-1, color=Color.YELLOW)
# img.show()

# img = Image("image.jpg")
# img.show()
# img.edges().show()
# lines = img.findLines()
# lines = lines.filter(lines.length() > 50)
# lines.show(width=3)


# Draw box around faces
# from SimpleCV import Camera, Display

# cam = Camera()
# disp = Display()

# while disp.isNotDone():
#     img = cam.getImage()
#     gray_img = img.grayscale()
#     faces = gray_img.findHaarFeatures('face.xml')
#     if faces:
#         for face in faces:
#             face_box = face.boundingBox()
#             img.drawRectangle(face_box[0], face_box[1], face_box[2], face_box[3], color=(255, 0, 0), width=3)
#     img.show()
#     if disp.mouseRight:
#         break

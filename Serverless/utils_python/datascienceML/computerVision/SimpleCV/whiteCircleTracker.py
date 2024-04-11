
# https://www.youtube.com/watch?v=jihxqg3kr-g
from SimpleCV import Camera, Color

# White Ball Traacker
cam = Camera()  
while True:
    img = cam.getImage().flipHorizontal()
    dist = img.colorDistance(Color.BLACK) #.dilate(2)
    segmented = dist.stretch(200,255)
    blobs = segmented.findBlobs()
    if blobs:
        # biggestBlob = blobs.sortArea()[-1]
        # img.drawCircle(biggestBlob.centroid(), 10, Color.RED, -1)
        circles = blobs.filter([b.isCircle(0.5) for b in blobs])
        if circles:
            img.drawCircle((circles[-1].x, circles[-1].y), circles[-1].radius(), Color.BLUE, 3)

    img.show()
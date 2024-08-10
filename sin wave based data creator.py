import numpy
from PIL import Image
import os, time

path = os.path.join("sample.png")
limitSize = 50


img = Image.open(path).convert("RGB")
y, x, _ = numpy.array(img).shape
scaleFactor = limitSize/x if x>y else limitSize/y
img = numpy.array(img.resize((max(1, (round(x*scaleFactor))),max(1, round(y*scaleFactor)))))
imgC = numpy.empty(img.shape[:2])
imgC = img[:,:,0]*65536 + img[:,:,1]*256 + img[:,:,0]
translated = []
for y in range(imgC.shape[1]):
    for x in range(imgC.shape[0]):
        translated.append(imgC[x,y])
print(translated)
print(f"size: [{imgC.shape[1]}, {imgC.shape[0]}]")
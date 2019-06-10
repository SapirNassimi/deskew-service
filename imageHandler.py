import deskew
import urllib.request
from PIL import Image
import uploadImage
import uploadImage

# function that 
# receives a url
# takes the image out of it
# sends it to deskew
# receives the deskewd image
# saves the new image to amazon
# returns the deskewd url


def handleImage(url):    
    getImageFromUrl(url)
    deskewdImage = deskew.deskew("skewd.jpg")
    outImage = Image.fromarray(deskewdImage)
    outImage.save("deskewd.jpg", "JPEG")

    return (uploadImage.saveImageToAmazon())


def getImageFromUrl(url):
    skewdImage = Image.open(urllib.request.urlopen(url))
    skewdImage.save("skewd.jpg", "JPEG")

    return skewdImage
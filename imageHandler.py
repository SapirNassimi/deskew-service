import deskew


# function that 
# receives a url
# takes the image out of it
# sends it to deskew
# receives the deskewd image
# saves the new image to amazon
# returns the deskewd url


def handleImage(url):    
    skewdImage = getImageFromUrl(url)
    deskewdImage = deskew.deskew(skewdImage)
    
    return (saveImageToAmazon(deskewdImage))

def getImageFromUrl(url):
    
    skewdImage = 0 # ???

    return skewdImage

def saveImageToAmazon(image):
    # save to amazon
    # get url

    url = 0 # ????

    return url
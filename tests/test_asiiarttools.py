import pytest
from PIL import Image
from asiiarttools import asciiarttools
gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
gscale2 = '@%#*+=-:. '
#This test function is not working
def testTextAsciiOutputQuality(fileName,moreLevels=True):
    gscale = gscale1 if moreLevels else gscale2
    newtext=asciiarttools.convertImageToAscii(fileName, cols=80, scale=0.43, moreLevels=True, debug=False)
    check=True
    for i in range(len(newtext)):
        if newtext[i] in gscale:
            continue
        else:
            check=False
    assert check==True, "The generated text image contains invalid character"
        
def testColorAsciiOutputQuality(inputImage):
    asciiarttools.convertImageToAsciiImage(inputImage, outFile='output.png')
    check=True
    try:
        im=Image.open('output.png')
        try:
            im.verify()
        except:
            check=False
    except:
        check=False
    assert check==True, "The generated image is broken"

def testColorAsciiOutputSize(inputImage):
    im1 = Image.open(inputImage)
    width1, height1=im1.size
    asciiarttools.convertImageToAsciiImage(inputImage, outFile='output.png')
    im2 = Image.open('output.png')
    width2, height2=im2.size
    assert (width2==10*width1) & (height2==18*height1), "The generated image is in the wrong size"

def testAdjustBrightnessShape(art,value,moreLevels=True):
    newtext=asciiarttools.adjustASCIIBrightness(art, value,moreLevels=True)
    assert len(art)==len(newtext), "The new ascii art has the wrong shape after adjusting the brightness"

def testIncreaseBrightness(art,value,moreLevels=True):
    gscale = gscale1 if moreLevels else gscale2
    newtext=asciiarttools.adjustASCIIBrightness(art, value,moreLevels=True)
    check=True
    for i in range(len(newtext)):
        if gscale.index(art[i])<=gscale.index(newtext[i]):
            continue
        else:
            check=False
            break
    assert check==True, "The character shift is in the wrong direction"

def testDecreaseBrightness(art,value,moreLevels=True):
    gscale = gscale1 if moreLevels else gscale2
    newtext=asciiarttools.adjustASCIIBrightness(art, value,moreLevels=True)
    check=True
    for i in range(len(newtext)):
        if gscale.index(art[i])>=gscale.index(newtext[i]):
            continue
        else:
            check=False
            break
    assert check==True, "The character shift is in the wrong direction"

def testAdjustContrastShape(art,value,moreLevels=True):
    newtext=asciiarttools.adjustASCIIContrast(art, value,moreLevels=True)
    assert len(art)==len(newtext), "The new ascii art has the wrong shape after adjusting contrast"

def testSharpenContrast(art,value,moreLevels=True):
    gscale = gscale1 if moreLevels else gscale2
    newtext=asciiarttools.adjustASCIIContrast(art, value,moreLevels=True)
    check=True
    for i in range(len(newtext)):
        if gscale.index(art[i])<=len(gscale)/2:
            if gscale.index(art[i])>=gscale.index(newtext[i]):
                continue
            else:
                check=False
                break
        else:
            if gscale.index(art[i])<=gscale.index(newtext[i]):
                continue
            else:
                check=False
                break
    assert check==True, "The character shift is in the wrong direction"

def testSoftenContrast(art,value,moreLevels=True):
    gscale = gscale1 if moreLevels else gscale2
    newtext=asciiarttools.adjustASCIIContrast(art, value,moreLevels=True)
    check=True
    for i in range(len(newtext)):
        if gscale.index(art[i])<=len(gscale)/2:
            if gscale.index(art[i])<=gscale.index(newtext[i]):
                continue
            else:
                check=False
                break
        else:
            if gscale.index(art[i])>=gscale.index(newtext[i]):
                continue
            else:
                check=False
                break
    assert check==True, "The character shift is in the wrong direction"

testIncreaseBrightness("out.txt",0.5,moreLevels=True)
testDecreaseBrightness("out.txt",-0.5,moreLevels=True)
testAdjustBrightnessShape("out.txt",0.5,moreLevels=True)
testSharpenContrast("out.txt",0.5,moreLevels=True)
testSoftenContrast("out.txt",-0.5,moreLevels=True)
testAdjustContrastShape("out.txt",0.5,moreLevels=True)
testColorAsciiOutputQuality("cat2.jpg")
testColorAsciiOutputSize("cat2.jpg")
testTextAsciiOutputQuality("cat2.jpg")
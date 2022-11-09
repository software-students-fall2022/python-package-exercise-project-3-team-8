import pytest
from PIL import Image
#from asciiarttools import asciiarttools
import sys
sys.path.insert(1, '../src/asciiarttools')
from src.asciiarttools import asciiarttools
gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
gscale2 = '@%#*+=-:. '
allowed_chars = '\n'
def test_TextAsciiOutputLength(inputImage="tests/cat2.jpg"):
    newfile=asciiarttools.convertImageToAscii(inputImage)
    f=open(newfile,'r')
    f=list(f)
    assert len(f)>0, "The output file empty"

def test_TextAsciiOutputQuality(fileName="tests/cat2.jpg",moreLevels=True):
    gscale = gscale1 if moreLevels else gscale2
    newfile=asciiarttools.convertImageToAscii(fileName, moreLevels)
    newtext=open(newfile,'r')
    newtext=list(newtext)
    for i in range(len(newtext)):
        assert newtext[i] not in gscale and newtext[i] not in allowed_chars, f"The generated text image contains invalid character '{newtext[i]}'"

def test_TextAsciiOutputType(inputImage="tests/cat2.jpg"):
    file=asciiarttools.convertImageToAscii(inputImage)
    assert file.endswith('.txt'), "The output file format is wrong"

def test_ColorAsciiOutputType(inputImage="tests/cat2.jpg"):
    image=asciiarttools.convertImageToAsciiImage(inputImage)
    assert image.endswith('.png'), "The output file format is wrong"
        
def test_ColorAsciiOutputQuality(inputImage="tests/cat2.jpg",outFile='output.png'):
    image=asciiarttools.convertImageToAsciiImage(inputImage, outFile='output.png')
    check=True
    try:
        im=Image.open(outFile)
        try:
            im.verify()
        except:
            check=False
    except:
        check=False
    assert check==True, "The generated image is broken"

def test_ColorAsciiOutputSize(inputImage="tests/cat2.jpg"):
    im1 = Image.open(inputImage)
    width1, height1=im1.size
    asciiarttools.convertImageToAsciiImage(inputImage, outFile='output.png')
    im2 = Image.open('output.png')
    width2, height2=im2.size
    assert (width2==10*width1) & (height2==18*height1), "The generated image is in the wrong size"
def test_AdjustBrightnessShape(art="out.txt",value=0.5,moreLevels=True):
    newtext=asciiarttools.adjustASCIIBrightness(art, value,moreLevels=True)
    assert len(art)==len(newtext), "The new ascii art has the wrong shape after adjusting the brightness"

def test_IncreaseBrightness(art="out.txt",value=0.5,moreLevels=True):
    gscale = gscale1 if moreLevels else gscale2
    newtext=asciiarttools.adjustASCIIBrightness(art, value,moreLevels=True)
    check=True
    for i in range(len(newtext)):
        assert gscale.index(art[i])<=gscale.index(newtext[i]), f"The character '{art[i]}' was shifted in the wrong direction"

def test_DecreaseBrightness(art="out.txt",value=-0.5,moreLevels=True):
    gscale = gscale1 if moreLevels else gscale2
    newtext=asciiarttools.adjustASCIIBrightness(art, value,moreLevels=True)
    check=True
    for i in range(len(newtext)):
        assert gscale.index(art[i])>=gscale.index(newtext[i]), f"The character '{art[i]}' was shifted in the wrong direction"

def test_AdjustContrastShape(art="out.txt",value=0.5,moreLevels=True):
    newtext=asciiarttools.adjustASCIIContrast(art, value,moreLevels=True)
    assert len(art)==len(newtext), "The new ascii art has the wrong shape after adjusting contrast"

def test_SharpenContrast(art="out.txt",value=0.5,moreLevels=True):
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

def test_SoftenContrast(art="out.txt",value=-0.5,moreLevels=True):
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


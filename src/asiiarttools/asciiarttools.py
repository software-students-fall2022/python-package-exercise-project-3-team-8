#import library
import numpy as np
 
from PIL import Image, ImageDraw

# 70 levels of gray
gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
 
# 10 levels of gray
gscale2 = '@%#*+=-:. '

def convertImageToAsciiImage(inputImage, outFile='output.png'):

    #"Standard" list of ASCII sorted by grayscale (dark to light)
    global gscale1
    character=gscale1

    #convert string to list
    character_list=list(character)

    #get number of characters (68)
    #print(len(character_list))

    #open image
    im = Image.open(inputImage)

    #get width and height of the image
    width, height=im.size

    #get pixel matrix
    pixel = im.load()

    #open output text file - already function for this below
    #output=open("output.txt","w")
    
    #create output image
    #use color to adjust how dark the output image to be (0->dark, 255->light)
    outputImage = Image.new('RGB', (10 * width, 18 * height), color = (40, 40, 40))

    #draw output image
    out = ImageDraw.Draw(outputImage)

    #loop through rows of pixel matrix
    for i in range(height):

        #loop through columns of pixel matrix
        for j in range(width):

            #get R G B value of each pixel
            r,g,b=pixel[j,i]

            #take the average of R G B value for each pixel
            average=(r+g+b)/3

            #get the index of chracter for each pixel
            #the range for R G B is 0-255
            #index range is 0-67
            index=int(average/3.8)

            #write the character to output file
            #output.write(character_list[index])

            #fill the character with color (same rgb as the original image)
            out.text((j*10, i*18), character_list[index], fill = (r, g, b))

        #write to the next line in output file
        #output.write("\n")

    #get .png output image   
    outputImage.save(outFile)   
 
def getAverageL(image):
    """
    Given PIL Image, return average value of grayscale value
    """
    # get image as numpy array
    im = np.array(image)
 
    # get shape
    w,h = im.shape
 
    # get average
    return np.average(im.reshape(w*h))
 
def convertImageToAscii(fileName, cols=80, scale=0.43, moreLevels=True, debug=False):
    """
    Given Image and dims (rows, cols) returns an m*n list of Images
    """
    # declare globals
    global gscale1, gscale2
 
    # open image and convert to grayscale
    image = Image.open(fileName).convert('L')
 
    # store dimensions
    W, H = image.size[0], image.size[1]
    if debug:
        print("input image dims: %d x %d" % (W, H))
 
    # compute width of tile
    w = W/cols
 
    # compute tile height based on aspect ratio and scale
    h = w/scale
 
    # compute number of rows
    rows = int(H/h)
     
    print("cols: %d, rows: %d" % (cols, rows))
    print("tile dims: %d x %d" % (w, h))
 
    # check if image size is too small
    if cols > W or rows > H:
        print("Image too small for specified cols!")
        exit(0)
 
    # ascii image is a list of character strings
    aimg = []
    # generate list of dimensions
    for j in range(rows):
        y1 = int(j*h)
        y2 = int((j+1)*h)
 
        # correct last tile
        if j == rows-1:
            y2 = H
 
        # append an empty string
        aimg.append("")
 
        for i in range(cols):
 
            # crop image to tile
            x1 = int(i*w)
            x2 = int((i+1)*w)
 
            # correct last tile
            if i == cols-1:
                x2 = W
 
            # crop image to extract tile
            img = image.crop((x1, y1, x2, y2))
 
            # get average luminance
            avg = int(getAverageL(img))
 
            # look up ascii char
            if moreLevels:
                gsval = gscale1[int((avg*69)/255)]
            else:
                gsval = gscale2[int((avg*9)/255)]
 
            # append ascii char to string
            aimg[j] += gsval
     
    # return txt image
    return aimg

def adjustASCIIBrightness(art, value, moreLevels=True):
    """
    Given ASCII Art text and brightness value [-1, 1] returns original ASCII Art text brightened/darkened
    """
    global gscale1, gscale2
    gscale = gscale1 if moreLevels else gscale2

    # adjust +/- brightness
    adjustedVal = round(value * len(gscale)/2)

    output = list(art)

    for i in range(len(art)):
        if art[i] in gscale:
            # clamp new value to gscale
            newVal = min(len(gscale) - 1, max(0, gscale.index(art[i]) + adjustedVal))
            output[i] = gscale[newVal]
    return ''.join(output)

def adjustASCIIContrast(art, value, moreLevels=True):
    """
    Given ASCII Art text and contrast value [-1, 1] returns original ASCII Art text with softer or sharper contrast
    """
    global gscale1, gscale2

    gscale = gscale1 if moreLevels else gscale2

    # change in index
    adjustedVal = round(abs(value) * len(gscale)/7)

    output = list(art)

    for i in range(len(art)):

        if art[i] in gscale:
            #softer
            if (value<0):
                #make index approach middle of gscale list
                if (gscale.index(art[i])<=len(gscale)/2):

                    newVal=min(round(len(gscale)/2)-1, gscale.index(art[i]) + adjustedVal)
               
                else:
                    newVal = max(round(len(gscale)/2), gscale.index(art[i]) - adjustedVal)

                output[i] = gscale[newVal]
            #sharper
            else:
                #make index approach the end of gscale list
                if (gscale.index(art[i])<=len(gscale)/2):

                    newVal=max(0, gscale.index(art[i]) - adjustedVal)

                else:

                    newVal = min(len(gscale)-1, gscale.index(art[i]) + adjustedVal)

                output[i] = gscale[newVal]

    return ''.join(output)
# Python code to convert an image to ASCII image.
import asciiarttools as art
 
# main() function
def main():
    imgFile = "cat2.jpg"
 
    # set output file
    outFile = 'out.txt'
 
    # set scale default as 0.43 which suits
    # a Courier font
    scale = 0.43
 
    # set cols
    cols = 80
 
    print('Generating ASCII art from image...')
    # convert image to ascii txt
    aimg = art.convertImageToAscii(imgFile, cols, scale, True)
 
    # open file
    f = open(outFile, 'w')
 
    # write to file
    for row in aimg:
        f.write(row + '\n')
 
    # cleanup
    f.close()
    print("ASCII art written to %s" % outFile)

    # test ASCII color image
    print('Generating ASCII art color image from image...')
    art.convertImageToAsciiImage('cat1.jpg', 'output.png')
    print('ASCII image written to output.png')

    # test adjusting brightness
    print('Adjusting brightness of ASCII image')

    f = open(outFile, 'r')
    baseImg = f.read()
    f.close()
    brighten = art.adjustASCIIBrightness(baseImg, .5)
    darken = art.adjustASCIIBrightness(baseImg, -.5)
    
    bOut = open('brightened.txt', 'w')
    dOut = open('darkened.txt', 'w')

    bOut.write(brighten)
    dOut.write(darken)

    print('ASCII image output written to brightened.txt and darkened.txt')
    
    f = open("pyasciiart/out.txt", 'r')
    baseImg = f.read()
    f.close()

    sharper=art.adjustASCIIContrast(baseImg,0.5)
    softer=art.adjustASCIIContrast(baseImg,-0.5)

    sharpOut = open('SharperContrast.txt', 'w')
    sharpOut.write(sharper)
    sharpOut.close()

    softOut = open('SofterContrast.txt', 'w')
    softOut.write(softer)
    softOut.close()

    print('ASCII image output written to SharperContrast.txt and SofterContrast.txt')

# call main
if __name__ == '__main__':
    main()
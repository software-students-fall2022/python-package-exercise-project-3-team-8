# Python code to convert an image to ASCII image.
import asciiarttools as art
import sys
 
# main() function
def main():
    if len(sys.argv) < 2:
        print(f"Usage: py {sys.argv[0]} filename\n")
        sys.exit()
    imgFile = sys.argv[1]

    # -------- convertImageToAscii --------
    # set output file
    outFile = 'out.txt'

    # set scale default as 0.43 which suits
    # a Courier font (default value)
    scale = 0.43

    # set cols (80 is a default value)
    cols = 80

    print('Generating ASCII art from image...')
    art.convertImageToAscii(imgFile, cols, scale, True)
    print("ASCII art written to %s" % outFile)

    # -------- convertImageToAsciiImage --------
    print('Generating ASCII art color image from image...')
    art.convertImageToAsciiImage(imgFile, 'output.png')
    print('ASCII image written to output.png')

    # -------- adjustASCIIBrightness --------
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
    
    # -------- adjustASCIIContrast --------
    f = open("out.txt", 'r')
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
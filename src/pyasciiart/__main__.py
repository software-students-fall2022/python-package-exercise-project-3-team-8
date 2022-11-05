# Python code to convert an image to ASCII image.
import argparse
import asciiArt as art
 
# main() function
def main():
    # create parser
    descStr = "This program converts an image into ASCII art."
    parser = argparse.ArgumentParser(description=descStr)
    # add expected arguments
    parser.add_argument('--file', dest='imgFile', required=True)
    parser.add_argument('--scale', dest='scale', required=False)
    parser.add_argument('--out', dest='outFile', required=False)
    parser.add_argument('--cols', dest='cols', required=False)
    parser.add_argument('--morelevels',dest='moreLevels',action='store_true')
 
    # parse args
    args = parser.parse_args()
   
    imgFile = args.imgFile
 
    # set output file
    outFile = 'out.txt'
    if args.outFile:
        outFile = args.outFile
 
    # set scale default as 0.43 which suits
    # a Courier font
    scale = 0.43
    if args.scale:
        scale = float(args.scale)
 
    # set cols
    cols = 80
    if args.cols:
        cols = int(args.cols)
 
    print('Generating ASCII art from image...')
    # convert image to ascii txt
    aimg = art.convertImageToAscii(imgFile, cols, scale, args.moreLevels)
 
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
# Python code to convert an image to ASCII image.
import sys, argparse
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
    aimg = art.covertImageToAscii(imgFile, cols, scale, args.moreLevels)
 
    # open file
    f = open(outFile, 'w')
 
    # write to file
    for row in aimg:
        f.write(row + '\n')
 
    # cleanup
    f.close()
    print("ASCII art written to %s" % outFile)

    print('Generating ASCII art color image from image...')
    art.covertImageToAsciiImage('cat1.jpg', 'output.png')
    print('ASCII image written to output.png')
 
# call main
if __name__ == '__main__':
    main()
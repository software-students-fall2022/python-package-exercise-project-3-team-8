#import library
from PIL import Image, ImageDraw

def Convert_to_ascii(image):

    #"Standard" list of ASCII sorted by grayscale (dark to light)
    character="$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,^`'."

    #convert string to list
    character_list=list(character)

    #get number of characters (68)
    #print(len(character_list))

    #open image
    im = Image.open(image)

    #get width and height of the image
    width, height=im.size

    #get pixel matrix
    pixel = im.load()

    #open output text file
    output=open("output.txt","w")
    
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
            output.write(character_list[index])

            #fill the character with color (same rgb as the original image)
            out.text((j*10, i*18), character_list[index], fill = (r, g, b))

        #write to the next line in output file
        output.write("\n")

    #get .png output image   
    outputImage.save('output.png')   

#call function
Convert_to_ascii("cat1.jpg")

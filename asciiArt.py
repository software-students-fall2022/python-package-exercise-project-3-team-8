from PIL import Image
def Convert_to_ascii(image):
    character="$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,^`'."
    character_list=list(character)
    #print(len(character_list))
    im = Image.open(image)
    width, height=im.size
    pixel = im.load()
    output=open("output.txt","w")
    for i in range(height):
        for j in range(width):
            r,g,b=pixel[j,i]
            average=(r+g+b)/3
            index=int(average/3.81)
            output.write(character_list[index])
        output.write("\n")   
Convert_to_ascii("cat2.jpg")


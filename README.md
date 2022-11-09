![Python build & test](https://github.com/software-students-fall2022/python-package-exercise-project-3-team-8/actions/workflows/python-package.yml/badge.svg)

# Convert Image to ASCII
ASCII art is a graphic design technique that uses computers for presentation and consists of pictures pieced together from the 95 printable (from a total of 128) characters defined by the ASCII Standard from 1963 and ASCII compliant character sets with proprietary extended characters (beyond the 128 characters of standard 7-bit ASCII). The term is also loosely used to refer to text-based visual art in general. ASCII art can be created with any text editor and is often used with free-form languages. Most examples of ASCII art require a fixed-width font (non-proportional fonts, as on a traditional typewriter) such as Courier for presentation. Among the oldest known examples of ASCII art are the creations by computer-art pioneer Kenneth Knowlton from around 1966, who was working for Bell Labs at the time. “Studies in Perception I” by Ken Knowlton and Leon Harmon from 1966 shows some examples of their early ASCII art. ASCII art was invented, in large part, because early printers often lacked graphics ability and thus characters were used in place of graphic marks. Also, to mark divisions between different print jobs from different users, bulk printers often used ASCII art to print large banners, making the division easier to spot so that the results could be more easily separated by a computer operator or clerk. ASCII art was also used in an early e-mail when images could not be embedded. You can find out more about them. [Source : Wiki](https://en.wikipedia.org/wiki/ASCII_art).<br />
Our project is to convert input image from user and generate the corresponding ASCII output image.<br />
## Installation
1. Create a `pipenv`-managed virtual environment and install the latest version of the package installed: 
```
pipenv install -i https://test.pypi.org/simple/ asciiarttools
```
2. Activate the virtual environment: 
```
pipenv shell
```
3. Create a Python program file that imports the package and uses it, e.g. 
```
from asciiarttools import asciiarttools
```
and then call the functions, for example:
```
asciiarttools.convertImageToAsciiImage('cat1.jpg', 'output.png')
```


## Functions

1. Generate a plain ASCII image from input image
```
convertImageToAscii(fileName, cols, scale, moreLevels, debug,outFile)
```

Call convertImageToAscii function and pass the input file name, columns number, scale, level of grayscale, debug mode, and output file name. The default value is cols=80, scale=0.43, moreLevels=True,debug=False,outFile="out.txt".

2. Generate a colored ASCII image from input image
```
convertImageToAsciiImage(inputImage, outFile='output.png')
```
Call convertImageToAsciiImage function and pass the input file and output file. The default is outFile='output.png'

3. Adjust the brightness of a generated ASCII text image
```
adjustASCIIBrightness(art, value, moreLevels=True)
```
Call adjustASCIIBrightness function and pass the input ASCII art file, magnitude in adjusting brightness, and level of grayscale. The default is moreLevels=True. The range for value is [-1,1], where value approaches 1 means increases the brightness, and value approaches -1 means decreases the brightness.

4. Adjust the contrast of a generated ASCII text image
```
adjustASCIIContrast(art, value, moreLevels=True)
```
Call adjustASCIIContrast function and pass the input ASCII art file, magnitude in adjusting contrast, and level of grayscale. The default is moreLevels=True.The range for value is [-1,1], where value approaches 1 means sharpen the contrast, and value approaches -1 means soften the contrast.<br />

## How to Contribute
1. Clone the repository
```
git clone https://github.com/software-students-fall2022/python-package-exercise-project-3-team-8.git
```
2. Set up the environment
```
pipenv shell
```
3. Install the dependencies
```
pipenv install --dev
```
4. Modify the code
5. To build the package, run the following command:
```
python -m build
```
6. To test the package, run the following command:
```
python -m pytest
```

## Link to Example Python Program
[Example Program](https://github.com/software-students-fall2022/python-package-exercise-project-3-team-8/blob/main/src/asciiarttools/__main__.py)
## Link to package's page on the PyPI website
https://test.pypi.org/project/asciiarttools/



## Contributors
[Adler, David](https://github.com/dov212)

[Fan, Wenni](https://github.com/fwenni)

[Ma, Michael](https://github.com/mma01us)

[Zhang, Jiawei](https://github.com/jiawei-zhang-a)

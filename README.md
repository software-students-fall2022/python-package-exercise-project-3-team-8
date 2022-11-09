![Python build & test](https://github.com/software-students-fall2022/python-package-exercise-project-3-team-8/actions/workflows/python-package.yml/badge.svg)

# Convert Image to ASCII
ASCII art is a graphic design technique that uses computers for presentation and consists of pictures pieced together from the 95 printable (from a total of 128) characters defined by the ASCII Standard from 1963 and ASCII compliant character sets with proprietary extended characters (beyond the 128 characters of standard 7-bit ASCII). The term is also loosely used to refer to text-based visual art in general. ASCII art can be created with any text editor and is often used with free-form languages. Most examples of ASCII art require a fixed-width font (non-proportional fonts, as on a traditional typewriter) such as Courier for presentation. Among the oldest known examples of ASCII art are the creations by computer-art pioneer Kenneth Knowlton from around 1966, who was working for Bell Labs at the time. “Studies in Perception I” by Ken Knowlton and Leon Harmon from 1966 shows some examples of their early ASCII art. ASCII art was invented, in large part, because early printers often lacked graphics ability and thus characters were used in place of graphic marks. Also, to mark divisions between different print jobs from different users, bulk printers often used ASCII art to print large banners, making the division easier to spot so that the results could be more easily separated by a computer operator or clerk. ASCII art was also used in an early e-mail when images could not be embedded. You can find out more about them. [Source : Wiki](https://en.wikipedia.org/wiki/ASCII_art).<br />
Our project is to convert input image from user and generate the corresponding ASCII output image.<br />
## Installation
1.
2.
3.
4.
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
Call adjustASCIIBrightness function and pass the input ASCII art file, value for magnitude in adjusting brightness, and level of grayscale. The default is moreLevels=True. The range for value is [-1,1], where value approaches 1 means increase the brightness, and value approaches -1 means decrease the brightness.

4. Adjust the brightness of a generated ASCII text image
```
adjustASCIIContrast(art, value, moreLevels=True)
```
Call adjustASCIIContrast function and pass the input ASCII art file, value for magnitude in adjusting contrast, and level of grayscale. The default is moreLevels=True.The range for value is [-1,1], where value approaches 1 means sharpen the contrast, and value approaches -1 means soften the contrast.<br />

## How to build and test this package
1. To build the package, run the following command:
```
python -m pytest
```
2. To test the package, run the following command:
```
python -m pytest
```

## Link to Example Python Program

## Link to package's page on the PyPI website




## Contributors
- Adler, David
- Fan, Wenni https://github.com/fwenni
- Ma, Michael
- Zhang, Jiawei https://github.com/jiawei-zhang-a

## How this package was created

```
python-package-example/
  |____README.md
  |____LICENSE
  |____pyproject.toml
  |____tests
  |____src
    |____asciiarttools
      |______init__.py
      |______main__.py
      |____asciiarttools.py
```



1. Four main functions in `src`/`pyasciiart`/`asciiArt.py` 
2. Optionally add a `__main__.py` file to the package directory, if you want to be able to run the package as a script from the command line, e.g. `python -m pyasciiart`.
3. Build the project by running `python -m build` from the same directory where the `pyproject.toml` file is located.

4. Verify that the built `.tar` archive has the files you expect your package to have (including any important non-code files) by running the command: `tar --list -f dist/pyasciiart-0.0.1.tar.gz`, where `pyasciiart-0.0.1` is replaced with your own package name 
5. Create an account on [TestPyPI](https://test.pypi.org/) where one can upload to a test repository instead of the production PyPI repo.
6. Create a [new API token](https://test.pypi.org/manage/account/#api-tokens) on TestPyPI with the "Scope" set to “Entire account”. Save a copy of the token somewhere safe.
7. [Upload your package](examplepackagefb1258) to the TestPyPI repository using twine, e.g. `twine upload -r testpypi dist/*`
8. twine will output the URL of your package on the PyPI website - load that URL in your web browser to see your packaged published - make sure the `README.md` file looks nice on the web site.

Every time you change the code in your package, you will need to rebuild and reupload it to PyPI. You will need to build from a clean slate and update the version number to achieve this:

1. delete the autogenerated `dist` directory
2. delete the autogenerated `src/*.egg-info` directory
3. update the version number in `pyproject.toml` and anywhere else it is mentioned (do a find/replace)
4. build the package again with `python -m build`
5. upload the package again with `twine upload -r testpypi dist/*`

Repeat as many times as necessary until the package works as expected. Once complete, upload to the real PyPI instead of the TestPyPI repository.

If updating version numbers is tedious, you may consider using [bumpver](https://pypi.org/project/bumpver/#configuration-setup) - a tool that can automate some parts of updating version numbers.

## How to install and use this package

Try [installing and using your package](https://packaging.python.org/en/latest/tutorials/packaging-projects/#installing-your-newly-uploaded-package) in a separate Python project:

1. Create a `pipenv`-managed virtual environment and install the latest version of your package installed: `pipenv install -i https://test.pypi.org/simple/ examplepackagefb1258==0.0.7`. (Note that if you've previously created a `pipenv` virtual environment in the same directory, you may have to delete the old one first. Find out where it is located with the `pipenv --venv` command.)
1. Activate the virtual environment: `pipenv shell`.
2. Create a Python program file that imports your package and uses it, e.g. `from pyasciiart import asciiarttools` and then `print(asciiarttools.convertImageToAsciiImage('cat1.jpg', 'output.png')
())` 
3. Run the program: `python3 __main__.py`.
4. Exit the virtual environment: `exit`.

Try running the package directly:

1. Create and activate up the `pipenv` virtual environment as before.
2. Run the package directly from the command line: `python3 -m pyasciiart`. This should run the code in the `__main__.py` file.
3. Exit the virtual environment.

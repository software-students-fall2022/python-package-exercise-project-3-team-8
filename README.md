# Convert Image to ASCII
ASCII art is a graphic design technique that uses computers for presentation and consists of pictures pieced together from the 95 printable (from a total of 128) characters defined by the ASCII Standard from 1963 and ASCII compliant character sets with proprietary extended characters (beyond the 128 characters of standard 7-bit ASCII). The term is also loosely used to refer to text-based visual art in general. ASCII art can be created with any text editor and is often used with free-form languages. Most examples of ASCII art require a fixed-width font (non-proportional fonts, as on a traditional typewriter) such as Courier for presentation. Among the oldest known examples of ASCII art are the creations by computer-art pioneer Kenneth Knowlton from around 1966, who was working for Bell Labs at the time. “Studies in Perception I” by Ken Knowlton and Leon Harmon from 1966 shows some examples of their early ASCII art. ASCII art was invented, in large part, because early printers often lacked graphics ability and thus characters were used in place of graphic marks. Also, to mark divisions between different print jobs from different users, bulk printers often used ASCII art to print large banners, making the division easier to spot so that the results could be more easily separated by a computer operator or clerk. ASCII art was also used in an early e-mail when images could not be embedded. You can find out more about them. [Source : Wiki](https://en.wikipedia.org/wiki/ASCII_art)


## How this package was created

1. [Install pipenv](https://packaging.python.org/en/latest/tutorials/managing-dependencies/#managing-dependencies), [build](https://packaging.python.org/en/latest/tutorials/packaging-projects/#generating-distribution-archives), and [twine](https://packaging.python.org/en/latest/key_projects/#twine) if not already installed.
2. create directory structure for the package like that below, where `pyasciiart` is replaced with your package's name. This name must be uniquely yours when uploaded to [PyPI](https://pypi.org/). Better to avoid hyphens or underline characters (`-` or `_`) in the package name, as these can create problems when importing. The parent directory name (the repository name) - `python-package-example` in this case - is not relevant to the package name.

```
python-package-example/
  |____README.md
  |____LICENSE
  |____pyproject.toml
  |____tests
  |____src
    |____pyasciiart
      |______init__.py
      |______main__.py
      |____asciiArt.py
```

3. Make `__init__.py` an empty file.
4. Enter the text of a [copyright license of your choosing](https://choosealicense.com/) into `LICENSE`.
5. Add settings in `pyproject.toml` suitable for a `setuptools`-based build and add metadata fields to this file - see the example in this repository.
6. Four main functions in `src`/`pyasciiart`/`asciiArt.py` 
7. Optionally add a `__main__.py` file to the package directory, if you want to be able to run the package as a script from the command line, e.g. `python -m pyasciiart`.
8. Build the project by running `python -m build` from the same directory where the `pyproject.toml` file is located.
9. Verify that the built `.tar` archive has the files you expect your package to have (including any important non-code files) by running the command: `tar --list -f dist/examplepackagefb1258-0.0.7.tar.gz`, where `examplepackagefb1258-0.0.7` is replaced with your own package name and version.
10. Create an account on [TestPyPI](https://test.pypi.org/) where one can upload to a test repository instead of the production PyPI repo.
11. Create a [new API token](https://test.pypi.org/manage/account/#api-tokens) on TestPyPI with the "Scope" set to “Entire account”. Save a copy of the token somewhere safe.
12. [Upload your package](examplepackagefb1258) to the TestPyPI repository using twine, e.g. `twine upload -r testpypi dist/*`
13. twine will output the URL of your package on the PyPI website - load that URL in your web browser to see your packaged published - make sure the `README.md` file looks nice on the web site.

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
1. Create a Python program file that imports your package and uses it, e.g. `from examplepackagefb1258 import wisdom` and then `print(wisdom.get())` (replace `wisdom` and `get()` with any module name and function that exists in your package) .
1. Run the program: `python3 my_program_filename.py`.
1. Exit the virtual environment: `exit`.

Try running the package directly:

1. Create and activate up the `pipenv` virtual environment as before.
2. Run the package directly from the command line: `python3 -m examplepackagefb1258`. This should run the code in the `__main__.py` file.
3. Exit the virtual environment.

from setuptools import setup

setup(name             = 'nbref',
      version          = '0.1.0',
      author           = 'Bill Spotz',
      author_email     = 'wfspotz@sandia.gov',
      packages         = ['nbref'],
      scripts          = ['scripts/nb2html.py'],
      url              = 'https://github.com/wfspotz/nb2html',
      license          = 'LICENSE',
      description      = 'Convert Jupyter notebooks to HTML with references',
      long_description = open('README.md').read(),
      long_description_content_type = "text/markdown",
      classifiers      = ("Development Status :: 3 - Alpha",
                          "Programming Language :: Python :: 2",
                          "Programming Language :: Python :: 3",
                          "License :: OSI Approved :: BSD License",
                          "Operating System :: OS Independent"),
      install_requires = ["nbconvert",
                          "nbformat",
                          "traitlets",
                          "pypandoc",
                          "pandoc-citeproc"]
      )

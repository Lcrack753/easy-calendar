from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'An easy calendar object for heat map and html template'
LONG_DESCRIPTION = 'Multiple functions that make easy calendars, It works for django projects too'

# Setting up
setup(
    name="easy-calendar",
    version=VERSION,
    author="Lcarck753 (Lucio Carnero)",
    author_email="<luxiocarnero@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'calendar', 'django', 'easy calendar', 'easy dates'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
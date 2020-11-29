'''
setup script
'''

from setuptools import setup
from packaging import version

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    install_requires = f.read().splitlines()

try:
    import cv2
    ver = cv2.__version__
    if version.parse(ver) >= version.parse('4.4.0'):
        print('Using system provided opencv')
        install_requires.remove('opencv-python')
    else:
        print('Using opencv-python')
    print('Required packages:', install_requires)

except ImportError as ex:
    print('Using opencv-python')

setup(
        name = 'image_extraction',
        version = '0.0.1',
        author = 'Randolph Sapp',
        description = 'Rip info and images from PDF tables',
        long_description=long_description,
        long_description_content_type="text/markdown",
        url = 'https://github.com/tsledge07/csc480-oracle-bone',
        packages = ['image_extraction'],
        scripts = ['pdfripper.py',
                   'pdftopng.py',
                   'pdfpostproc.py'],
        python_requires = '>=3.6',
        install_requires = install_requires,
)

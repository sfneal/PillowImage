import os
from setuptools import setup, find_packages

NAME = 'PillowImage'

DESCRIPTION = 'Pillow wrapper for quick image alterations.'

LONG_DESCRIPTION = """
Pure Python Pillow package wrapper.
"""


def get_version(package_name, version_file='_version.py'):
    """
    Retrieve the package version from a version file in the package root.

    :param package_name:
    :param version_file: version file name (inside package root)
    :return: package version
    """
    filename = os.path.join(os.path.dirname(__file__), package_name, version_file)
    with open(filename, 'rb') as fp:
        return fp.read().decode('utf8').split('=')[1].strip(" \n'")


setup(
    name=NAME,
    version=get_version(NAME),
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[
        'reportlab>=3.5.19',
        'Pillow>=7.0',
        'PyBundle>=1.0.6',
    ],
    include_package_data=True,
    url='https://github.com/sfneal/PillowImage',
    license='MIT',
    author='Stephen Neal',
    author_email='stephen@stephenneal.net',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
)

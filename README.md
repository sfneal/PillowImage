# PillowImage

[![Build Status](https://travis-ci.com/sfneal/PillowImage.svg?branch=master)](https://travis-ci.com/sfneal/PillowImage)
[![PyPi version](https://img.shields.io/pypi/v/PillowImage)](https://pypi.org/project/PillowImage)
[![PyPi Python support](https://img.shields.io/pypi/pyversions/PillowImage)](https://pypi.org/project/PillowImage)
[![PyPi downloads per month](https://img.shields.io/pypi/dm/PillowImage)](https://pypi.org/project/PillowImage)
[![PyPi license](https://img.shields.io/pypi/l/PillowImage)](https://pypi.org/project/PillowImage)
[![StyleCI](https://github.styleci.io/repos/179334000/shield?branch=master)](https://github.styleci.io/repos/179334000?branch=master)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/sfneal/PillowImage/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/sfneal/PillowImage/?branch=master)

Pillow wrapper for quick image alterations.

Package features:

* Resize, rotate, stretch & scale images
* Draw text
* Insert images
* Centering & scaled image/text placement

## Propose
PillowImage is a Pillow wrapper that provides a simple interface for basic image manipulation in Python scripts & applications.

## Usage
Add text or images to a blank canvas or existing images

### Adding a centered Watermark
```python
with PillowImage(img=image_path) as pi:
    pi.draw_img(watermark path, opacity=0.08, rotate=30, x='center', y='center')
    image = pi(destination=output_directory, file_name='output')
```

### Adding text to an image
```python
with PillowImage(img=image_path) as pi:
	pi.draw_text('Here is the first text', y=10, opacity=50)
	pi.draw_text('Here is the second text', y=50, opacity=50)
   image = pi(destination=output_directory, file_name='output')
```

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

In order to utilize this PillowImage you will need to have a Python (3.6+) interpreter installed on your machine.

#### PyPi installation
```
pip install PillowImage
```

#### PyPi update
```
pip install --upgrade --no-cache-dir PillowImage
```

### Project Structure

```
├── PillowImage
│   ├── __init__.py
│   ├── _version.py
│   ├── font
│   │   ├── __init__.py
│   │   ├── Vera.ttf
│   │   └── register.py
│   ├── pillow.py
│   └── utils.py
```

## Contributing

Please read [CONTRIBUTING.md](https://github.com/sfneal/PillowImage/CONTRIBUTING.md) for details on our code of 
conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/sfneal/PillowImage). 

## Authors

* **Stephen Neal** - *Initial work* - [PillowImage](https://github.com/sfneal)

## License

This project is licensed under the Apache License - see the [LICENSE.md](LICENSE.md) file for details

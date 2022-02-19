# image-optimizer-cli

A simple CLI application written in Python to optimize images. You can use it from the command line after installing it. Executable name is `image-optimizer`.

## Installation

Run:&nbsp; ``pip install image-optimizer-cli``

## Usage

* Show help: ``image-optimizer -h``

* Optimize single image: ``image-optimizer -p /path/to/image.jpg``

* Optimize all images in a folder: ``image-optimizer -p /path/to/images/``

* Optimize all images in a folder recursively: ``image-optimizer -p /path/to/images/ -r``

* Optimize a number of images: ``image-optimizer -p /path/to/images/ -n 10``

* Optimize with custom quality: ``image-optimizer -p /path/to/images/ -q 30``

## Parameters

* ``-h, --help:`` Show help.

* ``-p, --path:`` Path to the image or folder to optimize. Defaults to the current directory if not specified.

* ``-r, --recursive:`` Optimize all images in a folder recursively. Defaults to False if not specified.

* ``-n, --number:`` Optimize a number of images. Defaults to all images in the folder if not specified.

* ``-q, --quality:`` Optimize with custom quality. Defaults to 80 if not specified.

## Important notes

* BACKUP YOUR IMAGES BEFORE OPTIMIZING! All images will be overwritten with optimized versions.

* This is a simple CLI application. It is not meant to be a full-featured image optimizer.

* Relative and absolute paths are supported.

* The quality parameter is a value between 0 and 100.

* The number parameter is a positive integer. And is not required.

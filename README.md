# reciept-merger

This repo contains a simple Python script for making a set of one-page pdf files into a jpg collage of the images of the pdf files  

## Pre-requisites

*Pyton 3* installed and executable `python` pointing to this  

Installequired libraries:
```
$ pip install pdf2image
$ pip install Pillow
```

You probably need to install `poppler` in order to use `pdf2image`, see instructions here: https://github.com/Belval/pdf2image.  
For MacOS it is available with `brew`:
```
$ brew install poppler
```

## Usage

```
./run.sh <input folder> <output file name>
```
where `<input folder>` is the folder containing the pdf files. For instance:
```
$ ./run.sh /Users/frode/reciepts collage.jpg
```

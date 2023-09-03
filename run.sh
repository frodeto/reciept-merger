#!/bin/bash

INPUT_FOLDER=$1
OUTPUT_IMAGE_NAME=$2

[ $# -ne 2 ] && { echo "Usage: $0 <input folder> <output file name>"; exit 1; }

echo using pyton `which python`
python pdfs_to_collage.py $INPUT_FOLDER $OUTPUT_IMAGE_NAME

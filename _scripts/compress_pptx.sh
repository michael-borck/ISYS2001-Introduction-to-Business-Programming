#!/bin/bash

# Check if source directory and output zip file are provided
if [ $# -ne 2 ]; then
    echo "Usage: $0 <source_directory> <output_zip_file>"
    exit 1
fi

SOURCE_DIR="$1"
OUTPUT_ZIP="$2"

# Ensure source directory exists
if [ ! -d "$SOURCE_DIR" ]; then
    echo "Error: Source directory does not exist"
    exit 1
fi

# Find and zip only .pptx files
find "$SOURCE_DIR" -type f -name "*.pptx" | zip "$OUTPUT_ZIP" -@

echo "Compression complete. Output file: $OUTPUT_ZIP"

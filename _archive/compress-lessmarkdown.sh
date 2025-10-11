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

# Compress the directory, excluding .qmd and .md files
zip -r "$OUTPUT_ZIP" "$SOURCE_DIR" -x "*.qmd" "*.md"

echo "Compression complete. Output file: $OUTPUT_ZIP"

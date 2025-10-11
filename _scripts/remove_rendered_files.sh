#!/bin/bash

# Check if a directory was provided as an argument
if [ -z "$1" ]; then
    # No directory provided, use the current directory
    TARGET_DIR="."
else
    # Use the provided directory
    TARGET_DIR="$1"
fi

# Find and remove PDF, HTML, DOCX, and PPTX files
find "$TARGET_DIR" -type f \( -name "*.pdf" -o -name "*.html" -o -name "*.docx" -o -name "*.pptx" \) -exec rm -f {} \;

echo "Removed all PDF, HTML, DOCX, and PPTX files from $TARGET_DIR"

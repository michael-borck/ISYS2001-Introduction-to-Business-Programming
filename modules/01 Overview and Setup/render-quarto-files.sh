#!/bin/bash

# Function to process files
process_file() {
    local file="$1"
    echo "Rendering: $file"
    quarto render "$file"
}

# Find and process .md and .qmd files
find . -type f \( -name "*.md" -o -name "*.qmd" \) -print0 | while IFS= read -r -d '' file; do
    process_file "$file"
done

echo "Rendering complete!"

#!/bin/bash

# Characters to remove
CHARS='[\\/:*?"<>|]'

# Find and rename files recursively
find . -depth | while IFS= read -r file; do
  # Get the directory and base name of the file
  dir=$(dirname "$file")
  base=$(basename "$file")
  
  # Check if the base name contains any of the characters
  if [[ $base =~ $CHARS ]]; then
    # Remove the characters from the base name
    new_base=$(echo "$base" | sed 's/[\\\/:*?"<>|]//g')
    
    # Rename the file
    mv "$dir/$base" "$dir/$new_base"
  fi
done

echo "Renaming completed."


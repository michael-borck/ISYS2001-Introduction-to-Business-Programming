#!/bin/bash

# Initialize the counter
counter=1

# Loop through the files in the directory
for file in $(ls | sort); do
  # Extract the filename without the XX_ prefix
  filename=$(echo $file | cut -d'_' -f2-)
  
  # Format the counter to be two digits with a leading zero if necessary
  new_number=$(printf "%02d" $counter)
  
  # Create the new filename
  new_filename="${new_number}_${filename}"
  
  # Rename the file
  mv "$file" "$new_filename"
  
  # Increment the counter
  ((counter++))
done

echo "Renumbering complete!"


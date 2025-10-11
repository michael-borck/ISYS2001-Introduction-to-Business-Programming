import os
import argparse
import re

def concatenate_md_files(directory, output_file, pattern=None, exclude_pattern=None):
    with open(output_file, 'w') as outfile:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith('.md'):
                    # Include files if they match the pattern or if no pattern is provided
                    if (pattern is None or re.search(pattern, file)) and (exclude_pattern is None or not re.search(exclude_pattern, file)):
                        file_path = os.path.join(root, file)
                        with open(file_path, 'r') as infile:
                            outfile.write(infile.read() + "\n\n")  # Concatenate with some spacing
                        print(f"Added: {file_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Concatenate .md files recursively.")
    parser.add_argument('directory', help="The directory to search for .md files.")
    parser.add_argument('output_file', help="The output file name (e.g., combined.md).")
    parser.add_argument('--pattern', help="Optional pattern to match in the .md filenames.", default=None)
    parser.add_argument('--exclude', help="Optional pattern to exclude from the .md filenames.", default=None)

    args = parser.parse_args()
    concatenate_md_files(args.directory, args.output_file, args.pattern, args.exclude)
    print(f"All .md files matching pattern '{args.pattern}' and excluding pattern '{args.exclude}' have been concatenated into {args.output_file}")


import sys

def split_file(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    current_file = None
    current_content = []

    for line in lines:
        if line.startswith('# '):
            if current_file:
                # Write the previous file
                with open(current_file, 'w') as outfile:
                    outfile.writelines(current_content)
                current_content = []

            # Set new file name
            current_file = line[2:].strip()

        current_content.append(line)

    # Write the last file
    if current_file:
        with open(current_file, 'w') as outfile:
            outfile.writelines(current_content)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python split_file.py <input_file>")
    else:
        input_file = sys.argv[1]
        split_file(input_file)

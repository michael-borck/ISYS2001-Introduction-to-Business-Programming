import nbformat as nbf
import sys

def extract_python_code_blocks(markdown_file):
    """
    Extracts Python code blocks from a Markdown file.
    
    Args:
    markdown_file (str): Path to the markdown file.
    
    Returns:
    List[str]: A list of Python code blocks as strings.
    """
    code_blocks = []
    inside_code_block = False
    current_block = []
    
    with open(markdown_file, 'r') as file:
        for line in file:
            if line.startswith("```python"):
                inside_code_block = True
                continue
            if line.startswith("```") and inside_code_block:
                inside_code_block = False
                code_blocks.append("\n".join(current_block))
                current_block = []
                continue
            if inside_code_block:
                current_block.append(line.rstrip())
    
    return code_blocks

def create_notebook_with_code_blocks(code_blocks, notebook_name):
    """
    Creates a Jupyter notebook with each Python code block in a separate cell.
    
    Args:
    code_blocks (List[str]): List of Python code blocks.
    notebook_name (str): The name of the output notebook file.
    """
    nb = nbf.v4.new_notebook()
    cells = []
    
    for block in code_blocks:
        cell = nbf.v4.new_code_cell(block)
        cells.append(cell)
    
    nb['cells'] = cells
    
    with open(notebook_name, 'w') as f:
        nbf.write(nb, f)
        
    print(f"Notebook '{notebook_name}' created successfully with {len(code_blocks)} cells.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <markdown_file> <notebook_name>")
        sys.exit(1)
    
    markdown_file = sys.argv[1]
    notebook_name = sys.argv[2]
    
    code_blocks = extract_python_code_blocks(markdown_file)
    create_notebook_with_code_blocks(code_blocks, notebook_name)

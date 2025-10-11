#!/usr/bin/env python
# coding: utf-8

from os import makedirs, path
from shutil import copyfile
import json
import copy

# hide existing code and results and add an empty code cell or hide answer to questions
def release_guided_workshop_file(directory, filepath):

    new_filepath = directory + filepath
    makedirs(path.dirname(new_filepath), exist_ok=True)
    copyfile(filepath, new_filepath)
    json_data = ""

    with open(new_filepath, encoding='utf-8', mode='r') as f:
        json_data = json.load(f)

    cells = json_data['cells']

    new_cells = []

    for i, cell in enumerate(cells):
        metadata = cell['metadata']
        if "tags" in metadata.keys():

            # find the marker (and let the magic begin)
            if "delete" in metadata['tags']:

                if not "cell" in metadata['tags']:

                    # add a new collapsed heading for SOLUTION
                    solution_markdown_cell = {}
                    solution_markdown_cell["cell_type"] = "markdown"
                    solution_markdown_cell["metadata"] = {}
                    solution_markdown_cell["metadata"]["heading_collapsed"] = True
                    solution_markdown_cell["source"] = ['###### <span style="color:green;">SOLUTION <small>(Click the arrow on the left side if a hint is needed)</small></span>']
                    
                    # there are to types of cells:
                    # - answer cells, written in Markdown
                    # - code cells, written in Python with outputs
                    
                    # add answer cell
                    if cell["cell_type"] == "markdown":
                        new_cells.append(solution_markdown_cell)
                        new_cells.append(cell)
                    # cell with code
                    else:
                        solution_code_cell = copy.deepcopy(cell)
                        solution_code_cell["execution_count"] = None
                        index = solution_code_cell['metadata']['tags'].index("delete")
                        del solution_code_cell['metadata']['tags'][index]
                        solution_code_cell['metadata']['deletable'] = False
                        solution_code_cell['metadata']['editable'] = False
                        solution_code_cell['metadata']['hidden'] = True
                        solution_code_cell['metadata']['run_control'] = {}
                        solution_code_cell['metadata']['run_control']["frozen"] = True
                        if "outputs" in solution_code_cell and len(solution_code_cell['outputs']) > 0 and "execution_count" in solution_code_cell['outputs'][0]:
                            solution_code_cell['outputs'][0]["execution_count"] = None

                        # empty original cell
                        cell['source'] = []
                        cell['outputs'] = []

                        # add all cells ot the notebook's cell list
                        new_cells.append(cell)
                        new_cells.append(solution_markdown_cell)
                        new_cells.append(solution_code_cell)

        else:
            new_cells.append(cell)

        if "code" in cell["cell_type"]:
            cell['execution_count'] = None

    json_data['cells'] = new_cells
    main_metadata = json_data['metadata']
    if "celltoolbar" in main_metadata.keys():
        del main_metadata['celltoolbar']
        
    with open(new_filepath, encoding='utf-8', mode='w') as outfile:
        json.dump(json_data, outfile, indent=4)


filelist = []
filelist.append("00_Jupyter_Notebook_and_Python_basics.ipynb")

guided_workshop_output_directory = "/home/michael/Projects/out/"

for filepath in filelist:
    release_guided_workshop_file(guided_workshop_output_directory, filepath)

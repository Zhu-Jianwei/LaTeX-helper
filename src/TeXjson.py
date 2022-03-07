import json
import re

from utils.fileio import *


def generate_json(dir_path: str, json_path: str = None):
    file_dict = get_tex_list_recursive(dir_path)
    print(file_dict)
    tex_dict = {}
    describe_dict = {}
    for file, file_path in file_dict.items():
        with open(file_path) as f:
            text_data = f.read()
            description = re.match(r"%\s*description\s*:\s*(.*)", text_data)
            if (description == None):
                describe_dict[file] = 'None'
            else:
                print(description.group(0))
                description = description.group(1)
                describe_dict[file] = description
            single_tex_dict = {
                'prefix': os.path.splitext(file)[0],
                'body': text_data,
                'description': description
            }
            fragment = os.path.splitext(file)[0].replace('_', ' ')
            tex_dict[fragment] = single_tex_dict

    json_str = json.dumps(tex_dict)
    with open(json_path, 'w') as f:
        f.write(json_str)

    describe_str = json.dumps(describe_dict)
    with open('description.json', 'w') as f:
        f.write(describe_str)


if __name__ == '__main__':
    generate_json(
        '.',
        "/mnt/c/Users/86181/AppData/Roaming/Code/User/snippets/latex.json")

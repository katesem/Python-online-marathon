import json
import logging

def print_file(file):
    with open(file, 'r') as f:
        print(f.read())
        
def parse_user(output_file, *input_files):
    names_list, r  = [], []
    for file in input_files:
        try:
            with open(file) as f:
                for i in json.load(f):
                    if i.get('name') and i['name'] not in names_list :
                        names_list.append(i['name'])
                        r.append(i)
        except :
            logging.basicConfig (filename='app.log', filemode='w+', format='%(name)s - %(levelname)s - %(message)s', level = logging.ERROR)
            logging.error(f"File {file} doesn't exists")
    with open(output_file,'w+') as write_file:
                json.dump(r,write_file, indent=4)

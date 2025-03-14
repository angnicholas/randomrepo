import os
import json
import pickle
from pathlib import Path

'''
  _____  _  _       
 |  ___|(_)| |  ___ 
 | |_   | || | / _ \
 |  _|  | || ||  __/
 |_|    |_||_| \___|
                    
'''

def make_dir_for_file(*filepaths):
    for filepath in filepaths:
        filepath = str(filepath)
        if not filepath:
            continue
        if not os.path.isdir(x := str(Path(filepath).parent)):
            os.makedirs(x)

def load_json(filepath):
    filepath = str(filepath)
    with open(filepath, mode='r') as f:
        return json.load(f)

def save_json(obj, filepath):
    filepath = str(filepath)
    make_dir_for_file(filepath)
    with open(filepath, mode='w') as f:
        json.dump(obj, f)
        
def load_pickle(filename):
    filename = str(filename)
    with open(filename, mode='rb') as f:
        return pickle.load(f)

def save_pickle(obj, filename):
    filename = str(filename)
    make_dir_for_file(filename)
    with open(filename, mode='wb') as f:
        pickle.dump(obj, f)

def load_text(filename):
    filename = str(filename)
    with open(filename, mode='r') as f:
        return f.read()

def save_text(obj, filename):
    filename = str(filename)
    make_dir_for_file(filename)
    with open(filename, mode='w') as f:
        f.write(obj)

def cached(path_to_cache, method_to_make):
    try:
        return load_pickle(path_to_cache)
        #print('we are able to use the pickle')
    except:
        value = method_to_make()
        save_pickle(value, path_to_cache)
        return value
'''
  ____              _    _                               _         _    _               
 |  _ \  _ __  ___ | |_ | |_  _   _         _ __   _ __ (_) _ __  | |_ (_) _ __    __ _ 
 | |_) || '__|/ _ \| __|| __|| | | | _____ | '_ \ | '__|| || '_ \ | __|| || '_ \  / _` |
 |  __/ | |  |  __/| |_ | |_ | |_| ||_____|| |_) || |   | || | | || |_ | || | | || (_| |
 |_|    |_|   \___| \__| \__| \__, |       | .__/ |_|   |_||_| |_| \__||_||_| |_| \__, |
                              |___/        |_|                                    |___/ 
'''

def pretty_print_dict(dictionary):
    outputs = []
    max_len = max([len(i) for i in dictionary])
    for k, v in dictionary.items():
        n_spaces = max_len - len(k)
        spaces = ' ' * n_spaces
        outputs.append(f'{spaces} {k} = {v}')
    output_string = '\n'.join(outputs)
    return output_string

def pretty_print_list_of_tuples(list_of_tuples):
    outputs = []
    max_len = max([len(i[0]) for i in list_of_tuples])
    for k, v in list_of_tuples:
        if not k and not v:
            outputs.append('')
            continue
        n_spaces = max_len - len(k)
        spaces = ' ' * n_spaces
        outputs.append(f'{spaces} {k} = {v}')
    output_string = '\n'.join(outputs)
    return output_string
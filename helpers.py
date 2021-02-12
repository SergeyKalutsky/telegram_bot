from keyboard.supporting_elements import return_menu

def prev_path(path):
    return '/'.join(path.split('/')[:-2]) + '/'

def set_return_path(data):
    for key, val in return_menu:
        if key in data['path']:
            if val == '':
                data['path'] = '/'.join(data['path'].split('/')[:-2])+'/'
            else:
                data['path'] = val
            return data
    return data
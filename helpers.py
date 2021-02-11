from keyboard.supporting_elements import return_menu

def prev_path(path):
    return '/'.join(path.split('/')[:-2]) + '/'

def set_return_path(data):
    for key, val in return_menu.items():
        if key in data['path']:
            data['path'] = val
            break
        
    return data
import uuid


def prev_path(path):
    return '/'.join(path.split('/')[:-2]) + '/'


def calculate_area(data):
    live = int(data['/Общие сведения/Площадь/Жилая/'])
    comm = int(data['/Общие сведения/Площадь/Общая/'])
    return comm - live


def make_img_fname(ext='.jpg'):
    return str(uuid.uuid4()) + ext


def put_key_json(path, data, val, photo=False):
    keys = path[1:-1].split('/')
    for i in range(len(keys)-1):
        if keys[i] not in data:
            data[keys[i]] = {keys[i+1]: {}}
        data = data[keys[i]]

    if photo:
        if keys[-1] not in data or type(data[keys[-1]]) == dict:
            data[keys[-1]] = [val]
        else:
            data[keys[-1]].append(val)
    else:
        data[keys[-1]] = val

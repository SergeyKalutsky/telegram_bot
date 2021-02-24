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

    if not photo:
        for i in range(len(keys)-1):
            if keys[i] not in data:
                data[keys[i]] = {keys[i+1]: {}}
            data = data[keys[i]]
        data[keys[-1]] = val
        
    else:
        if keys[0] not in data['photo']:
            data['photo'][keys[0]] = {}
        data = data['photo'][keys[0]]
        key = '. '.join(keys[1:])
        if key not in data or type(data[key]) == dict:
            data[key] = [val]
        else:
            data[key].append(val)

from copy import copy
import uuid


def prev_path(path):
    return '/'.join(path.split('/')[:-2]) + '/'


def battn_vals(k):
    lst = []
    for val in k.values['inline_keyboard']:
        lst.append(val[0].text)
    return lst


def get_empty_keys(buttons, d):
    not_filled_buttons = []
    for button in buttons:
        if button not in d.keys():
            not_filled_buttons.append(button)
    return not_filled_buttons


def not_filled(path, keyboard, data):
    d = data.__dict__['_copy'].copy()
    buttons = battn_vals(keyboard)
    keys = path[1:-1].split('/')
    # handle starting position
    if not keys[0]:
        return get_empty_keys(buttons, d)

    for key in keys:
        if key not in d:
            return buttons
        d = d[key]

    return get_empty_keys(buttons, d)


def make_img_fname(ext='.jpg'):
    return str(uuid.uuid4()) + ext


def put_key_json(path, data, val, photo=False):
    keys = path[1:-1].split('/')

    if photo:
        d = copy(data)
        if keys[0] not in d['photo']:
            d['photo'][keys[0]] = {}
        d = d['photo'][keys[0]]
        key = '. '.join(keys[1:])
        if key not in d or type(d[key]) == dict:
            d[key] = [val]
        else:
            d[key].append(val)

    for i in range(len(keys)-1):
        if keys[i] not in data:
            data[keys[i]] = {keys[i+1]: {}}
        if type(data[keys[i]]) == str:
            data[keys[i]] ={keys[i+1]: {}}
        else:
            data = data[keys[i]]

    if photo:
        data[keys[-1]] = 'photo'
        return
        
    data[keys[-1]] = val


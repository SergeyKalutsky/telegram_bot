def prev_path(path):
    return '/'.join(path.split('/')[:-2]) + '/'

def calculate_area(data):
    live = int(data['/Общие сведения/Площадь/Жилая/'])
    comm = int(data['/Общие сведения/Площадь/Общая/'])
    return comm - live


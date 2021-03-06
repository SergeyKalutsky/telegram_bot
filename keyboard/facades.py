from .building_condition import get_keyboard, keyboard, answer

keyboard = {**keyboard, **{
    '/Фасады/': get_keyboard(['Расположение балконов',
                              'Фасад',
                              'Окна',
                              'Водосток',
                              'Дворовые ворота']),
    '/Фасады/Расположение балконов/': get_keyboard(['В уровне _-_ этажей',
                                                    'Балконы отстутсвуют',
                                                    'Материал',
                                                    'Опирание',
                                                    'Материал ограждений',
                                                    'Наличие декор. элементов',
                                                    'Наличие экрана']),
    '/Фасады/Расположение балконов/Материал/': get_keyboard(['Ж/Б плита', 'Другое']),
    '/Фасады/Расположение балконов/Опирание/': get_keyboard(['На балки, консольно-защемленные',
                                                             'Подкосы металлические',
                                                             'Плита консольно-защемленная',
                                                             'Другое']),
    '/Фасады/Расположение балконов/Материал ограждений/': get_keyboard(['Металл', 'Дерево', 'Кирпич', 'Другое']),
    '/Фасады/Расположение балконов/Наличие декор. элементов/': get_keyboard(['Нет', 'Да']),
    '/Фасады/Расположение балконов/Наличие декор. элементов/Да/': get_keyboard(['Перила', 'Колонны', 'Другое']),
    '/Фасады/Расположение балконов/Наличие экрана/': get_keyboard(['Нет', 'Да']),
    '/Фасады/Расположение балконов/Наличие экрана/Да/': get_keyboard(['Материал']),
    '/Фасады/Расположение балконов/Наличие экрана/Да/Материал/': get_keyboard(['Сталь', 'Поликарбонат', 'Асбестовые плиты', 'Другое']),
    '/Фасады/Фасад/': get_keyboard(['Главный фасад', 'Дворовый фасад', 'Торцевые фасады', 'Цоколь', 'Приямки']),
    '/Фасады/Фасад/Главный фасад/': get_keyboard(['Материал отделки стен',
                                                  'Наличие декоративных элементов',
                                                  'Размеры',
                                                  'Фото',
                                                  'Входные группы',
                                                  'Решетка водосборная',
                                                  'Видео камеры',
                                                  'Отмостка',
                                                  'Пожарная лестница']),
    '/Фасады/Фасад/Главный фасад/Материал отделки стен/': get_keyboard(['Штукатурка и покраска',
                                                                        'Кирпичная кладка',
                                                                        'Керамическая плитка',
                                                                        'Бетон',
                                                                        'Рустованный',
                                                                        'Кирпич крашеный',
                                                                        'Камень',
                                                                        'Другое']),
    '/Фасады/Фасад/Главный фасад/Наличие декоративных элементов/': get_keyboard(['Нет', 'Да']),
    '/Фасады/Фасад/Главный фасад/Наличие декоративных элементов/Да/': get_keyboard(['Пилястры',
                                                                                    'Сандрики',
                                                                                    'Карнизы',
                                                                                    'Медальоны',
                                                                                    'Фигуры',
                                                                                    'Капители',
                                                                                    'Лепнина',
                                                                                    'Криволинейные элементы',
                                                                                    'Другое']),
    '/Фасады/Фасад/Главный фасад/Размеры/': get_keyboard(['Длина', 'Высота']),
    '/Фасады/Фасад/Главный фасад/Фото/': get_keyboard(['Общие фото', 'Фото дефектов с описанием']),
    '/Фасады/Фасад/Главный фасад/Входные группы/': get_keyboard(['Нет',
                                                                 'Ступени',
                                                                 'Ограждения',
                                                                 'Двери',
                                                                 'Козырьки',
                                                                 'Освещение']),
    '/Фасады/Фасад/Главный фасад/Входные группы/Ступени/': get_keyboard(['Высота ступеней', 'Количество ступеней', 'Материал отделки']),
    '/Фасады/Фасад/Главный фасад/Входные группы/Ограждения/': get_keyboard(['Высота', 'Материал', 'Поручни', 'Фото']),
    '/Фасады/Фасад/Главный фасад/Входные группы/Ограждения/Поручни/': get_keyboard(['Размер', 'Материал']),
    '/Фасады/Фасад/Главный фасад/Входные группы/Ограждения/Размер/': get_keyboard(['Длина', 'Ширина', 'Высота']),
    '/Фасады/Фасад/Главный фасад/Входные группы/Двери/': get_keyboard(['Входная дверь', 'Тамбурная дверь']),
    '/Фасады/Фасад/Главный фасад/Входные группы/Двери/Входная дверь/': get_keyboard(['Размеры',
                                                                                     'Материал',
                                                                                     'Наличие декоративных элементов',
                                                                                     'Доводчик',
                                                                                     'Фото']),
    '/Фасады/Фасад/Главный фасад/Входные группы/Двери/Входная дверь/Размеры/': get_keyboard(['Ширина', 'Высота']),
    '/Фасады/Фасад/Главный фасад/Входные группы/Двери/Входная дверь/Материал/': get_keyboard(['Металл', 'Дерево', 'Другое']),
    '/Фасады/Фасад/Главный фасад/Входные группы/Двери/Входная дверь/Наличие декоративных элементов/': get_keyboard(['Да', 'Нет']),
    '/Фасады/Фасад/Главный фасад/Входные группы/Двери/Входная дверь/Доводчик/': get_keyboard(['Да', 'Нет']),
    '/Фасады/Фасад/Главный фасад/Входные группы/Двери/Входная дверь/Фото/': get_keyboard(['Общие фото', 'Фото дефектов с описанием']),
    '/Фасады/Фасад/Главный фасад/Входные группы/Двери/Тамбурная дверь/': get_keyboard(['Нет', 'Да']),
    '/Фасады/Фасад/Главный фасад/Входные группы/Двери/Тамбурная дверь/Да/': get_keyboard(['Размеры', 'Материал', 'Доводчик', 'Фото']),
    '/Фасады/Фасад/Главный фасад/Входные группы/Двери/Тамбурная дверь/Да/Размеры/': get_keyboard(['Ширина', 'Высота']),
    '/Фасады/Фасад/Главный фасад/Входные группы/Двери/Тамбурная дверь/Да/Материал/': get_keyboard(['Металл', 'Дерево', 'Другое']),
    '/Фасады/Фасад/Главный фасад/Входные группы/Двери/Тамбурная дверь/Да/Доводчик/': get_keyboard(['Да', 'Нет']),
    '/Фасады/Фасад/Главный фасад/Входные группы/Двери/Тамбурная дверь/Да/Фото/': get_keyboard(['Общие фото', 'Фото дефектов с описанием']),
    '/Фасады/Фасад/Главный фасад/Входные группы/Козырьки/': get_keyboard(['Материал', 'Размер', 'Фото']),
    '/Фасады/Фасад/Главный фасад/Входные группы/Козырьки/Материал/': get_keyboard(['Сталь оцинкованная',
                                                                                   'Профлист',
                                                                                   'Поликарбонат',
                                                                                   'Ж/Б',
                                                                                   'Другое',
                                                                                   'Отсутствует']),
    '/Фасады/Фасад/Главный фасад/Входные группы/Козырьки/Размер/': get_keyboard(['Длина', 'Ширина']),
    '/Фасады/Фасад/Главный фасад/Входные группы/Козырьки/Фото/': get_keyboard(['Общие фото', 'Фото дефектов с описанием']),
    '/Фасады/Фасад/Главный фасад/Входные группы/Освещение/': get_keyboard(['Да', 'Нет']),
    '/Фасады/Фасад/Главный фасад/Входные группы/Освещение/Да/': get_keyboard(['Тип освещения', 'Фото']),
    '/Фасады/Фасад/Главный фасад/Входные группы/Освещение/Да/Тип освещения/': get_keyboard(['Лампа накаливания',
                                                                                            'Диодное',
                                                                                            'Галогеновое',
                                                                                            'Люминесцентное',
                                                                                            'Другое']),
    '/Фасады/Фасад/Главный фасад/Входные группы/Освещение/Да/Фото/': get_keyboard(['Общие фото', 'Фото дефектов с описанием']),
    '/Фасады/Фасад/Главный фасад/Решетка водосборная/': get_keyboard(['Нет', 'Да']),
    '/Фасады/Фасад/Главный фасад/Решетка водосборная/Да/': get_keyboard(['Размеры', 'Материал', 'Фото']),
    '/Фасады/Фасад/Главный фасад/Решетка водосборная/Да/Размеры/': get_keyboard(['Длина', 'Ширина', 'Глубина приямка']),
    '/Фасады/Фасад/Главный фасад/Решетка водосборная/Да/Материал/': get_keyboard(['Металл', 'Другое']),
    '/Фасады/Фасад/Главный фасад/Решетка водосборная/Да/Фото/': get_keyboard(['Общие фото', 'Фото дефектов с описанием']),
    '/Фасады/Фасад/Главный фасад/Видео камеры/': get_keyboard(['Нет', 'Да']),
    '/Фасады/Фасад/Главный фасад/Отмостка/': get_keyboard(['Нет', 'Да']),
    '/Фасады/Фасад/Главный фасад/Отмостка/Да/': get_keyboard(['Размеры', 'Материал', 'Водоприемный лоток', 'Фото']),
    '/Фасады/Фасад/Главный фасад/Отмостка/Да/Размеры/': get_keyboard(['Ширина', 'Толщина']),
    '/Фасады/Фасад/Главный фасад/Отмостка/Да/Материал/': get_keyboard(['Бетон', 'Асфальтобетон', 'Брусчатка', 'Плитка', 'Другое']),
    '/Фасады/Фасад/Главный фасад/Отмостка/Да/Водоприемный лоток/': get_keyboard(['Нет', 'Да']),
    '/Фасады/Фасад/Главный фасад/Отмостка/Да/Водоприемный лоток/Да/': get_keyboard(['Размеры', 'Материал', 'Фото']),
    '/Фасады/Фасад/Главный фасад/Отмостка/Да/Водоприемный лоток/Да/Размеры/': get_keyboard(['Ширина', 'Глубина', 'Длина']),
    '/Фасады/Фасад/Главный фасад/Отмостка/Да/Водоприемный лоток/Да/Материал/': get_keyboard(['Бетон', 'Металл', 'Другое']),
    '/Фасады/Фасад/Главный фасад/Отмостка/Да/Водоприемный лоток/Да/Фото/': get_keyboard(['Общие фото', 'Фото дефектов с описанием']),
    '/Фасады/Фасад/Главный фасад/Пожарная лестница/': get_keyboard(['Нет', 'Да']),
    '/Фасады/Фасад/Главный фасад/Пожарная лестница/Да/': get_keyboard(['Материал',
                                                                       'Состояние лакокрасочного покрытия',
                                                                       'Размеры',
                                                                       'Крепление к стене']),
    '/Фасады/Фасад/Главный фасад/Пожарная лестница/Да/Материал/': get_keyboard(['Металл', 'Другое']),
    '/Фасады/Фасад/Главный фасад/Пожарная лестница/Да/Состояние лакокрасочного покрытия/': get_keyboard(['Отсутствует', 'Ржавчина', 'Отслоение', 'Другое']),
    '/Фасады/Фасад/Главный фасад/Пожарная лестница/Да/Размеры/': get_keyboard(['Длина', 'Ширина', 'Шаг ступеней']),
    '/Фасады/Фасад/Дворовый фасад/': get_keyboard(['Материал отделки стен',
                                                   'Наличие декоративных элементов',
                                                   'Размеры',
                                                   'Фото',
                                                   'Входные группы',
                                                   'Решетка водосборная',
                                                   'Видео камеры',
                                                   'Отмостка',
                                                   'Пожарная лестница']),
    '/Фасады/Фасад/Дворовый фасад/Материал отделки стен/': get_keyboard(['Штукатурка и покраска',
                                                                         'Кирпичная кладка',
                                                                         'Керамическая плитка',
                                                                         'Бетон',
                                                                         'Рустованный',
                                                                         'Кирпич крашеный',
                                                                         'Камень',
                                                                         'Другое']),
    '/Фасады/Фасад/Дворовый фасад/Наличие декоративных элементов/': get_keyboard(['Нет', 'Да']),
    '/Фасады/Фасад/Дворовый фасад/Наличие декоративных элементов/Да/': get_keyboard(['Пилястры',
                                                                                     'Сандрики',
                                                                                     'Карнизы',
                                                                                     'Медальоны',
                                                                                     'Фигуры',
                                                                                     'Капители',
                                                                                     'Лепнина',
                                                                                     'Криволинейные элементы',
                                                                                     'Другое']),
    '/Фасады/Фасад/Дворовый фасад/Размеры/': get_keyboard(['Длина', 'Высота']),
    '/Фасады/Фасад/Дворовый фасад/Фото/': get_keyboard(['Общие фото', 'Фото дефектов с описанием']),
    '/Фасады/Фасад/Дворовый фасад/Входные группы/': get_keyboard(['Нет',
                                                                  'Ступени',
                                                                  'Ограждения',
                                                                  'Двери',
                                                                  'Козырьки',
                                                                  'Освещение']),
    '/Фасады/Фасад/Дворовый фасад/Входные группы/Ступени/': get_keyboard(['Высота ступеней', 'Количество ступеней', 'Материал отделки']),
    '/Фасады/Фасад/Дворовый фасад/Входные группы/Ограждения/': get_keyboard(['Высота', 'Материал', 'Поручни', 'Фото']),
    '/Фасады/Фасад/Дворовый фасад/Входные группы/Ограждения/Поручни/': get_keyboard(['Размер', 'Материал']),
    '/Фасады/Фасад/Дворовый фасад/Входные группы/Ограждения/Размер/': get_keyboard(['Длина', 'Ширина', 'Высота']),
    '/Фасады/Фасад/Дворовый фасад/Входные группы/Двери/': get_keyboard(['Входная дверь', 'Тамбурная дверь']),
    '/Фасады/Фасад/Дворовый фасад/Входные группы/Двери/Входная дверь/': get_keyboard(['Размеры',
                                                                                      'Материал',
                                                                                      'Наличие декоративных элементов',
                                                                                      'Доводчик',
                                                                                      'Фото']),
    '/Фасады/Фасад/Дворовый фасад/Входные группы/Двери/Входная дверь/Размеры/': get_keyboard(['Ширина', 'Высота']),
    '/Фасады/Фасад/Дворовый фасад/Входные группы/Двери/Входная дверь/Материал/': get_keyboard(['Металл', 'Дерево', 'Другое']),
    '/Фасады/Фасад/Дворовый фасад/Входные группы/Двери/Входная дверь/Наличие декоративных элементов/': get_keyboard(['Да', 'Нет']),
    '/Фасады/Фасад/Дворовый фасад/Входные группы/Двери/Входная дверь/Доводчик/': get_keyboard(['Да', 'Нет']),
    '/Фасады/Фасад/Дворовый фасад/Входные группы/Двери/Входная дверь/Фото/': get_keyboard(['Общие фото', 'Фото дефектов с описанием']),
    '/Фасады/Фасад/Дворовый фасад/Входные группы/Двери/Тамбурная дверь/': get_keyboard(['Нет', 'Да']),
    '/Фасады/Фасад/Дворовый фасад/Входные группы/Двери/Тамбурная дверь/Да/': get_keyboard(['Размеры', 'Материал', 'Доводчик', 'Фото']),
    '/Фасады/Фасад/Дворовый фасад/Входные группы/Двери/Тамбурная дверь/Да/Размеры/': get_keyboard(['Ширина', 'Высота']),
    '/Фасады/Фасад/Дворовый фасад/Входные группы/Двери/Тамбурная дверь/Да/Материал/': get_keyboard(['Металл', 'Дерево', 'Другое']),
    '/Фасады/Фасад/Дворовый фасад/Входные группы/Двери/Тамбурная дверь/Да/Доводчик/': get_keyboard(['Да', 'Нет']),
    '/Фасады/Фасад/Дворовый фасад/Входные группы/Двери/Тамбурная дверь/Да/Фото/': get_keyboard(['Общие фото', 'Фото дефектов с описанием']),
    '/Фасады/Фасад/Дворовый фасад/Входные группы/Козырьки/': get_keyboard(['Материал', 'Размер', 'Фото']),
    '/Фасады/Фасад/Дворовый фасад/Входные группы/Козырьки/Материал/': get_keyboard(['Сталь оцинкованная',
                                                                                    'Профлист',
                                                                                    'Поликарбонат',
                                                                                    'Ж/Б',
                                                                                    'Другое',
                                                                                    'Отсутствует']),
    '/Фасады/Фасад/Дворовый фасад/Входные группы/Козырьки/Размер/': get_keyboard(['Длина', 'Ширина']),
    '/Фасады/Фасад/Дворовый фасад/Входные группы/Козырьки/Фото/': get_keyboard(['Общие фото', 'Фото дефектов с описанием']),
    '/Фасады/Фасад/Дворовый фасад/Входные группы/Освещение/': get_keyboard(['Да', 'Нет']),
    '/Фасады/Фасад/Дворовый фасад/Входные группы/Освещение/Да/': get_keyboard(['Тип освещения', 'Фото']),
    '/Фасады/Фасад/Дворовый фасад/Входные группы/Освещение/Да/Тип освещения/': get_keyboard(['Лампа накаливания',
                                                                                             'Диодное',
                                                                                             'Галогеновое',
                                                                                             'Люминесцентное',
                                                                                             'Другое']),
    '/Фасады/Фасад/Дворовый фасад/Входные группы/Освещение/Да/Фото/': get_keyboard(['Общие фото', 'Фото дефектов с описанием']),
    '/Фасады/Фасад/Дворовый фасад/Решетка водосборная/': get_keyboard(['Нет', 'Да']),
    '/Фасады/Фасад/Дворовый фасад/Решетка водосборная/Да/': get_keyboard(['Размеры', 'Материал', 'Фото']),
    '/Фасады/Фасад/Дворовый фасад/Решетка водосборная/Да/Размеры/': get_keyboard(['Длина', 'Ширина', 'Глубина приямка']),
    '/Фасады/Фасад/Дворовый фасад/Решетка водосборная/Да/Материал/': get_keyboard(['Металл', 'Другое']),
    '/Фасады/Фасад/Дворовый фасад/Решетка водосборная/Да/Фото/': get_keyboard(['Общие фото', 'Фото дефектов с описанием']),
    '/Фасады/Фасад/Дворовый фасад/Видео камеры/': get_keyboard(['Нет', 'Да']),
    '/Фасады/Фасад/Дворовый фасад/Отмостка/': get_keyboard(['Нет', 'Да']),
    '/Фасады/Фасад/Дворовый фасад/Отмостка/Да/': get_keyboard(['Размеры', 'Материал', 'Водоприемный лоток', 'Фото']),
    '/Фасады/Фасад/Дворовый фасад/Отмостка/Да/Размеры/': get_keyboard(['Ширина', 'Толщина']),
    '/Фасады/Фасад/Дворовый фасад/Отмостка/Да/Материал/': get_keyboard(['Бетон', 'Асфальтобетон', 'Брусчатка', 'Плитка', 'Другое']),
    '/Фасады/Фасад/Дворовый фасад/Отмостка/Да/Водоприемный лоток/': get_keyboard(['Нет', 'Да']),
    '/Фасады/Фасад/Дворовый фасад/Отмостка/Да/Водоприемный лоток/Да/': get_keyboard(['Размеры', 'Материал', 'Фото']),
    '/Фасады/Фасад/Дворовый фасад/Отмостка/Да/Водоприемный лоток/Да/Размеры/': get_keyboard(['Ширина', 'Глубина', 'Длина']),
    '/Фасады/Фасад/Дворовый фасад/Отмостка/Да/Водоприемный лоток/Да/Материал/': get_keyboard(['Бетон', 'Металл', 'Другое']),
    '/Фасады/Фасад/Дворовый фасад/Отмостка/Да/Водоприемный лоток/Да/Фото/': get_keyboard(['Общие фото', 'Фото дефектов с описанием']),
    '/Фасады/Фасад/Дворовый фасад/Пожарная лестница/': get_keyboard(['Нет', 'Да']),
    '/Фасады/Фасад/Дворовый фасад/Пожарная лестница/Да/': get_keyboard(['Материал',
                                                                        'Состояние лакокрасочного покрытия',
                                                                        'Размеры',
                                                                        'Крепление к стене']),
    '/Фасады/Фасад/Дворовый фасад/Пожарная лестница/Да/Материал/': get_keyboard(['Металл', 'Другое']),
    '/Фасады/Фасад/Дворовый фасад/Пожарная лестница/Да/Состояние лакокрасочного покрытия/': get_keyboard(['Отсутствует', 'Ржавчина', 'Отслоение', 'Другое']),
    '/Фасады/Фасад/Дворовый фасад/Пожарная лестница/Да/Размеры/': get_keyboard(['Длина', 'Ширина', 'Шаг ступеней']),
    '/Фасады/Фасад/Торцевые фасады/': get_keyboard(['Материал отделки стен',
                                                    'Наличие декоративных элементов',
                                                    'Размеры',
                                                    'Фото',
                                                    'Входные группы',
                                                    'Решетка водосборная',
                                                    'Видео камеры',
                                                    'Отмостка',
                                                    'Пожарная лестница']),
    '/Фасады/Фасад/Торцевые фасады/Материал отделки стен/': get_keyboard(['Штукатурка и покраска',
                                                                          'Кирпичная кладка',
                                                                          'Керамическая плитка',
                                                                          'Бетон',
                                                                          'Рустованный',
                                                                          'Кирпич крашеный',
                                                                          'Камень',
                                                                          'Другое']),
    '/Фасады/Фасад/Торцевые фасады/Наличие декоративных элементов/': get_keyboard(['Нет', 'Да']),
    '/Фасады/Фасад/Торцевые фасады/Наличие декоративных элементов/Да/': get_keyboard(['Пилястры',
                                                                                      'Сандрики',
                                                                                      'Карнизы',
                                                                                      'Медальоны',
                                                                                      'Фигуры',
                                                                                      'Капители',
                                                                                      'Лепнина',
                                                                                      'Криволинейные элементы',
                                                                                      'Другое']),
    '/Фасады/Фасад/Торцевые фасады/Размеры/': get_keyboard(['Длина', 'Высота']),
    '/Фасады/Фасад/Торцевые фасады/Фото/': get_keyboard(['Общие фото', 'Фото дефектов с описанием']),
    '/Фасады/Фасад/Торцевые фасады/Входные группы/': get_keyboard(['Нет',
                                                                   'Ступени',
                                                                   'Ограждения',
                                                                   'Двери',
                                                                   'Козырьки',
                                                                   'Освещение']),
    '/Фасады/Фасад/Торцевые фасады/Входные группы/Ступени/': get_keyboard(['Высота ступеней', 'Количество ступеней', 'Материал отделки']),
    '/Фасады/Фасад/Торцевые фасады/Входные группы/Ограждения/': get_keyboard(['Высота', 'Материал', 'Поручни', 'Фото']),
    '/Фасады/Фасад/Торцевые фасады/Входные группы/Ограждения/Поручни/': get_keyboard(['Размер', 'Материал']),
    '/Фасады/Фасад/Торцевые фасады/Входные группы/Ограждения/Размер/': get_keyboard(['Длина', 'Ширина', 'Высота']),
    '/Фасады/Фасад/Торцевые фасады/Входные группы/Двери/': get_keyboard(['Входная дверь', 'Тамбурная дверь']),
    '/Фасады/Фасад/Торцевые фасады/Входные группы/Двери/Входная дверь/': get_keyboard(['Размеры',
                                                                                       'Материал',
                                                                                       'Наличие декоративных элементов',
                                                                                       'Доводчик',
                                                                                       'Фото']),
    '/Фасады/Фасад/Торцевые фасады/Входные группы/Двери/Входная дверь/Размеры/': get_keyboard(['Ширина', 'Высота']),
    '/Фасады/Фасад/Торцевые фасады/Входные группы/Двери/Входная дверь/Материал/': get_keyboard(['Металл', 'Дерево', 'Другое']),
    '/Фасады/Фасад/Торцевые фасады/Входные группы/Двери/Входная дверь/Наличие декоративных элементов/': get_keyboard(['Да', 'Нет']),
    '/Фасады/Фасад/Торцевые фасады/Входные группы/Двери/Входная дверь/Доводчик/': get_keyboard(['Да', 'Нет']),
    '/Фасады/Фасад/Торцевые фасады/Входные группы/Двери/Входная дверь/Фото/': get_keyboard(['Общие фото', 'Фото дефектов с описанием']),
    '/Фасады/Фасад/Торцевые фасады/Входные группы/Двери/Тамбурная дверь/': get_keyboard(['Нет', 'Да']),
    '/Фасады/Фасад/Торцевые фасады/Входные группы/Двери/Тамбурная дверь/Да/': get_keyboard(['Размеры', 'Материал', 'Доводчик', 'Фото']),
    '/Фасады/Фасад/Торцевые фасады/Входные группы/Двери/Тамбурная дверь/Да/Размеры/': get_keyboard(['Ширина', 'Высота']),
    '/Фасады/Фасад/Торцевые фасады/Входные группы/Двери/Тамбурная дверь/Да/Материал/': get_keyboard(['Металл', 'Дерево', 'Другое']),
    '/Фасады/Фасад/Торцевые фасады/Входные группы/Двери/Тамбурная дверь/Да/Доводчик/': get_keyboard(['Да', 'Нет']),
    '/Фасады/Фасад/Торцевые фасады/Входные группы/Двери/Тамбурная дверь/Да/Фото/': get_keyboard(['Общие фото', 'Фото дефектов с описанием']),
    '/Фасады/Фасад/Торцевые фасады/Входные группы/Козырьки/': get_keyboard(['Материал', 'Размер', 'Фото']),
    '/Фасады/Фасад/Торцевые фасады/Входные группы/Козырьки/Материал/': get_keyboard(['Сталь оцинкованная',
                                                                                     'Профлист',
                                                                                     'Поликарбонат',
                                                                                     'Ж/Б',
                                                                                     'Другое',
                                                                                     'Отсутствует']),
    '/Фасады/Фасад/Торцевые фасады/Входные группы/Козырьки/Размер/': get_keyboard(['Длина', 'Ширина']),
    '/Фасады/Фасад/Торцевые фасады/Входные группы/Козырьки/Фото/': get_keyboard(['Общие фото', 'Фото дефектов с описанием']),
    '/Фасады/Фасад/Торцевые фасады/Входные группы/Освещение/': get_keyboard(['Да', 'Нет']),
    '/Фасады/Фасад/Торцевые фасады/Входные группы/Освещение/Да/': get_keyboard(['Тип освещения', 'Фото']),
    '/Фасады/Фасад/Торцевые фасады/Входные группы/Освещение/Да/Тип освещения/': get_keyboard(['Лампа накаливания',
                                                                                              'Диодное',
                                                                                              'Галогеновое',
                                                                                              'Люминесцентное',
                                                                                              'Другое']),
    '/Фасады/Фасад/Торцевые фасады/Входные группы/Освещение/Да/Фото/': get_keyboard(['Общие фото', 'Фото дефектов с описанием']),
    '/Фасады/Фасад/Торцевые фасады/Решетка водосборная/': get_keyboard(['Нет', 'Да']),
    '/Фасады/Фасад/Торцевые фасады/Решетка водосборная/Да/': get_keyboard(['Размеры', 'Материал', 'Фото']),
    '/Фасады/Фасад/Торцевые фасады/Решетка водосборная/Да/Размеры/': get_keyboard(['Длина', 'Ширина', 'Глубина приямка']),
    '/Фасады/Фасад/Торцевые фасады/Решетка водосборная/Да/Материал/': get_keyboard(['Металл', 'Другое']),
    '/Фасады/Фасад/Торцевые фасады/Решетка водосборная/Да/Фото/': get_keyboard(['Общие фото', 'Фото дефектов с описанием']),
    '/Фасады/Фасад/Торцевые фасады/Видео камеры/': get_keyboard(['Нет', 'Да']),
    '/Фасады/Фасад/Торцевые фасады/Отмостка/': get_keyboard(['Нет', 'Да']),
    '/Фасады/Фасад/Торцевые фасады/Отмостка/Да/': get_keyboard(['Размеры', 'Материал', 'Водоприемный лоток', 'Фото']),
    '/Фасады/Фасад/Торцевые фасады/Отмостка/Да/Размеры/': get_keyboard(['Ширина', 'Толщина']),
    '/Фасады/Фасад/Торцевые фасады/Отмостка/Да/Материал/': get_keyboard(['Бетон', 'Асфальтобетон', 'Брусчатка', 'Плитка', 'Другое']),
    '/Фасады/Фасад/Торцевые фасады/Отмостка/Да/Водоприемный лоток/': get_keyboard(['Нет', 'Да']),
    '/Фасады/Фасад/Торцевые фасады/Отмостка/Да/Водоприемный лоток/Да/': get_keyboard(['Размеры', 'Материал', 'Фото']),
    '/Фасады/Фасад/Торцевые фасады/Отмостка/Да/Водоприемный лоток/Да/Размеры/': get_keyboard(['Ширина', 'Глубина', 'Длина']),
    '/Фасады/Фасад/Торцевые фасады/Отмостка/Да/Водоприемный лоток/Да/Материал/': get_keyboard(['Бетон', 'Металл', 'Другое']),
    '/Фасады/Фасад/Торцевые фасады/Отмостка/Да/Водоприемный лоток/Да/Фото/': get_keyboard(['Общие фото', 'Фото дефектов с описанием']),
    '/Фасады/Фасад/Торцевые фасады/Пожарная лестница/': get_keyboard(['Нет', 'Да']),
    '/Фасады/Фасад/Торцевые фасады/Пожарная лестница/Да/': get_keyboard(['Материал',
                                                                         'Состояние лакокрасочного покрытия',
                                                                         'Размеры',
                                                                         'Крепление к стене']),
    '/Фасады/Фасад/Торцевые фасады/Пожарная лестница/Да/Материал/': get_keyboard(['Металл', 'Другое']),
    '/Фасады/Фасад/Торцевые фасады/Пожарная лестница/Да/Состояние лакокрасочного покрытия/': get_keyboard(['Отсутствует', 'Ржавчина', 'Отслоение', 'Другое']),
    '/Фасады/Фасад/Торцевые фасады/Пожарная лестница/Да/Размеры/': get_keyboard(['Длина', 'Ширина', 'Шаг ступеней']),
    '/Фасады/Фасад/Цоколь/': get_keyboard(['Материал отделки', 'Наличие декоративных элементов', 'Размер', 'Фото']),
    '/Фасады/Фасад/Цоколь/Материал отделки/': get_keyboard(['Штукатурка и покраска',
                                                            'Кирпичная кладка',
                                                            'Керамическая плитка',
                                                            'Бетон',
                                                            'Рустованный',
                                                            'Кирпич крашеный',
                                                            'Камень',
                                                            'Другое']),
    '/Фасады/Фасад/Цоколь/Наличие декоративных элементов/': get_keyboard(['Нет', 'Да']),
    '/Фасады/Фасад/Цоколь/Наличие декоративных элементов/Да/': get_keyboard(['Пилястры',
                                                                             'Сандрики',
                                                                             'Карнизы',
                                                                             'Медальоны',
                                                                             'Фигуры',
                                                                             'Капители',
                                                                             'Лепнина',
                                                                             'Криволинейные элементы',
                                                                             'Другое']),
    '/Фасады/Фасад/Цоколь/Размер/': get_keyboard(['Длина', 'Высота']),
    '/Фасады/Фасад/Цоколь/Фото/': get_keyboard(['Общие фото', 'Фото дефектов с описанием']),
    '/Фасады/Фасад/Приямки/': get_keyboard(['Да']),
    '/Фасады/Фасад/Приямки/Да/': get_keyboard(['Размеры', 'Материал', 'Отделка', 'Гидроизоляция', 'Фото']),
    '/Фасады/Фасад/Приямки/Да/Размеры/': get_keyboard(['Глубина', 'Ширина', 'Высота над уровнем земли']),
    '/Фасады/Фасад/Приямки/Да/Материал/': get_keyboard(['Кирпич', 'Бетон', 'Камень']),
    '/Фасады/Фасад/Приямки/Да/Отделка/': get_keyboard(['Штукатурка и покраска', 'Краска']),
    '/Фасады/Фасад/Приямки/Да/Гидроизоляция/': get_keyboard(['Да', 'Нет']),
    '/Фасады/Фасад/Приямки/Да/Фото/': get_keyboard(['Общие фото', 'Фото дефектов с описанием']),
    '/Фасады/Окна/': get_keyboard(['МОП', 'Квартиры']),
    '/Фасады/Окна/Квартиры/': get_keyboard(['Материал', 'Размеры', 'Отливы', 'Откосы']),
    '/Фасады/Окна/Квартиры/Материал/': get_keyboard(['Пластиковые', 'Деревянные', 'Пластиковые и деревянные']),
    '/Фасады/Окна/Квартиры/Размеры/': get_keyboard(['Ширина', 'Высота']),
    '/Фасады/Окна/Квартиры/Отливы/': get_keyboard(['Размеры', 'Материал', 'Фото']),
    '/Фасады/Окна/Квартиры/Отливы/Размеры/': get_keyboard(['Длина', 'Ширина']),
    '/Фасады/Окна/Квартиры/Отливы/Материал/': get_keyboard(['Металл', 'Пластик', 'Другое']),
    '/Фасады/Окна/Квартиры/Откосы/': get_keyboard(['Размеры', 'Материал']),
    '/Фасады/Окна/Квартиры/Откосы/Размеры/': get_keyboard(['Ширина']),
    '/Фасады/Окна/Квартиры/Откосы/Материал/': get_keyboard(['Штукатурка и покраскаина', 'Металл', 'Пластик', 'Другое']),
    '/Фасады/Окна/МОП/': get_keyboard(['Материал', 'Размеры', 'Отливы', 'Откосы', 'Фото']),
    '/Фасады/Окна/МОП/Материал/': get_keyboard(['Пластиковые', 'Деревянные', 'Пластиковые и деревянные', ]),
    '/Фасады/Окна/МОП/Размеры/': get_keyboard(['Ширина', 'Высота', ]),
    '/Фасады/Окна/МОП/Отливы/': get_keyboard(['Размеры', 'Материал', 'Сделать Фото']),
    '/Фасады/Окна/МОП/Отливы/Размеры/': get_keyboard(['Длина', 'Ширина']),
    '/Фасады/Окна/МОП/Отливы/Материал/': get_keyboard(['Металл', 'Пластик', 'Другое']),
    '/Фасады/Окна/МОП/Откосы/': get_keyboard(['Размеры', 'Материал']),
    '/Фасады/Окна/МОП/Откосы/Размеры/': get_keyboard(['Ширина']),
    '/Фасады/Окна/МОП/Откосы/Материал/': get_keyboard(['Штукатурка и покраска', 'Металл', 'Пластик', 'Другое']),
    '/Фасады/Окна/МОП/Фото/': get_keyboard(['Общие фото', 'Фото дефектов с описанием']),
    '/Фасады/Водосток/': get_keyboard(['Наружний', 'Внутренний']),
    '/Фасады/Водосток/Наружний/': get_keyboard(['Количество стояков', 'Материал', 'Размеры', 'Греющий кабель', 'Повреждения', 'Фото']),
    '/Фасады/Водосток/Наружний/Материал/': get_keyboard(['Оцинкованная сталь', 'Стальные окрашенные', 'Пластиковые', 'Другое']),
    '/Фасады/Водосток/Наружний/Размеры/': get_keyboard(['Длина', 'Диаметр']),
    '/Фасады/Водосток/Наружний/Греющий кабель/': get_keyboard(['Нет', 'Да']),
    '/Фасады/Водосток/Наружний/Греющий кабель/Да/': get_keyboard(['Сечение', 'Марка']),
    '/Фасады/Водосток/Наружний/Повреждения/': get_keyboard(['Коррозия', 'Замятости', 'Протечки', 'Повреждение крепежных элементов', 'Наличие отмётов']),
    '/Фасады/Водосток/Наружний/Повреждения/Наличие отмётов/': get_keyboard(['Да', 'Нет']),
    '/Фасады/Водосток/Наружний/Фото/': get_keyboard(['Общие фото', 'Фото дефектов с описанием']),
    '/Фасады/Водосток/Наружний/Фото/': get_keyboard(['Общие фото', 'Фото дефектов с описанием']),
    '/Фасады/Дворовые ворота/': get_keyboard(['Нет', 'Да', 'Керамзит']),
    '/Фасады/Дворовые ворота/Да/': get_keyboard(['Размеры', 'Материал', 'Фото']),
    '/Фасады/Дворовые ворота/Да/Размеры/': get_keyboard(['Ширина', 'Высота']),
    '/Фасады/Дворовые ворота/Да/Материал/': get_keyboard(['Металл']),
    '/Фасады/Дворовые ворота/Да/Фото/': get_keyboard(['Общие фото', 'Фото дефектов с описанием']),
}}

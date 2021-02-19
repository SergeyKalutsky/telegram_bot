from .roof import get_keyboard, keyboard, answer


keyboard = {**keyboard, **{
    '/МОПы/': get_keyboard(['Стены',
                            'Потолки',
                            'Полы',
                            'Окна',
                            'Двери',
                            'Лестничные ограждения',
                            'Ступени',
                            'Освещение',
                            'Отопление',
                            'Водоснабжение',
                            'Пожарный водопровод',
                            'Мусоропровод']),
    '/МОПы/Стены/': get_keyboard(['Общая площадь', 'Отделка', 'Декоративные элементы', 'Плинтус', 'Фото']),
    '/МОПы/Стены/Отделка/': get_keyboard(['Штукатурка и покраска', 'Кирпич', 'Другое']),
    '/МОПы/Стены/Декоративные элементы/': get_keyboard(['Нет', 'Да']),
    '/МОПы/Стены/Плинтус/': get_keyboard(['Верхний', 'Нижний']),
    '/МОПы/Стены/Плинтус/Верхний/': get_keyboard(['Нет', 'Да']),
    '/МОПы/Стены/Плинтус/Нижний/': get_keyboard(['Нет', 'Да']),
    '/МОПы/Стены/Плинтус/Нижний/Да/': get_keyboard(['Требует ли замены?']),
    '/МОПы/Стены/Плинтус/Нижний/Да/Требует ли замены?/': get_keyboard(['Нет', 'Да']),
    '/МОПы/Стены/Фото/': get_keyboard(['Общие фото', 'Фото дефектов с описанием', 'Фото зарисовки фактических размеров на плане БТИ']),
    '/МОПы/Потолки/': get_keyboard(['Общая площадь', 'Отделка', 'Декоративные элементы', 'Плита перекрытия', 'Фото']),
    '/МОПы/Потолки/Отделка/': get_keyboard(['Штукатурка и покраска', 'Побелка', 'Другое']),
    '/МОПы/Потолки/Декоративные элементы/': get_keyboard(['Нет', 'Да']),
    '/МОПы/Потолки/Декоративные элементы/': get_keyboard(['Нет', 'Да']),
    '/МОПы/Потолки/Плита перекрытия/': get_keyboard(['Бетон', 'Дерево', 'Другое']),
    '/МОПы/Потолки/Фото/': get_keyboard(['Общие фото', 'Фото дефектов с описанием']),
    '/МОПы/Полы/': get_keyboard(['Общая площадь', 'Отделка', 'Фото']),
    '/МОПы/Полы/Отделка/': get_keyboard(['Плитка', 'Бетон', 'Мозаичный бетон', 'Другое']),
    '/МОПы/Полы/Плитка/': get_keyboard(['Размер плитки']),
    '/МОПы/Полы/Фото/': get_keyboard(['Общие фото', 'Фото дефектов с описанием']),
    '/МОПы/Окна/': get_keyboard(['Размеры', 'Материал', 'Подоконники', 'Количество стеклопакетов', 'Фото', 'Решетки']),
    '/МОПы/Окна/Материал/': get_keyboard(['Дерево', 'ПВХ', 'Другое']),
    '/МОПы/Окна/Подоконники/': get_keyboard(['Размеры', 'Материал']),
    '/МОПы/Окна/Подоконники/Размеры/': get_keyboard(['Ширина', 'Длина']),
    '/МОПы/Окна/Подоконники/Материал/': get_keyboard(['Дерево', 'Камень', 'ПВХ', 'Другое']),
    '/МОПы/Окна/Фото/': get_keyboard(['Общие фото', 'Фото дефектов с описанием', 'Фото зарисовок окон с размерами']),
    '/МОПы/Окна/Решетки/': get_keyboard(['Да', 'Нет']),
    '/МОПы/Двери/': get_keyboard(['Количество', 'Материал', 'Размеры', 'Фото']),
    '/МОПы/Двери/Материал/': get_keyboard(['Металл', 'Дерево', 'ПВХ', 'Другое']),
    '/МОПы/Двери/Размеры/': get_keyboard(['Высота', 'Ширина']),
    '/МОПы/Двери/Фото/': get_keyboard(['Общие фото', 'Фото дефектов с описанием']),
    '/МОПы/Двери/Фото/': get_keyboard(['Общие фото', 'Фото дефектов с описанием']),
    '/МОПы/Лестничные ограждения/': get_keyboard(['Поручни', 'Балясины', 'Фото']),
    '/МОПы/Лестничные ограждения/Поручни/': get_keyboard(['Материал', 'Размеры', 'Отделка', 'Способ крепления']),
    '/МОПы/Лестничные ограждения/Поручни/Материал/': get_keyboard(['Дерево', 'Металл', 'Пластик', 'Другое']),
    '/МОПы/Лестничные ограждения/Поручни/Размеры/': get_keyboard(['Длина', 'Ширина', 'Высота']),
    '/МОПы/Лестничные ограждения/Поручни/Отделка/': get_keyboard(['Нет', 'Покраска', 'Лак', 'Другое']),
    '/МОПы/Лестничные ограждения/Балясины/': get_keyboard(['Материал', 'Шаг', 'Лак', 'O co']),
    '/МОПы/Лестничные ограждения/Балясины/Материал/': get_keyboard(['Металл', 'Дерево', 'Камень', 'Другое']),
    '/МОПы/Лестничные ограждения/Балясины/Размеры/': get_keyboard(['Высота', 'Ширина', 'Толщина']),
    '/МОПы/Лестничные ограждения/Фото/': get_keyboard(['Общие фото', 'Фото дефектов с описанием', 'Фото зарисовки элемента ограждения']),
    '/МОПы/Ступени/': get_keyboard(['Тип', 'Размеры', 'Косоуры', 'Фото']),
    '/МОПы/Ступени/Тип/': get_keyboard(['Монолитные', 'Наборные', 'Деревянные', 'Другое']),
    '/МОПы/Ступени/Размеры/': get_keyboard(['Высота', 'Ширина']),
    '/МОПы/Ступени/Косоуры/': get_keyboard(['Металлические', 'Бетонные', 'Другое', 'Отделка']),
    '/МОПы/Ступени/Косоуры/Отделка/': get_keyboard(['Штукатурка по сетке', 'Штукатурка по бетону', 'Окраска по бетону', 'Другое']),
    '/МОПы/Ступени/Фото/': get_keyboard(['Общие фото', 'Фото дефектов с описанием', 'Фото зарисовки дефектов на плане']),
    '/МОПы/Освещение/': get_keyboard(['Способ прокладки кабеля', 'Тип кабеля', 'Светильники', 'Выключатели', 'Эл щиты', 'Фото']),
    '/МОПы/Освещение/Способ прокладки кабеля/': get_keyboard(['Открытый', 'В лотках', 'В трубе', 'В коробах', 'Другое']),
    '/МОПы/Освещение/Тип кабеля/': get_keyboard(['Алюминий', 'Медь']),
    '/МОПы/Освещение/Тип кабеля/Алюминий/': get_keyboard(['Сечение']),
    '/МОПы/Освещение/Тип кабеля/Медь/': get_keyboard(['Сечение']),
    '/МОПы/Освещение/Светильники/': get_keyboard(['Нет', 'Да']),
    '/МОПы/Освещение/Светильники/Да/': get_keyboard(['Тип освещения', 'Фото']),
    '/МОПы/Освещение/Светильники/Да/Тип освещения/': get_keyboard(['Лампа накаливания', 'Диодное', 'Галогеновое', 'Люминесцентное', 'Другое']),
    '/МОПы/Освещение/Светильники/Да/Фото/': get_keyboard(['Общие фото', 'Фото дефектов с описанием', 'Фото зарисовки на плане']),
    '/МОПы/Освещение/Выключатели/': get_keyboard(['Нет', 'Да']),
    '/МОПы/Освещение/Выключатели/Да/': get_keyboard(['Фото зарисовки на плане', 'Общие фото']),
    '/МОПы/Освещение/Эл щиты/': get_keyboard(['Нет', 'Да']),
    '/МОПы/Освещение/Эл щиты/Да/': get_keyboard(['Вводной автомат', 'Фото']),
    '/МОПы/Освещение/Эл щиты/Да/Вводной автомат/': get_keyboard(['Номинал', 'Производитель', 'Подводящий кабель']),
    '/МОПы/Освещение/Эл щиты/Да/Фото/': get_keyboard(['Фото зарисовки на плане', 'Общие фото']),
    '/МОПы/Освещение/Фото/': get_keyboard(['Общие фото']),
    '/МОПы/Отопление/': get_keyboard(['Наличие магистралей', 'Наличие стояков', 'Отопительные приборы', 'Фото']),
    '/МОПы/Отопление/': get_keyboard(['Наличие магистралей', 'Наличие стояков', 'Отопительные приборы', 'Фото']),
    '/МОПы/Отопление/Наличие магистралей/': get_keyboard(['Нет', 'Да']),
    '/МОПы/Отопление/Наличие магистралей/Да/': get_keyboard(['Диаметры', 'Материал', 'Утепление', 'Запорная арматура']),
    '/МОПы/Отопление/Наличие магистралей/Да/Материал/': get_keyboard(['Сталь', 'Полипропилен', 'Металлопласт', 'Сшитый полиэтилен', 'Другое']),
    '/МОПы/Отопление/Наличие магистралей/Да/Утепление/': get_keyboard(['Мин вата',
                                                                       'Вспененный полиэтилен',
                                                                       'Обмазочное',
                                                                       'Белая глина по сетке',
                                                                       'Стеклоткань по стекловате',
                                                                       'Без утепления',
                                                                       'Другое']),
    '/МОПы/Отопление/Наличие магистралей/Да/Запорная арматура/': get_keyboard(['Нет', 'Да']),
    '/МОПы/Отопление/Наличие магистралей/Да/Запорная арматура/Да/': get_keyboard(['Диаметр',
                                                                                  'Расширительный бак',
                                                                                  'Воздухоотводные клапаны',
                                                                                  'Регулирующие вентили',
                                                                                  'Воздухоотводные устройства с вантузами',
                                                                                  'Шаровый кран']),
    '/МОПы/Отопление/Наличие магистралей/Да/Запорная арматура/Да/Расширительный бак/': get_keyboard(['Да', 'Нет']),
    '/МОПы/Отопление/Наличие магистралей/Да/Запорная арматура/Да/Воздухоотводные клапаны/': get_keyboard(['Да', 'Нет']),
    '/МОПы/Отопление/Наличие магистралей/Да/Запорная арматура/Да/Регулирующие вентили/': get_keyboard(['Да', 'Нет']),
    '/МОПы/Отопление/Наличие магистралей/Да/Запорная арматура/Да/Воздухоотводные устройства с вантузами/': get_keyboard(['Да', 'Нет']),
    '/МОПы/Отопление/Наличие магистралей/Да/Запорная арматура/Да/Шаровый кран/': get_keyboard(['Да', 'Нет']),
    '/МОПы/Отопление/Наличие стояков/': get_keyboard(['Да', 'Нет']),
    '/МОПы/Отопление/Наличие стояков/Да/': get_keyboard(['Диаметры', 'Материал', 'Утепление', 'Запорная арматура', 'Способ прокладки']),
    '/МОПы/Отопление/Наличие стояков/Да/Материал/': get_keyboard(['Сталь', 'Полипропилен', 'Металлопласт', 'Сшитый полиэтилен', 'Другое']),
    '/МОПы/Отопление/Наличие стояков/Да/Утепление/': get_keyboard(['Мин вата',
                                                                   'Вспененный полиэтилен',
                                                                   'Обмазочное',
                                                                   'Белая глина по сетке',
                                                                   'Стеклоткань по стекловате',
                                                                   'Другое']),
    '/МОПы/Отопление/Наличие стояков/Да/Запорная арматура/': get_keyboard(['Нет', 'Да']),
    '/МОПы/Отопление/Наличие стояков/Да/Запорная арматура/Да/': get_keyboard(['Диаметр',
                                                                              'Воздухоотводные клапаны',
                                                                              'Регулирующие вентили',
                                                                              'Шаровый кран']),
    '/МОПы/Отопление/Наличие стояков/Да/Запорная арматура/Да/Воздухоотводные клапаны/': get_keyboard(['Да', 'Нет']),
    '/МОПы/Отопление/Наличие стояков/Да/Запорная арматура/Да/Регулирующие вентили/': get_keyboard(['Да', 'Нет']),
    '/МОПы/Отопление/Наличие стояков/Да/Запорная арматура/Да/Шаровый кран/': get_keyboard(['Да', 'Нет']),
    '/МОПы/Отопление/Наличие стояков/Да/Способ прокладки/': get_keyboard(['Открытый', 'Зашиты в стене']),
    '/МОПы/Отопление/Наличие стояков/Да/Способ прокладки/Зашиты в стене/': get_keyboard(['Указать объем восстанов. ремонта']),
    '/МОПы/Отопление/Отопительные приборы/': get_keyboard(['Нет', 'Да']),
    '/МОПы/Отопление/Отопительные приборы/Да/': get_keyboard(['Материал', 'Количество секций']),
    '/МОПы/Отопление/Отопительные приборы/Да/Материал/': get_keyboard(['Чугун', 'Биметаллические', 'Другое']),
    '/МОПы/Отопление/Фото/': get_keyboard(['Общие фото', 'Фото дефектов с описанием', 'Фото зарисовки аксонометрической схемы']),
    '/МОПы/Водоснабжение/': get_keyboard(['Наличие магистралей', 'Наличие стояков', 'Фото']),
    '/МОПы/Водоснабжение/Наличие магистралей/': get_keyboard(['Нет', 'Да']),
    '/МОПы/Водоснабжение/Наличие магистралей/Да/': get_keyboard(['Диаметры', 'Материал', 'Утепление', 'Запорная арматура']),
    '/МОПы/Водоснабжение/Наличие магистралей/Да/Материал/': get_keyboard(['Сталь', 'Полипропилен', 'Металлопласт', 'Сшитый полиэтилен', 'Другое']),
    '/МОПы/Водоснабжение/Наличие магистралей/Да/Утепление/': get_keyboard(['Мин вата',
                                                                           'Вспененный полиэтилен',
                                                                           'Обмазочное',
                                                                           'Белая глина по сетке',
                                                                           'Стеклоткань по стекловате',
                                                                           'Без утепления',
                                                                           'Другое']),
    '/МОПы/Водоснабжение/Наличие магистралей/Да/Запорная арматура/': get_keyboard(['Нет', 'Да']),
    '/МОПы/Водоснабжение/Наличие магистралей/Да/Запорная арматура/Да/': get_keyboard(['Диаметр',
                                                                                      'Расширительный бак',
                                                                                      'Воздухоотводные клапаны',
                                                                                      'Регулирующие вентили',
                                                                                      'Воздухоотводные устройства с вантузами',
                                                                                      'Шаровый кран']),
    '/МОПы/Водоснабжение/Наличие магистралей/Да/Запорная арматура/Да/Расширительный бак/': get_keyboard(['Да', 'Нет']),
    '/МОПы/Водоснабжение/Наличие магистралей/Да/Запорная арматура/Да/Воздухоотводные клапаны/': get_keyboard(['Да', 'Нет']),
    '/МОПы/Водоснабжение/Наличие магистралей/Да/Запорная арматура/Да/Регулирующие вентили/': get_keyboard(['Да', 'Нет']),
    '/МОПы/Водоснабжение/Наличие магистралей/Да/Запорная арматура/Да/Воздухоотводные устройства с вантузами/': get_keyboard(['Да', 'Нет']),
    '/МОПы/Водоснабжение/Наличие магистралей/Да/Запорная арматура/Да/Шаровый кран/': get_keyboard(['Да', 'Нет']),
    '/МОПы/Водоснабжение/Наличие стояков/': get_keyboard(['Да', 'Нет']),
    '/МОПы/Водоснабжение/Наличие стояков/Да/': get_keyboard(['Диаметры', 'Материал', 'Утепление', 'Запорная арматура', 'Способ прокладки']),
    '/МОПы/Водоснабжение/Наличие стояков/Да/Материал/': get_keyboard(['Сталь', 'Полипропилен', 'Металлопласт', 'Сшитый полиэтилен', 'Другое']),
    '/МОПы/Водоснабжение/Наличие стояков/Да/Утепление/': get_keyboard(['Мин вата',
                                                                       'Вспененный полиэтилен',
                                                                       'Обмазочное',
                                                                       'Белая глина по сетке',
                                                                       'Стеклоткань по стекловате',
                                                                       'Другое']),
    '/МОПы/Водоснабжение/Наличие стояков/Да/Запорная арматура/': get_keyboard(['Нет', 'Да']),
    '/МОПы/Водоснабжение/Наличие стояков/Да/Запорная арматура/Да/': get_keyboard(['Диаметр',
                                                                                  'Воздухоотводные клапаны',
                                                                                  'Регулирующие вентили',
                                                                                  'Шаровый кран']),
    '/МОПы/Водоснабжение/Наличие стояков/Да/Запорная арматура/Да/Воздухоотводные клапаны/': get_keyboard(['Да', 'Нет']),
    '/МОПы/Водоснабжение/Наличие стояков/Да/Запорная арматура/Да/Регулирующие вентили/': get_keyboard(['Да', 'Нет']),
    '/МОПы/Водоснабжение/Наличие стояков/Да/Запорная арматура/Да/Шаровый кран/': get_keyboard(['Да', 'Нет']),
    '/МОПы/Водоснабжение/Наличие стояков/Да/Способ прокладки/': get_keyboard(['Открытый', 'Зашиты в стене']),
    '/МОПы/Водоснабжение/Наличие стояков/Да/Способ прокладки/Зашиты в стене/': get_keyboard(['Указать объем восстанов. ремонта']),
    '/МОПы/Водоснабжение/Фото/': get_keyboard(['Общие фото', 'Фото дефектов с описанием', 'Фото зарисовки аксонометрической схемы']),
    '/МОПы/Пожарный водопровод/': get_keyboard(['Да', 'Нет']),
    '/МОПы/Пожарный водопровод/Да/': get_keyboard(['Диаметр магистралей',
                                                   'Способ прокладки',
                                                   'Шкафы',
                                                   'Фото',
                                                   'Шланги',
                                                   'Манометр',
                                                   'Диаметр вентилей']),
    '/МОПы/Пожарный водопровод/Да/Способ прокладки/': get_keyboard(['Открытый', 'Закрытый']),
    '/МОПы/Пожарный водопровод/Да/Способ прокладки/Закрытый/': get_keyboard(['Открытый', 'Указать объем восстанов. ремонта']),
    '/МОПы/Пожарный водопровод/Да/Шкафы/': get_keyboard(['Размер', 'Способ крепления']),
    '/МОПы/Пожарный водопровод/Да/Шкафы/Размер/': get_keyboard(['Ширина', 'Высота', 'Глубина']),
    '/МОПы/Пожарный водопровод/Да/Шкафы/Способ крепления/': get_keyboard(['Встроенный', 'Навесной']),
    '/МОПы/Пожарный водопровод/Да/Фото/': get_keyboard(['Общие фото', 'Фото дефектов с описанием', 'Фото зарисовки на плане']),
    '/МОПы/Пожарный водопровод/Да/Шланги/': get_keyboard(['Нет', 'Да']),
    '/МОПы/Пожарный водопровод/Да/Шланги/Да/': get_keyboard(['Состояние']),
    '/МОПы/Пожарный водопровод/Да/Манометр/': get_keyboard(['Нет', 'Да']),
    '/МОПы/Мусоропровод/': get_keyboard(['Нет', 'Да']),
    '/МОПы/Мусоропровод/Да/': get_keyboard(['Диаметр ствола',
                                            'Количество клапанов',
                                            'Наличие устройства прочистки',
                                            'Наличие ГВС для промывки',
                                            'Наличие мусорокамер',
                                            'Фото']),
    '/МОПы/Мусоропровод/Да/Наличие устройства прочистки/': get_keyboard(['Нет', 'Да']),
    '/МОПы/Мусоропровод/Да/Наличие ГВС для промывки/': get_keyboard(['Нет', 'Да']),
    '/МОПы/Мусоропровод/Да/Наличие мусорокамер/': get_keyboard(['Нет', 'Да']),
    '/МОПы/Мусоропровод/Да/Наличие мусорокамер/Да/': get_keyboard(['Размеры', 'Отделка', 'Светильники']),
    '/МОПы/Мусоропровод/Да/Наличие мусорокамер/Да/Размеры/': get_keyboard(['Высота', 'Ширина', 'Длина']),
    '/МОПы/Мусоропровод/Да/Наличие мусорокамер/Да/Отделка/': get_keyboard(['Плитка', 'Штукарка и покраска', 'Другое']),
    '/МОПы/Мусоропровод/Да/Наличие мусорокамер/Да/Светильники/': get_keyboard(['Нет', 'Да']),
    '/МОПы/Мусоропровод/Да/Наличие мусорокамер/Да/Светильники/Да/': get_keyboard(['Тип освещения', 'Фото']),
    '/МОПы/Мусоропровод/Да/Наличие мусорокамер/Да/Светильники/Да/Тип освещения/': get_keyboard(['Лампа накаливания',
                                                                                                'Диодное',
                                                                                                'Галогеновое',
                                                                                                'Люминесцентное',
                                                                                                'Другое']),
    '/МОПы/Мусоропровод/Да/Наличие мусорокамер/Да/Светильники/Да/Фото/': get_keyboard(['Общие фото', 'Фото дефектов с описанием', 'Фото зарисовки на плане']),
    '/МОПы/Мусоропровод/Да/Фото/': get_keyboard(['Общие фото', 'Фото дефектов с описанием', 'Фото зарисовки на плане']),


}}
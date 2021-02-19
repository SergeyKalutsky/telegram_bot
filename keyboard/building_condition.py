from .landscaping import keyboard, answer, get_keyboard

keyboard = {**keyboard, **{
    '/Состояние здания/': get_keyboard(['Выветривание кладки', 'Состояние перемычек', 'Деформации']),
    '/Состояние здания/Выветривание кладки/': get_keyboard(['Наблюдается', 'Не наблюдается']),
    '/Состояние здания/Выветривание кладки/Наблюдается/': get_keyboard(['Со стороны главного фасада',
                                                                        'Со стороны торцевых фасадов',
                                                                        'Со стороны дворового фасада']),
    '/Состояние здания/Состояние перемычек/': get_keyboard(['Работоспособное']),
    '/Состояние здания/Деформации/': get_keyboard(['Не наблюдаются', 'Наблюдаются']),


}}

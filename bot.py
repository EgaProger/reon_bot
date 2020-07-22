# импорт модулей
import vk_api
import os
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

token = os.environ['TOKEN']
group_id = os.environ['GROUP_ID']

vk_session = vk_api.VkApi(token=token) # логимся как сообщество
longpoll = VkBotLongPoll(vk_session, group_id) # получаем доступ к longpolling'у, то есть к бесконечному циклу для отслеживания событий
vk = vk_session.get_api() # получем доступ к методам

welcome_message = '''
Здравствуйте! Мы крошечная компания, которая разрабатывает: игры, ИИ, моды, программы.
Наша команда:
Кирилл Дятлов - основатель, программист, аниматор
Виталий Турчак - спрайтер, локализатор на украинский
Владислав Шабардин - помощник по модам
Степан Кириешкин - верстальщик, программист
Илья Зараменских - верстальщик
Владимир Корнилов - 3D шер
Андрей Захаров, Артём Федоров - дизайнеры
Бэлигто Бейнганов - 3D-шер, скриптер
Тимофей Петров - видеомонтажер
Степан Цыганков - композитор
'''


for event in longpoll.listen():

    if event.type == VkBotEventType.MESSAGE_NEW: # если новое сообщение
        message_text = event.obj['text']
        user_id = event.obj['from_id']
        vk.messages.send(peer_id=user_id, random_id=0, message=welcome_message) # отправляем

import configuration

# Импорт библиотеки requests, который предназначен для отправки HTTP-запросов
import requests

# Импорт файла data, в котором содержатся переменные для заголовков и тело запроса
import data
from data import body

# Определение функции post_new_order для отправки POST-запроса на создание нового заказа
def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body,
                         headers=data.headers)

# Определяем вспомогательную функцию поиска заказа по трек-номеру
def get_order(track):
    return requests.get(configuration.URL_SERVICE +  "/v1/orders/track?t=" + str(track))


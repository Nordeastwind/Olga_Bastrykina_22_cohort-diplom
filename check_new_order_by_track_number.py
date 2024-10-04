import  sender_stand_request

# Функция позитивной проверки
def positive_assert():
    rsp = sender_stand_request.post_new_order()
    assert rsp.status_code == 201
    track = rsp.json()['track']
    rsp2 = sender_stand_request.get_order(track)
    assert rsp2.status_code == 200

# Тест 1. Получение данных о заказе по трек-номеру
def test1_check_new_order_by_track_number():
    positive_assert()
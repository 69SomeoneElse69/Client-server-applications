"""2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий его заполнение данными. Для этого:
Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity), цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде словаря в файл orders.json. При записи данных указать величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра."""

import json

def write_order_to_json(item: str, quantiti: str, pice: str, buyer: str, date: str) -> None:
    with open('orders.json', 'r', encoding="utf-8") as f_out:
        data = json.load(f_out)

    with open("orders.json", 'w', encoding="utf-8") as f_in:
        orders_list = data['orders']
        orders_info = {'item': item,
                       'quantiti': quantiti,
                       'pice': pice,
                       'buyer': buyer,
                       'date': date
                       }
        orders_list.append(orders_info)
        json.dump(data, f_in, indent=4, ensure_ascii=False)

write_order_to_json('pen', '100', '20', 'Максим E.C.', '05.09.2011')
write_order_to_json('стол', '5', '1700', 'Ivanov I.P.', '12.12.2020')

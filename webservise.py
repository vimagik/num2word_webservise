from flask import Flask, request, jsonify
from num2words import num2words


app = Flask(__name__)


@app.route('/num2text/', methods=['POST'])
def num_text():
    json_data = request.get_json()
    # Проверяем наличие необходимого ключа в запросе
    if 'number' not in json_data:
        return jsonify(str='The key number doesn`t exist')
    # Достаем пришедшие данные из запроса
    number = json_data['number']
    # Начало блока по обработке пришедших данных. Здесь пишем свой код
    text = num2words(number, lang='ru')
    # Конеч блока обработки данных

    return jsonify(str=text)


if __name__ == '__main__':
    app.run(debug=True)

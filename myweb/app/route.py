from flask import render_template
from flask import request
from urllib.parse import unquote


def index():
    return render_template('index.html')


def other():
    game_list = ['BB視訊', 'AG視訊', 'BB捕魚達人']
    return render_template('other.html', game_list=game_list)


def get_wagerdiv():

    game = request.args.get('game')  # 獲取選擇的遊戲
    decoded_game = unquote(game)
    if (decoded_game == 'BB視訊'):

        params = ['日期', '局號', '注單編號']

    html = ''
    # 根據選擇的遊戲生成對應的 HTML
    for item in params:
        html += '<div class="form-group form-row" id="wagerdiv">'
        html += '<label for="length" class="col-md-4 col-form-label">' + item + '</label>'
        html += '<div class="col-md-8">'
        html += '<input type="text" name="' + item + \
            '" class="form-control" id="length" min="4" max="16" value="' + item + '">'
        html += '</div></div>'

    return html


def test_start():

    form_data = request.form

    for key, value in form_data:

        print(f'key:{key},value:{value}')

    return "Success"

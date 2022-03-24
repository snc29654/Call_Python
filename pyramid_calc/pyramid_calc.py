# -*- coding: utf-8 -*-
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import signal
import sqlite3
from contextlib import closing
dbname = 'database.db'

import webbrowser
webbrowser.open('C:/github/Call_Python/pyramid_calc/pyramid_calc.html')

def diary_world(request):
    print(request.params)
    in_data=request.params
    num1=in_data["num1"]
    num2=in_data["num2"]
    kind =in_data["kind"]
    if kind == "*":
        result = int(num1) * int(num2);
    if kind == "+":
        result = int(num1) + int(num2);
    if kind == "-":
        result = int(num1) - int(num2);
    if kind == "/":
        result = int(num1) / int(num2);
    return Response("演算結果は  " + str(result)  + "です")
    #実行処理  python サーバーを立てています
if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    with Configurator() as config:
        config.add_route('diary', '/')
        config.add_view(diary_world, route_name='diary',renderer="jsonp")
        app = config.make_wsgi_app()
    server = make_server("localhost", 6543, app)
    server.serve_forever()

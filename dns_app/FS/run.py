import json
from flask import Flask, request, Response
import requests
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'


@app.route('/register')
def user_register():
    json_object = {}
    host_name = request.args.get('hostname')
    ip_address = request.args.get('ip')
    as_ip: request.args.get('as_ip'),
    as_port: request.args.get('as_port')
    json_object['name'] = host_name
    json_object['address'] = ip_address
    json_object['as_ip'] = as_ip
    json_object['as_port'] = as_port
    req = requests.post('http://0.0.0.0:53533', data=json_object)
    return req.text


@app.route('/fibonacci')
def fibonacci():
    number = int(request.args.get('number'))
    if number == None:
        return Response("Bad request", status=400)
    elif not number.isnumeric():
        return Response("Bad request", status=400)
    else:
        result = str(calculate_fibonacci(number))
        return Response("The fibonacci value of the number " + str(number) + " is: " + result + ".", status=200)


def calculate_fibonacci(number):
    if number <= 1:
        if number == 1:
            return number
        else:
            return 0
    else:
        return calculate_fibonacci(number - 1) + calculate_fibonacci(number - 2)


app.run(host='0.0.0.0',
        port=9090,
        debug=True)

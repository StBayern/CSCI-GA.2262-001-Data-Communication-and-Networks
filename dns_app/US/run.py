from flask import Flask, url_for, request, render_template, Response
import requests
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'


@app.route('/fibonacci')
def US():
    host_name = request.args.get('hostname')
    fs_port = request.args.get('fs_port')
    number = request.args.get('number')
    as_ip = request.args.get('as_ip')
    as_port = request.args.get('as_port')

    if host_name == None:
        return Response("Bad request", status=400)
    if fs_port == None:
        return Response("Bad request", status=400)
    if number == None:
        return Response("Bad request", status=400)
    if as_ip == None:
        return Response("Bad request", status=400)
    if as_port == None:
        return Response("Bad request", status=400)

    name_port_pair = {'name': host_name, 'fs_port': fs_port}
    request_url = 'http://' + as_ip + ':' + as_port
    req = requests.get(request_url, params=name_port_pair)
    if req.status_code == 404:
        error = host_name + " not found, Status:404"
        return error
    else:
        FS = 'http://' + req.text + ':' + fs_port + '/fabonacci?number=' + number
        req = requests.get(FS)
        result = req.text
        return result


app.run(host='0.0.0.0',
        port=8080,
        debug=True)

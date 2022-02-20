import json
from flask import Flask, request, Response
import os
import requests
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def AS():
    send_method = ''
    if request.method != None:
        send_method = request.method
    # create the DNS database
    if os.path.exists('database.json'):
        db_file = 'database.json'
    else:
        os.system(r'touch database.json')
    db_file = 'database.json'

    # handle the registration
    if send_method == 'POST':
        new_register = {}
        received = request.form
        new_register[received['name']] = received['address']
        with open(db_file, 'w') as f:
            json.dump(new_register, f)
        return Response("Registration Finished!", status=200)

    # handle the dns query
    if send_method == 'GET':
        target_name = ''
        if request.args.get('name') != None:
            target_name = request.args.get('name')
        with open(db_file, 'r') as f:
            pairs = json.load(f)
            if pairs != None:
                if target_name in pairs:
                    return Response(pairs.get(target_name), status=200)
                else:
                    return Response("Not Found", status=404)
            else:
                return Response("Not Found", status=404)


app.run(host='0.0.0.0',
        port=53533,
        debug=True)

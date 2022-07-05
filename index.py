import os
import requests
from flask import Flask, request

app = Flask(__name__)

@app.route('/api/auth')
def apiAuth():
    code = request.args.get('code')
    if code is None:
        return 'missing parameter code', 400
    else:
        response = requests.post('https://github.com/login/oauth/access_token', json={
            'client_id': os.environ.get('REDSTONELAUNCHER_CLIENTID'),
            'client_secret': os.environ.get('REDSTONELAUNCHER_CLIENT_SECRET'),
            'code': code
        }, headers={
            'Accept': 'application/json'
        })
        return response.text, 200

from flask import Flask, jsonify, request, Response
import apiservice

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def main_route():
    return 'hello'

@app.route('/api/sub', methods=['GET'])
def sub():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        result = apiservice.sub(a, b)
        response = Response(str(result), 200)
        return response
    except:
        return Response('Bad request', 400)

@app.route('/api/mul', methods=['GET'])
def mul():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        result =  apiservice.mul(a, b)
        response = Response(str(result), 200)
        return response
    except:
        return Response('Bad request', 400)

@app.route('/api/div', methods=['GET'])
def div():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        result =  apiservice.div(a, b)
        response = Response(str(result), 200)
        return response
    except:
        return Response('Bad request', 400)
    
app.run('0.0.0.0', port=80)
from flask import Flask , request 
import socket
import requests
from flask_cors import CORS

def obtener_direccion_ip():
    hostname = socket.gethostname()
    direccion_ip = socket.gethostbyname(hostname)
    return direccion_ip
"""
def ping ():
    Nododata = {'Ip': obtener_direccion_ip(), 'Nombre':"REBAJE 720" }
    resp = requests.post('http://192.168.100.31:7000/Control/1', data=Nododata)
    print(resp)
"""
direccion_ip = obtener_direccion_ip()


app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})

@app.route("/") 
def home():
    return "high"

@app.route("/Input/A") 
def InputA():
    return "I 1"

@app.route("/Input/B") 
def InputB():
    return "I 2"

if __name__== "__main__":
    #ping() 
    app.run(host='192.168.100.56', port=7000)
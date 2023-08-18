from flask import Flask, request

from main import main

app = Flask(__name__)

@app.put("/analyse")
def analyse():
    data = request.get_json()
    print(data)

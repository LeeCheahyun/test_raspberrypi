from flask import Flask

app = Flask(__name__)

@app.route("/")
def helloworld():
    str = "hello world! leecheahyun"
    return str

app.run(host='0.0.0.0', port='8000')
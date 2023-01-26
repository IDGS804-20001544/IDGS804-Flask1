from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return "Hola mundo! este mensaje es nuevo"

@app.route("/hola")
def hola():
    return "Hola mundo comprame algo de comer!"

if __name__ == "__main__":
    app.run(debug=True)

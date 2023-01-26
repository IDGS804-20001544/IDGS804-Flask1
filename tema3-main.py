from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return "Hola mundo!"

#pasamos un string
@app.route("/username/<string:username>")
def username(username):
    return "Hola " + username

#pasamos un parametro int
@app.route("/numero/<int:n>")
def numero(n):
    return "Numero: {}".format(n)

#pasamos mas de un parametro
@app.route("/user/<int:id/<string:username>")
def user(id,username):
    return "ID : {} Nombre:{}".format(id,username)

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask
from flask import request

app=Flask(__name__)

@app.route("/suma",methods=["GET","POST"])
def suma():
    if request.method == "POST":
        num1=request.form.get("num1")
        num2=request.form.get("num2")
        op=request.form.get("op")
        
        if op == "suma":
            return "<h1> la Suma es : {}</h1>".format(str(int(num1)+int(num2)))
        if op == "resta":
             return "<h1> la Resta es : {}</h1>".format(str(int(num1)-int(num2)))
        if op == "multiplicacion":
                 return "<h1> la Multiplicacion es : {}</h1>".format(str(int(num1)*int(num2)))
        if op == "division":
             return "<h1> la Division es : {}</h1>".format(str(int(num1)/int(num2)))

    else:
        return'''
        <form action="/suma" method="POST">
        <input type="radio" id="1" name="op" value="suma">
        <label>Suma</label> <br></br>
        <input type="radio" id="2" name="op" value="resta">
        <label>Resta</label> <br></br>
        <input type="radio" id="3" name="op" value="multiplicacion">
        <label>Multiplicacion</label> <br></br>
        <input type="radio" id="4" name="op" value="division">
        <label>Division</label> <br></br>


        <label>N1: </label>
        <input type="text" name="num1"/><br></br>
        <label>N2: </label>
        <input type="text" name="num2"/><br></br>
        <input type="submit" value="Calcular"/>
        </form>
        
    '''
    

if __name__ == "__main__":
    app.run(debug=True)
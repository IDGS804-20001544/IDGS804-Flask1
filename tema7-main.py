from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/operasbas")
def operasbas():
    return render_template("operasbas.html",)

@app.route("/resultado",methods=["GET","POST"])
def resultado():
     num1=request.form.get("txtNum1")
     num2=request.form.get("txtNum2")
     res= int(num1)*int(num2)
     return render_template("resultado.html",num1=num1,num2=num2,res=res)
     
if __name__ == "__main__":
     app.run(debug=True)   
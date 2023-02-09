from flask import Flask,render_template,request
import os
app=Flask(__name__)

    
@app.route("/cinepolis")
def cinepolis():
    return render_template("cinepolis.html",)

@app.route("/resultadocinepolis",methods=["GET","POST"])
def resultado():
    #aqui se definen las variables a utilizar
    nombre=request.form.get("txtnombre") 
    compradores=request.form.get("txtcompradores")
    cineco=request.form.get("cineco")
    boletos=request.form.get("txtboletos")
    
    
    #a qui se realiza las operaciones 
    while int(boletos) <= int(compradores) * 7:
        descuento = 0
        costo= int(boletos) * 12
        if int(boletos)> 6:
            descuento=costo-(0.15 * costo)
        elif  int(boletos) == 3|int(boletos) ==4 | int(boletos) == 5 :
            descuento=costo-(0.10*costo)
        else:
            descuento= costo
        
        #se re asigna el valor a la variable de descuento
        if cineco == "si":
            descuento = descuento - (descuento * 0.10)
        return render_template("resultadocinepolis.html", descuento=descuento,nombre=nombre,boletos=boletos)    
    return "<h1> No puedes comprar mas de 7 boletos por persona</h1>"

  

     
if __name__ == "__main__":
     app.run(debug=True)   
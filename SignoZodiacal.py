from flask import Flask,render_template,request
import os
app=Flask(__name__)

    
@app.route("/datos")
def datosPersonales():
    return render_template("SignoZodiacal.html")

@app.route("/resultado",methods=["post"])
def resultado():
    nombre=request.form.get("txtnombre") 
    apaterno=request.form.get("txtapaterno")
    amaterno=request.form.get("txtamaterno")
    dia=request.form.get("txtdia")
    mes=request.form.get("txtmes")
    año=request.form.get("txtaño")
    masculino=request.form.get("txtmasculino")
    femenino=request.form.get("txtfemenino")
    calificacion=request.form.get("txtcalificacion")
    
    edad=0
    
    respuesta1=request.form.get("txtrespuesta1")
    respuesta2=request.form.get("txtrespuesta2")
    respuesta3=request.form.get("txtrespuesta3")
    respuesta4=request.form.get("txtrespuesta4")
    respuesta5=request.form.get("txtrespuesta5")
    
    if int(mes) > 2:
        edad = 2022 - int(año)
    elif int(mes) <= 2:
        if int(dia) > 8:
            edad = 2022 - int(año)
        elif int(dia) <= 8:
            edad = 2023 - int(año)
    
    if respuesta1 == "1":
        respuesta1 = 1
    else: 
        respuesta1 = 0 
 
    if respuesta2 == "4":
        respuesta2 = 1
    else: 
        respuesta2 = 0 
    
    if respuesta3 == "1":
        respuesta3 = 1
    else: 
        respuesta3 = 0                
    
    if respuesta4 == "2":
        respuesta4 = 1
    else: 
        respuesta4 = 0 
    
    if respuesta5 == "3":
        respuesta5 = 1
    else: 
        respuesta5 = 0
    
    total=respuesta1+respuesta2+respuesta3+respuesta4+respuesta5
    
    zodiaco = ""
    image = ""
    a = int(año)
    while a > 1911:
        a -= 12
        if a == 1900:
            zodiaco = "RATA"
            image = "https://www.clarin.com/pages/bundles/horoscopochino/images/rata@2x.png"
        elif a == 1901:
            zodiaco = "BUEY"
            image = "https://www.euroresidentes.com/horoscopo-chino/2017/imagenes/ox-euroresidentes.jpg"
        elif a == 1902:
            zodiaco = "TIGRE"
            image = "https://www.euroresidentes.com/horoscopo-chino/2017/imagenes/tiger-euroresidentes.jpg"
        elif a == 1903:
            zodiaco = "CONEJO"
            image = "https://www.euroresidentes.com/horoscopo-chino/2017/imagenes/rabbit-euroresidentes.jpg"
        elif a == 1904:
            zodiaco = "DRAGÓN"
            image = "https://www.euroresidentes.com/horoscopo-chino/2017/imagenes/dragon-euroresidentes.jpg"
        elif a == 1905:
            zodiaco = "SERPIENTE"
            image = "https://www.euroresidentes.com/horoscopo-chino/2017/imagenes/sneg-euroresidentes.jpg"
        elif a == 1906:
            zodiaco = "CABALLO"
            image = "https://www.euroresidentes.com/horoscopo-chino/2017/imagenes/horse-euroresidentes.jpg"
        elif a == 1907:
            zodiaco = "CABRA"
            image = "https://www.euroresidentes.com/horoscopo-chino/2017/imagenes/horse-euroresidentes.jpg"
        elif a == 1908:
            zodiaco = "MONO"
            image = "https://www.euroresidentes.com/horoscopo-chino/2017/imagenes/monkey-euroresidentes.jpg"
        elif a == 1909:
            zodiaco = "GALLO"
            image = "https://www.euroresidentes.com/horoscopo-chino/2017/imagenes/cock-euroresidentes.jpg"
        elif a == 1910:
            zodiaco = "PERRO"
            image = "https://www.euroresidentes.com/horoscopo-chino/2017/imagenes/dog-euroresidentes.jpg"
        elif a == 1911:
            zodiaco = "CERDO"
            image = "https://www.euroresidentes.com/horoscopo-chino/2017/imagenes/pig-euroresidentes.jpg"
         
    return render_template("SignoZodiacalRespuesta.html",nombre=nombre,apaterno=apaterno,amaterno=amaterno,edad=edad,total=total,zodiaco=zodiaco,image=image)




  

     
if __name__ == "__main__":
     app.run(debug=True)   
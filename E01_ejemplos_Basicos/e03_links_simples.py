#Ejemplo de hola mundo en flask
from flask import Flask

#el codigo de html tiene los links

app=Flask(__name__) #creando objeto app

codigoHtml1="""
<!DOCTYPE HTML>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Pag1</title>
  </head>
  <body style="background-color:LightBlue;">
    <h1>Hola soy la pagina 1</h1>
    <a href="/pag2">Link a la pag 2</a>
  </body>
</html>
"""

codigoHtml2="""
<!DOCTYPE HTML>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Pag2</title>
  </head>
  <body style="background-color:PaleGreen;">
    <h1>Hola soy la pagina 2</h1>
    <a href="/">Regresar</a>
  </body>
</html>
"""

@app.route("/") #pag1
def inicio(): 
    return codigoHtml1

@app.route("/pag2") #pag2
def pag2():
    return codigoHtml2

#-------------------------------------
if __name__=="__main__": #lanzando app ejemplo
    import webbrowser
    webbrowser.open("http://127.0.0.1:8000")
    app.run("127.0.0.1",8000) 

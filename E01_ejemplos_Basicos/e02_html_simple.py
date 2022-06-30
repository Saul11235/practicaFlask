#Ejemplo de hola mundo en flask
from flask import Flask

app=Flask(__name__) #creando objeto app

codigoHtml="""
<!DOCTYPE HTML>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Hola soy una web html</title>
  </head>
  <body>
    <h1>Hola soy un titulo</h1>
    <p> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum </p>
    <h2>Hola soy otro titulo</h2>
    <p> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum </p>
  </body>
</html>
"""

@app.route("/") #decorador
def holaMundo(): 
    return codigoHtml

#-------------------------------------
if __name__=="__main__": #lanzando app ejemplo
    import webbrowser
    webbrowser.open("http://127.0.0.1:8000")
    app.run("127.0.0.1",8000) 

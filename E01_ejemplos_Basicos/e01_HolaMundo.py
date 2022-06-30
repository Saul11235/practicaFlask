#Ejemplo de hola mundo en flask
from flask import Flask

app=Flask(__name__) #creando objeto app

@app.route("/") #decorador
def holaMundo(): 
    return "Hola Mundo esta es mi primera App"

#-------------------------------------
if __name__=="__main__": #lanzando app ejemplo
    import webbrowser
    webbrowser.open("http://127.0.0.1:8000")
    app.run("127.0.0.1",8000) 

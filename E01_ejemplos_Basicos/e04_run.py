#Ejemplo de  configurando  debug en  Flask
from flask import Flask

app=Flask(__name__) #creando objeto app

@app.route("/") #decorador
def holaMundo(): 
    return "Hola Mundo es una prueba de las configuraciones de app.run  en flask :) "

#-------------------------------------
if __name__=="__main__": #lanzando app ejemplo
    import webbrowser
    webbrowser.open("http://127.0.0.1:8000")
    #---------------------------
    #  port=8000
    #  debug=True  #el cliente escucha al servidor
    #              #actualiza si detecta uncambio en el prog

    app.run(debug=True, port=8000) 

#Ejemplo de  configurando  debug en  Flask
from flask import Flask
#importar para paramtros de entrada en url 

app=Flask(__name__) #creando objeto app

@app.route("/pagina") #decorador
def holaMundo(): 
    return "pagina mira la direccion"

#-------------------------------------
if __name__=="__main__": #lanzando app ejemplo
    import webbrowser
    webbrowser.open("http://127.0.0.1:8000/pagina")
    #---------------------------
    #  port=8000
    #  debug=True  #el clien te escucha al servidor

    app.run(debug=True, port=8000) 

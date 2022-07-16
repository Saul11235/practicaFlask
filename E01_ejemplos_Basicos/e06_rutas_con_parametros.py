#Ejemplo de  configurando  debug en  Flask
from flask import Flask,request
#importar para paramtros de entrada en url 

app=Flask(__name__) #creando objeto app


#
# SIN PARAMETROS, MUESTRA VALOR  POR DEFECTO
#http://127.0.0.1:8000/pagina
# CON PARAMETROS, 
#http://127.0.0.1:8000/pagina?valor=valorColocado
#http://127.0.0.1:8000/pagina?valor=valorColocado&valor2=otroVal
@app.route("/pagina") #decorador
def holaMundo(): 
    #                            #nombreParametro  #valorPorDefecto
    valorObtenido=request.args.get("valor","No hay valor que mostrar")
    return "pagina con parametro : "+valorObtenido

#-------------------------------------
if __name__=="__main__": #lanzando app ejemplo
    import webbrowser
    print("indica un valor, si no colocas valor se usara el valor por defecto ")
    valor=input("Colocar valor > ")
    valor=valor.replace(" ","")
    extra=""
    if valor!="":extra="?valor="+valor
    url="http://127.0.0.1:8000/pagina"+extra
    webbrowser.open(url)
    #---------------------------
    #  port=8000
    #  debug=True  #el clien te escucha al servidor

    app.run(debug=True, port=8000) 

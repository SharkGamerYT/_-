# importar modulos de la biblioteca Flask.
from flask import Flask , render_template

# crear objetos de la clase Flask, dando __name__ como argumento.
app = Flask(__name__)

# escribir las rutas usando las funciones "decorator".
# ruta o 'URL' predefinida.
@app.route("/")
def home():

    name = "Leo :)" # escribe tu nombre
    age = "12 años" # escribe tu edad

    return render_template('index.html' , name = name , age = age)

# define la ruta a la página web de tu padre.
app.route("/padre")

# define la ruta a la página web de tu madre.
app.route("/madre")

# define la ruta a la página web de tus amigos.
app.route("/amigo")

# agrega otras rutas, si tú quieres.




# ejecuta el archivo
if __name__  ==  '__main__':
    app.run(debug=True)

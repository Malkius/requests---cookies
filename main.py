import random
from flask import Flask, render_template, request, make_response

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/formulario", methods=["GET", "POST"])
def formulario():
    if request.method == "GET":
        return render_template("formulario.html")
    elif request.method == "POST":
        nombre = request.form.get("formGroupExampleInput")
        email = request.form.get("exampleFormControlInput1")

        print(nombre)
        print(email)

        return render_template("formulario-correcto.html")


@app.route("/juego", methods=["POST"])
def juego():
    guess = int(request.form.get("guess"))
    secret_number = int(request.cookies.get("secret_number"))

    if guess == secret_number:
        message = "Correct! The secret number is {0}".format(str(secret_number))
        response = make_response(render_template("resultado.html", message=message))
        response.set_cookie("secret_number", str(random.randint(1, 30)))  # set the new secret number
        return response
    elif guess > secret_number:
        message = "Prueba algo más pequeño."
        return render_template("resultado.html", message=message)
    elif guess < secret_number:
        message = "Prueba algo más grande."
        return render_template("resultado.html", message=message)


if __name__ == '__main__':
    app.run()

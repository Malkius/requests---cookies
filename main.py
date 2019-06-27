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
        nombre = request.cookies.get("nombre")
        email = request.cookies.get("email")

        return render_template("formulario.html", nombre=nombre, email=email)

    elif request.method == "POST":
        nombre = request.form.get("nombre")
        email = request.form.get("email")
        print(nombre)
        print(email)
        response = make_response(render_template("formulario-correcto.html",
                                                 nombre=nombre, email=email))
        response.set_cookie("nombre", nombre)
        response.set_cookie("email", email)

        return response


@app.route("/juego", methods=["GET", "POST"])
def juego():
    if request.method == "GET":
        secret_number = request.cookies.get("secret_number")  # check if there is already a cookie named secret_number
        response = make_response(render_template("juego.html"))
        if not secret_number:  # if not, create a new cookie
            new_secret = random.randint(1, 30)
            response.set_cookie("secret_number", str(new_secret))
        return response

    elif request.method == "POST":
        guess = int(request.form.get("guess"))
        secret_number = int(request.cookies.get("secret_number"))
        if guess == secret_number:
            message = "Sí, el número es {0}, eres el nuevo Rappel.".format(str(secret_number))
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

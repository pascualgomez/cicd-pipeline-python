"""This module contains the main application logic."""
# app/app.py
from flask import Flask, render_template, request
from .calculadora import sumar, restar, multiplicar, dividir

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    """Renders the main calculator page and handles the calculation logic.

    On a GET request, it displays the calculator's user interface.
    On a POST request, it processes the submitted form data to perform
    a mathematical operation (addition, subtraction,
    multiplication, or division)on two numbers.
    It handles invalid number inputs and division by zero.

    Returns:
        The rendered HTML template ('index.html') with the context of
        the calculation result.
    """
    resultado = None
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operacion = request.form["operacion"]

            if operacion == "sumar":
                resultado = sumar(num1, num2)
            elif operacion == "restar":
                resultado = restar(num1, num2)
            elif operacion == "multiplicar":
                resultado = multiplicar(num1, num2)
            elif operacion == "dividir":
                resultado = dividir(num1, num2)
            else:
                resultado = "Operación no válida"
        except ValueError:
            resultado = "Error: Introduce números válidos"
        except ZeroDivisionError:
            resultado = "Error: No se puede dividir por cero"

    return render_template("index.html", resultado=resultado)


if __name__ == "__main__":  # pragma: no cover
    # Quita debug=True para producción
    app.run(debug=True, port=5000, host="0.0.0.0")

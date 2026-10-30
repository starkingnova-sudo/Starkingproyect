
from flask import Flask, render_template, request

# Crear la aplicacion Flask
app = Flask(__name__)


# Ruta principal
@app.route("/", methods=["GET", "POST"])
def inicio():

    resultado = None
    mensaje = None
    longitud = 0
    tiene_numero = False
    tiene_simbolo = False

    # Recibir datos del formulario
    if request.method == "POST":

        contrasena = request.form.get("contrasena", "")

        # DATOS DE ENTRADA Y PROCESAMIENTO
        longitud = len(contrasena)

        tiene_numero = any(
            caracter.isdigit() for caracter in contrasena
        )

        simbolos = "@#$%&"

        tiene_simbolo = any(
            caracter in simbolos for caracter in contrasena
        )

        # CLASIFICACION DE LA CONTRASENA

        if longitud < 8:

            resultado = "Debil"

            mensaje = (
                "Tu contrasena es demasiado corta. "
                "Aumenta su longitud a 12 caracteres o mas "
                "y agrega numeros y simbolos especiales."
            )

        elif longitud >= 12 and tiene_numero and tiene_simbolo:

            resultado = "Fuerte"

            mensaje = (
                "Excelente. Tu contrasena cumple los requisitos. "
                "Mantenla privada, evita reutilizarla y activa "
                "la verificacion en dos pasos."
            )

        else:

            resultado = "Media"

            recomendaciones = []

            if longitud < 12:
                recomendaciones.append(
                    "aumenta la longitud a 12 caracteres o mas"
                )

            if not tiene_numero:
                recomendaciones.append(
                    "agrega numeros"
                )

            if not tiene_simbolo:
                recomendaciones.append(
                    "agrega simbolos especiales como @, # o $"
                )

            mensaje = (
                "Tu contrasena tiene un nivel medio. "
                "Para mejorarla, "
                + ", ".join(recomendaciones)
                + "."
            )

    # ENVIAR RESULTADOS A LA PAGINA WEB
    return render_template(
        "index.html",
        resultado=resultado,
        mensaje=mensaje,
        longitud=longitud,
        tiene_numero=tiene_numero,
        tiene_simbolo=tiene_simbolo
    )


# INICIAR EL SERVIDOR
if __name__ == "__main__":
    app.run(debug=True)
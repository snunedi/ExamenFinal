from flask import Flask, render_template, request

app = Flask(__name__)

# página principal
@app.route('/')
def home():
    return render_template('index.html')

#ejercicio 1
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        # Recibiendo datos
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])

        # Precios
        precio_unitario = 9000
        total_sin_descuento = precio_unitario * cantidad

        # Determinar el descuento
        if 18 <= edad <= 30:
            descuento = total_sin_descuento * 0.15
        elif edad > 30:
            descuento = total_sin_descuento * 0.25
        else:
            descuento = 0

        # Total con el descuento aplicado
        total_con_descuento = total_sin_descuento - descuento

        # variables
        return render_template(
            'resultado1.html',
            nombre=nombre,
            total_sin_descuento=total_sin_descuento,
            descuento=descuento,
            total_con_descuento=total_con_descuento
        )
    return render_template('ejercicio1.html')

# ejercicio 2
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    # usuarios y contraseñas
    usuarios = {'juan': 'admin', 'pepe': 'user'}

    if request.method == 'POST':
        # Recibiendo datos del formulario
        nombre = request.form['nombre']
        contrasena = request.form['contrasena']


        if nombre in usuarios and usuarios[nombre] == contrasena:
            if nombre == 'juan':
                mensaje = f"Bienvenido administrador {nombre}"
            else:
                mensaje = f"Bienvenido usuario {nombre}"
        else:
            mensaje = "Usuario o contraseña incorrectos"


        return render_template('resultado2.html', mensaje=mensaje)

    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)
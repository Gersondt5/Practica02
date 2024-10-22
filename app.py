from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form1', methods=['GET', 'POST'])
def form1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        curso = request.form['curso']
        return render_template('result.html', form='form1', nombre=nombre, apellido=apellido, curso=curso)
    return render_template('form1.html')

@app.route('/form2', methods=['GET', 'POST'])
def form2():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        correo = request.form['correo']
        contrasena = request.form['contrasena']
        return render_template('result_form2.html', nombre=nombre, apellido=apellido, correo=correo, contrasena=contrasena)
    return render_template('form2.html')

@app.route('/form3', methods=['GET', 'POST'])
def form3():
    if request.method == 'POST':
        producto = request.form['producto']
        categoria = request.form['categoria']
        precio = request.form['precio']
        return render_template('result_form3.html', producto=producto, categoria=categoria, precio=precio)
    return render_template('form3.html')

@app.route('/form4', methods=['GET', 'POST'])
def form4():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        resumen = request.form['resumen']
        modo = request.form['modo']
        return render_template('result_form4.html', titulo=titulo, autor=autor, resumen=resumen, modo=modo)
    return render_template('form4.html')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, jsonify, request, render_template, redirect, url_for, flash
import requests

app = Flask(__name__)
app.secret_key = "supersecreto"

FASTAPI_URL = "http://127.0.0.1:5001"

# Configuración de la aplicación Flask
@app.route('/', methods=['GET'])
def home():
    return render_template('agregar.html')


@app.route('/consulta', methods=['GET'])
def consulta():
    return render_template('consulta.html')

#ruta para la vista de editar
@app.route('/actualizar/<int:id>', methods=['GET'])
def actualizar_usuario(id):
    try:
        response = requests.get(f"{FASTAPI_URL}/usuarios/{id}")
        if response.status_code == 200:
            usuario = response.json()
            return render_template('editar.html', usuario=usuario)
        else:
            flash("No se encontró el usuario", "danger")
            return redirect(url_for('get_usuarios'))
    except requests.exceptions.RequestException as e:
        flash(f"No se pudo conectar a la API: {str(e)}", "danger")
        return redirect(url_for('get_usuarios'))

#ruta para agregar un usuario
@app.route('/agregar', methods=['POST'])
def post_usuario():
    try: 
        usuarioNuevo = {
            "name": request.form['txtNombre'],
            "age": int(request.form['txtEdad']),
            "email": request.form['txtCorreo']
        }
    
        response = requests.post(f"{FASTAPI_URL}/usuarios/", json=usuarioNuevo)

        if response.status_code == 200 or response.status_code == 201:
            flash("Usuario creado exitosamente", "success")
        else:
            flash(f"Error al crear el usuario: {response.json().get('detail', 'error desconocido')}", "danger")
    
        return redirect(url_for('home'))

    except requests.exceptions.RequestException as e:
        flash(f"No se pudo conectar a la API: {str(e)}", "danger")
        return redirect(url_for('home'))

#ruta para consultar todos los usuarios
@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    try:
        response = requests.get(f"{FASTAPI_URL}/usuarios")
        response.raise_for_status()
        usuarios = response.json()
        return render_template('consultar.html', usuarios=usuarios)
    except requests.exceptions.RequestException as e:
        flash(f"No se pudo conectar a la API: {str(e)}", "danger")
        return redirect(url_for('consulta'))
    
#ruta para consultar un usuario por id    
@app.route('/usuarios/actualizar/<int:id>', methods=['POST'])
def put_usuario(id):
    try: 
        usuarioActualizado = {
            "name": request.form['txtNombre'],
            "age": int(request.form['txtEdad']),
            "email": request.form['txtCorreo']
        }
        response = requests.put(f"{FASTAPI_URL}/usuarios/{id}", json=usuarioActualizado)

        if response.status_code == 200 or response.status_code == 201:
            flash("Usuario actualizado exitosamente", "success")
        else:
            flash(f"Error al actualizar el usuario: {response.json().get('detail', 'error desconocido')}", "danger")
    
        return redirect(url_for('get_usuarios'))
    except requests.exceptions.RequestException as e:
        flash(f"No se pudo conectar a la API: {str(e)}", "danger")
        return redirect(url_for('actualizar_usuario', id=id))

#ruta para eliminar un usuario por id    
@app.route('/usuarios/eliminar/<int:id>', methods=['GET', 'POST'])
def eliminar_usuario(id):
    try:
        response = requests.delete(f"{FASTAPI_URL}/usuarios/{id}")
        if response.status_code == 200:
            flash("Usuario eliminado exitosamente", "success")
        else:
            flash(f"Error al eliminar el usuario", "danger")
    except requests.exceptions.RequestException as e:
        flash(f"No se pudo conectar a la API: {str(e)}", "danger")
    
    return redirect(url_for('get_usuarios'))

if __name__ == '__main__':
    app.run(debug=True, port=8002)
    
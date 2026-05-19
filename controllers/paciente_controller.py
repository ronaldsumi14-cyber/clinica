
from flask import Blueprint, render_template, request, redirect
from database import db
from models.paciente_model import Paciente

paciente_bp = Blueprint('paciente', __name__)

@paciente_bp.route('/pacientes')
def pacientes():
    datos = Paciente.query.all()
    return render_template('pacientes/index.html', pacientes=datos)

@paciente_bp.route('/pacientes/agregar', methods=['GET','POST'])
def agregar_paciente():
    if request.method == 'POST':
        p = Paciente(
            nombre=request.form['nombre'],
            edad=request.form['edad'],
            direccion=request.form['direccion'],
            telefono=request.form['telefono']
        )
        db.session.add(p)
        db.session.commit()
        return redirect('/pacientes')
    return render_template('pacientes/agregar.html')

@paciente_bp.route('/pacientes/eliminar/<int:id>')
def eliminar_paciente(id):
    p = Paciente.query.get(id)
    db.session.delete(p)
    db.session.commit()
    return redirect('/pacientes')

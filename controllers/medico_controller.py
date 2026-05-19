
from flask import Blueprint, render_template, request, redirect
from database import db
from models.medico_model import Medico

medico_bp = Blueprint('medico', __name__)

@medico_bp.route('/medicos')
def medicos():
    datos = Medico.query.all()
    return render_template('medicos/index.html', medicos=datos)

@medico_bp.route('/medicos/agregar', methods=['GET','POST'])
def agregar_medico():
    if request.method == 'POST':
        m = Medico(
            nombre=request.form['nombre'],
            especialidad=request.form['especialidad'],
            telefono=request.form['telefono'],
            correo=request.form['correo']
        )
        db.session.add(m)
        db.session.commit()
        return redirect('/medicos')
    return render_template('medicos/agregar.html')

@medico_bp.route('/medicos/eliminar/<int:id>')
def eliminar_medico(id):
    m = Medico.query.get(id)
    db.session.delete(m)
    db.session.commit()
    return redirect('/medicos')

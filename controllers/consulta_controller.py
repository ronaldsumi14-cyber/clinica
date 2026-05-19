
from flask import Blueprint, render_template, request, redirect
from database import db
from models.consulta_model import Consulta
from models.medico_model import Medico
from models.paciente_model import Paciente

consulta_bp = Blueprint('consulta', __name__)

@consulta_bp.route('/consultas')
def consultas():
    datos = Consulta.query.all()
    return render_template('consultas/index.html', consultas=datos)

@consulta_bp.route('/consultas/agregar', methods=['GET','POST'])
def agregar_consulta():
    medicos = Medico.query.all()
    pacientes = Paciente.query.all()

    if request.method == 'POST':
        c = Consulta(
            fecha=request.form['fecha'],
            diagnostico=request.form['diagnostico'],
            tratamiento=request.form['tratamiento'],
            id_medico=request.form['id_medico'],
            id_paciente=request.form['id_paciente']
        )
        db.session.add(c)
        db.session.commit()
        return redirect('/consultas')

    return render_template('consultas/agregar.html', medicos=medicos, pacientes=pacientes)

@consulta_bp.route('/consultas/eliminar/<int:id>')
def eliminar_consulta(id):
    c = Consulta.query.get(id)
    db.session.delete(c)
    db.session.commit()
    return redirect('/consultas')

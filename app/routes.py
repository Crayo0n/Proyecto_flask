from flask import Blueprint, render_template, request, jsonify
from app.validators import RegexValidator

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    results = None
    
    if request.method == 'POST':
        # Obtener los datos del formulario de validación
        nombre = request.form.get('nombre', '')
        ipv4 = request.form.get('ipv4', '')
        email = request.form.get('email', '')
        
        # Ejecutar la validación de las expresiones regulares
        results = validate_all(nombre.strip(), ipv4.strip(), email.strip())
        
    return render_template('index.html', results=results)

@bp.route('/validate', methods=['POST'])
def validate():
    """Endpoint para validar un campo individual"""
    data = request.json
    field = data.get('field')
    value = data.get('value')
    
    result = RegexValidator.validate_field(field, value)
    return jsonify(result)

@bp.route('/validate_all', methods=['POST'])
def validate_all():
    """Endpoint para validar todos los campos"""
    data = request.json
    result = RegexValidator.validate_all(data)
    return jsonify(result)
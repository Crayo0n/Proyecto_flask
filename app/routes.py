from flask import Blueprint, render_template, request, jsonify
from app.validators import RegexValidator

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    """Página principal"""
    return render_template('index.html')

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
import re

class RegexValidator:
    """Clase para centralizar las expresiones regulares y validaciones"""
    
    # Expresiones regulares
    EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    TELEFONO_REGEX = r'^\+?[1-9]\d{1,14}$'
    URL_REGEX = r'^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)$'
    
    # Mensajes de validación
    MESSAGES = {
        'email': {
            'success': 'Email válido',
            'error': 'Email inválido'
        },
        'telefono': {
            'success': 'Teléfono válido',
            'error': 'Teléfono inválido (usa formato internacional)'
        },
        'url': {
            'success': 'URL válida',
            'error': 'URL inválida (debe empezar con http:// o https://)'
        }
    }
    
    @classmethod
    def validate_email(cls, email):
        """Valida un email"""
        return bool(re.match(cls.EMAIL_REGEX, email))
    
    @classmethod
    def validate_telefono(cls, telefono):
        """Valida un número de teléfono"""
        return bool(re.match(cls.TELEFONO_REGEX, telefono))
    
    @classmethod
    def validate_url(cls, url):
        """Valida una URL"""
        return bool(re.match(cls.URL_REGEX, url))
    
    @classmethod
    def validate_field(cls, field, value):
        """Valida un campo específico y retorna el resultado"""
        validators = {
            'email': cls.validate_email,
            'telefono': cls.validate_telefono,
            'url': cls.validate_url
        }
        
        if field not in validators:
            return {'valid': False, 'message': 'Campo desconocido'}
        
        is_valid = validators[field](value)
        message = cls.MESSAGES[field]['success' if is_valid else 'error']
        
        return {'valid': is_valid, 'message': message}
    
    @classmethod
    def validate_all(cls, data):
        """Valida todos los campos"""
        results = {}
        all_valid = True
        
        fields = ['email', 'telefono', 'url']
        validators = {
            'email': cls.validate_email,
            'telefono': cls.validate_telefono,
            'url': cls.validate_url
        }
        
        for field in fields:
            value = data.get(field, '')
            is_valid = validators[field](value) if value else False
            results[field] = {
                'value': value,
                'valid': is_valid
            }
            if not is_valid:
                all_valid = False
        
        return {'all_valid': all_valid, 'results': results}

# Nombre 
REGEX_NOMBRE = r"^[A-Za-záéíóúÁÉÍÓÚñÑ\s]+$"

# Dirección IPv4 
OCTETO_REGEX = r"(\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])"
REGEX_IPV4 = r"^" + OCTETO_REGEX + r"\." + OCTETO_REGEX + r"\." + OCTETO_REGEX + r"\." + OCTETO_REGEX + r"$"

# Correo Electrónico 
REGEX_EMAIL = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

def validate_and_highlight(text, pattern):
    if not text:
        return "Ingrese un valor."
    
    match = re.fullmatch(pattern, text)
    
    if match:
        highlighted_text = f'<span class="highlight-success">{text}</span> (¡VALIDADO!)'
        return highlighted_text
    else:
        return f'<span class="highlight-error">{text}</span> (ERROR: No cumple con el formato)'

def validate_all(nombre, ipv4, email):
    """
    Ejecuta la validación para los tres campos y organiza los resultados.
    """
    results = {}
    
    results['nombre'] = {
        'input': nombre,
        'result': validate_and_highlight(nombre, REGEX_NOMBRE)
    }

    results['ipv4'] = {
        'input': ipv4,
        'result': validate_and_highlight(ipv4, REGEX_IPV4)
    }

    results['email'] = {
        'input': email,
        'result': validate_and_highlight(email, REGEX_EMAIL)
    }
    
    return results
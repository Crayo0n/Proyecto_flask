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

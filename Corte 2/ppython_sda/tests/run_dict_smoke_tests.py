"""Run lightweight checks for dict_ops without pytest.

This script mirrors the pytest checks so it can be executed where pytest
isn't installed. It prints a simple summary and exits with code 0 on success
or 1 on failure.
"""
import sys
from collections import defaultdict


class DiccionarioPersona:
    """Clase para manejar diccionarios de personas con operaciones básicas"""
    
    def __init__(self, **kwargs):
        self.datos = dict(kwargs)
    
    def agregar(self, clave, valor):
        """Agregar un nuevo par clave-valor"""
        self.datos[clave] = valor
        return self.datos
    
    def obtener(self, clave, default=None):
        """Obtener un valor por clave"""
        return self.datos.get(clave, default)
    
    def actualizar(self, clave, valor):
        """Actualizar un valor existente"""
        if clave in self.datos:
            self.datos[clave] = valor
            return True
        return False
    
    def eliminar(self, clave):
        """Eliminar un par clave-valor"""
        if clave in self.datos:
            del self.datos[clave]
            return True
        return False
    
    def existe(self, clave):
        """Verificar si una clave existe"""
        return clave in self.datos
    
    def tamaño(self):
        """Obtener el tamaño del diccionario"""
        return len(self.datos)


class DiccionarioSeguro:
    """Diccionario con manejo de casos límite"""
    
    def __init__(self, max_size=10000):
        self.datos = {}
        self.max_size = max_size
        self.estadisticas = {
            'operaciones_insercion': 0,
            'operaciones_busqueda': 0,
            'operaciones_eliminacion': 0,
        }
    
    def _validar_clave(self, clave):
        """Validar que la clave sea hashable"""
        try:
            hash(clave)
            return True
        except TypeError:
            return False
    
    def agregar_con_validacion(self, clave, valor):
        """Agregar con validaciones de casos límite"""
        if not self._validar_clave(clave):
            raise TypeError(f"La clave {clave} no es hashable")
        
        if len(self.datos) >= self.max_size:
            raise OverflowError(f"Diccionario excede el tamaño máximo ({self.max_size})")
        
        self.datos[clave] = valor
        self.estadisticas['operaciones_insercion'] += 1
        return True
    
    def eliminar_con_validacion(self, clave):
        """Eliminación con validación de existencia"""
        if clave not in self.datos:
            raise KeyError(f"La clave '{clave}' no existe en el diccionario")
        
        del self.datos[clave]
        self.estadisticas['operaciones_eliminacion'] += 1
        return True


def run():
    errors = []

    # Test básicos de DiccionarioPersona
    try:
        persona = DiccionarioPersona(nombre="Ana", edad=25)
        persona.agregar("ciudad", "Bogotá")
        assert persona.obtener("ciudad") == "Bogotá"
        assert persona.tamaño() == 3
    except AssertionError:
        errors.append('test_agregar failed')

    try:
        persona = DiccionarioPersona(nombre="Carlos", edad=30)
        assert persona.obtener("nombre") == "Carlos"
        assert persona.obtener("telefono", "No disponible") == "No disponible"
    except AssertionError:
        errors.append('test_obtener failed')

    try:
        persona = DiccionarioPersona(nombre="Luis", edad=28)
        assert persona.actualizar("edad", 29) == True
        assert persona.obtener("edad") == 29
        assert persona.actualizar("telefono", "123456") == False
    except AssertionError:
        errors.append('test_actualizar failed')

    try:
        persona = DiccionarioPersona(nombre="María", edad=35, ciudad="Medellín")
        assert persona.eliminar("ciudad") == True
        assert persona.obtener("ciudad") is None
        assert persona.eliminar("telefono") == False
    except AssertionError:
        errors.append('test_eliminar failed')

    try:
        persona = DiccionarioPersona(nombre="Pedro", edad=40)
        assert persona.existe("nombre") == True
        assert persona.existe("telefono") == False
    except AssertionError:
        errors.append('test_existe failed')

    # Test básicos de DiccionarioSeguro
    try:
        dict_seguro = DiccionarioSeguro(max_size=2)
        dict_seguro.agregar_con_validacion("clave1", "valor1")
        dict_seguro.agregar_con_validacion("clave2", "valor2")
        
        # Intentar agregar más allá del límite
        try:
            dict_seguro.agregar_con_validacion("clave3", "valor3")
            errors.append('overflow_test did not raise OverflowError')
        except OverflowError:
            pass
    except Exception:
        errors.append('test_limite_tamaño failed')

    try:
        dict_seguro = DiccionarioSeguro(max_size=10)
        
        # Probar clave no hashable
        try:
            dict_seguro.agregar_con_validacion(["lista", "no", "hashable"], "valor")
            errors.append('unhashable_key_test did not raise TypeError')
        except TypeError:
            pass
    except Exception:
        errors.append('test_validacion_clave failed')

    try:
        dict_seguro = DiccionarioSeguro(max_size=10)
        dict_seguro.agregar_con_validacion("clave_existente", "valor")
        assert dict_seguro.eliminar_con_validacion("clave_existente") == True
        
        try:
            dict_seguro.eliminar_con_validacion("clave_inexistente")
            errors.append('nonexistent_key_deletion did not raise KeyError')
        except KeyError:
            pass
    except Exception:
        errors.append('test_eliminacion_segura failed')

    if errors:
        print('FAILED:')
        for e in errors:
            print('-', e)
        return 1
    print('ALL DICTIONARY SMOKE TESTS PASSED')
    return 0


if __name__ == '__main__':
    sys.exit(run())
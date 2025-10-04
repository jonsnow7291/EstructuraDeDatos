import pytest
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
    
    def obtener_claves(self):
        """Obtener todas las claves"""
        return list(self.datos.keys())
    
    def obtener_valores(self):
        """Obtener todos los valores"""
        return list(self.datos.values())
    
    def obtener_items(self):
        """Obtener todos los pares clave-valor"""
        return list(self.datos.items())
    
    def tamaño(self):
        """Obtener el tamaño del diccionario"""
        return len(self.datos)


class DiccionarioSeguro:
    """
    Diccionario con manejo de casos límite:
    - Manejo de memoria
    - Validación de tipos de clave
    - Límites de tamaño
    - Estadísticas de colisiones
    """
    
    def __init__(self, max_size=10000):
        self.datos = {}
        self.max_size = max_size
        self.estadisticas = {
            'operaciones_insercion': 0,
            'operaciones_busqueda': 0,
            'operaciones_eliminacion': 0,
            'colisiones_simuladas': 0
        }
    
    def _validar_clave(self, clave):
        """Validar que la clave sea hashable"""
        try:
            hash(clave)
            return True
        except TypeError:
            return False
    
    def _verificar_memoria(self):
        """Verificar uso de memoria del diccionario"""
        return sys.getsizeof(self.datos)
    
    def agregar_con_validacion(self, clave, valor):
        """Agregar con validaciones de casos límite"""
        # Validar clave hashable
        if not self._validar_clave(clave):
            raise TypeError(f"La clave {clave} no es hashable")
        
        # Verificar límite de tamaño
        if len(self.datos) >= self.max_size:
            raise OverflowError(f"Diccionario excede el tamaño máximo ({self.max_size})")
        
        # Simular detección de colisión (hash simple)
        hash_simple = sum(ord(c) for c in str(clave)) % 100
        if any(sum(ord(c) for c in str(k)) % 100 == hash_simple for k in self.datos.keys() if k != clave):
            self.estadisticas['colisiones_simuladas'] += 1
        
        self.datos[clave] = valor
        self.estadisticas['operaciones_insercion'] += 1
        return True
    
    def buscar_con_estadisticas(self, clave, default=None):
        """Búsqueda con seguimiento de estadísticas"""
        self.estadisticas['operaciones_busqueda'] += 1
        return self.datos.get(clave, default)
    
    def eliminar_con_validacion(self, clave):
        """Eliminación con validación de existencia"""
        if clave not in self.datos:
            raise KeyError(f"La clave '{clave}' no existe en el diccionario")
        
        del self.datos[clave]
        self.estadisticas['operaciones_eliminacion'] += 1
        return True
    
    def obtener_estadisticas(self):
        """Obtener estadísticas completas del diccionario"""
        memoria_bytes = self._verificar_memoria()
        return {
            **self.estadisticas,
            'tamaño_actual': len(self.datos),
            'memoria_bytes': memoria_bytes,
            'memoria_mb': memoria_bytes / (1024 * 1024),
            'factor_carga': len(self.datos) / self.max_size,
            'eficiencia_hash': 1 - (self.estadisticas['colisiones_simuladas'] / max(1, self.estadisticas['operaciones_insercion']))
        }


class MaxCapacityError(Exception):
    """Error cuando se excede la capacidad máxima del diccionario"""
    pass


# Pruebas unitarias para DiccionarioPersona
def test_agregar():
    """Prueba la operación de agregar elementos"""
    persona = DiccionarioPersona(nombre="Ana", edad=25)
    persona.agregar("ciudad", "Bogotá")
    assert persona.obtener("ciudad") == "Bogotá"
    assert persona.tamaño() == 3


def test_obtener():
    """Prueba la operación de obtener elementos"""
    persona = DiccionarioPersona(nombre="Carlos", edad=30)
    assert persona.obtener("nombre") == "Carlos"
    assert persona.obtener("telefono", "No disponible") == "No disponible"


def test_actualizar():
    """Prueba la operación de actualizar elementos"""
    persona = DiccionarioPersona(nombre="Luis", edad=28)
    assert persona.actualizar("edad", 29) == True
    assert persona.obtener("edad") == 29
    assert persona.actualizar("telefono", "123456") == False


def test_eliminar():
    """Prueba la operación de eliminar elementos"""
    persona = DiccionarioPersona(nombre="María", edad=35, ciudad="Medellín")
    assert persona.eliminar("ciudad") == True
    assert persona.obtener("ciudad") is None
    assert persona.eliminar("telefono") == False


def test_existe():
    """Prueba la operación de verificar existencia"""
    persona = DiccionarioPersona(nombre="Pedro", edad=40)
    assert persona.existe("nombre") == True
    assert persona.existe("telefono") == False


def test_obtener_claves_valores_items():
    """Prueba las operaciones de obtener claves, valores e items"""
    persona = DiccionarioPersona(nombre="Ana", edad=25, ciudad="Madrid")
    
    claves = persona.obtener_claves()
    assert "nombre" in claves
    assert "edad" in claves
    assert "ciudad" in claves
    assert len(claves) == 3
    
    valores = persona.obtener_valores()
    assert "Ana" in valores
    assert 25 in valores
    assert "Madrid" in valores
    
    items = persona.obtener_items()
    assert ("nombre", "Ana") in items
    assert ("edad", 25) in items
    assert ("ciudad", "Madrid") in items


def test_tamaño():
    """Prueba la operación de obtener tamaño"""
    persona = DiccionarioPersona()
    assert persona.tamaño() == 0
    
    persona.agregar("nombre", "Juan")
    assert persona.tamaño() == 1
    
    persona.agregar("edad", 30)
    assert persona.tamaño() == 2
    
    persona.eliminar("nombre")
    assert persona.tamaño() == 1


# Pruebas para DiccionarioSeguro
def test_diccionario_seguro_validacion_clave():
    """Prueba validación de claves hashables"""
    dict_seguro = DiccionarioSeguro(max_size=10)
    
    # Clave válida (hashable)
    assert dict_seguro.agregar_con_validacion("clave_valida", "valor") == True
    
    # Clave inválida (no hashable)
    with pytest.raises(TypeError):
        dict_seguro.agregar_con_validacion(["lista", "no", "hashable"], "valor")


def test_diccionario_seguro_limite_tamaño():
    """Prueba límite de tamaño del diccionario"""
    dict_seguro = DiccionarioSeguro(max_size=2)
    
    # Agregar elementos dentro del límite
    dict_seguro.agregar_con_validacion("clave1", "valor1")
    dict_seguro.agregar_con_validacion("clave2", "valor2")
    
    # Intentar agregar más allá del límite
    with pytest.raises(OverflowError):
        dict_seguro.agregar_con_validacion("clave3", "valor3")


def test_diccionario_seguro_eliminacion():
    """Prueba eliminación con validación"""
    dict_seguro = DiccionarioSeguro(max_size=10)
    dict_seguro.agregar_con_validacion("clave_existente", "valor")
    
    # Eliminar clave existente
    assert dict_seguro.eliminar_con_validacion("clave_existente") == True
    
    # Intentar eliminar clave inexistente
    with pytest.raises(KeyError):
        dict_seguro.eliminar_con_validacion("clave_inexistente")


def test_diccionario_seguro_estadisticas():
    """Prueba el seguimiento de estadísticas"""
    dict_seguro = DiccionarioSeguro(max_size=10)
    
    # Realizar operaciones
    dict_seguro.agregar_con_validacion("clave1", "valor1")
    dict_seguro.buscar_con_estadisticas("clave1")
    dict_seguro.eliminar_con_validacion("clave1")
    
    stats = dict_seguro.obtener_estadisticas()
    
    assert stats['operaciones_insercion'] == 1
    assert stats['operaciones_busqueda'] == 1
    assert stats['operaciones_eliminacion'] == 1
    assert stats['tamaño_actual'] == 0
    assert 'memoria_bytes' in stats
    assert 'factor_carga' in stats


def test_diccionario_seguro_busqueda_con_default():
    """Prueba búsqueda con valor por defecto"""
    dict_seguro = DiccionarioSeguro(max_size=10)
    dict_seguro.agregar_con_validacion("clave_existente", "valor_existente")
    
    # Buscar clave existente
    assert dict_seguro.buscar_con_estadisticas("clave_existente") == "valor_existente"
    
    # Buscar clave inexistente con default
    assert dict_seguro.buscar_con_estadisticas("clave_inexistente", "default") == "default"
    
    # Buscar clave inexistente sin default
    assert dict_seguro.buscar_con_estadisticas("clave_inexistente") is None